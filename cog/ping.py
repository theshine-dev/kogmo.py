import nextcord.ext.commands
from nextcord.ext import commands
import nextcord.ext
import nextcord


class PingPongCommandCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: nextcord.ext.commands.Context):
        #     """
        #     봇의 반응 속도(ping) 출력
        #     """
        await ctx.send(f'이 길드의 아이디는 {ctx.guild.id}')
        await ctx.send(f'이 채널의 아이디는 {ctx.channel.id}')

        await ctx.send(f':ping_pong: 퐁! ({self.bot.latency * 1000:.2f}ms)')


def setup(bot):
    bot.add_cog(PingPongCommandCog(bot))


"""
from nextcord.ext import commands


class _CLASS_NAME(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f':ping_pong: 퐁! ({self.bot.latency * 1000:.2f}ms)')

def setup(bot):
    bot.add_cog(PingPongCommandCog(bot))
"""