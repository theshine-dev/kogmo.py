
import nextcord


from nextcord.ext import commands


class TestCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # @commands.command()
    # async def play(self, ctx, url):
    #     channel = ctx.author.voice.channel
    #     if not ctx.voice_client:
    #         await channel.connect()
    #         await ctx.send("connected to the voice channel, " + str(ctx.voice_client.channel))
    #
    #     ydl_opts = {'format': 'bestaudio'}
    #     FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    #                       'options': '-vn'}
    #     with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    #         info = ydl.extract_info(url, download=False)
    #         URL = info['formats'][0]['url']
    #     voice = ctx.voice_client
    #     voice.play(nextcord.FFmpegPCMAudio(URL, executable='C:/Users/Shadow/Desktop/kogmo.py/ffmpeg/bin/ffmpeg.exe', **FFMPEG_OPTIONS))
    #
    # @commands.command()
    # async def leave(self, ctx):
    #     await ctx.voice_client.disconnect()


def setup(bot):
    bot.add_cog(TestCog(bot))
