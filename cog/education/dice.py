from nextcord.ext import commands


class CLASS_NAME(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def DEF_NAME(self, ctx):
        await ctx.send(f':ping_pong: 퐁! ({self.bot.latency * 1000:.2f}ms)')


def setup(bot):
    bot.add_cog(CLASS_NAME(bot))
