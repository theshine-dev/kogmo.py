import nextcord
from googleapiclient.errors import HttpError
from nextcord.ext import commands
from core.youtube import YTDLSource, youtube_search


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Commands
    @commands.command()
    async def join(self, ctx, *, channel: nextcord.VoiceChannel):
        """채널명을 입력하여 봇을 입장시킴"""

        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)

        await channel.connect()

    @commands.command()
    async def yt(self, ctx, *, url):
        """Plays from a url (almost anything youtube_dl supports)"""

        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=self.bot.loop)
            ctx.voice_client.play(player, after=lambda e: print(f'Player error: {e}') if e else None)

        await ctx.send(f'Now playing: {player.title}')

    @commands.command()
    async def stream(self, ctx, *, url):
        """Streams from a url (same as yt, but doesn't predownload)"""

        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
            ctx.voice_client.play(player, after=lambda e: print(f'Player error: {e}') if e else None)

        await ctx.send(f'Now playing: {player.title}')

    @commands.command()
    async def volume(self, ctx, volume: int):
        """Changes the player's volume"""

        if ctx.voice_client is None:
            return await ctx.send("Not connected to a voice channel.")

        ctx.voice_client.source.volume = volume / 100
        await ctx.send(f"Changed volume to {volume}%")

    @commands.command(aliases=['p', ])
    async def play(self, ctx, *, query):
        """검색어를 입력 받아, 유튜브에서 가장 관련 있는 동영상 음원 재생"""

        try:
            id = await youtube_search(query)

            async with ctx.typing():
                url = 'https://www.youtube.com/watch?v='
                player = await YTDLSource.from_url(url + id, loop=self.bot.loop, stream=True)
                ctx.voice_client.play(player, after=lambda e: print(f'Player error: {e}') if e else None)

            await ctx.send(f'Now playing: {player.title}')

        except HttpError as e:
            await ctx.send(f'An Http Error {e.resp.statue} occurred:{e.content}')

    @commands.command(aliases=['s', ])
    async def stop(self, ctx):
        """Stops and disconnects the bot from voice"""

        await ctx.voice_client.disconnect(force=False)

    @play.before_invoke
    @stream.before_invoke
    @stop.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("You are not connected to a voice channel.")
                raise commands.CommandError("Author not connected to a voice channel.")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()


def setup(bot):
    bot.add_cog(Music(bot))
