from nextcord.ext import commands


class PingPongCommandCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        #     """
        #     봇의 반응 속도(ping) 출력
        #     """
        await ctx.send(f':ping_pong: 퐁! ({self.bot.latency * 1000:.2f}ms)')


def setup(bot):
    bot.add_cog(PingPongCommandCog(bot))
