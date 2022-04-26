import random
import nextcord.ext.commands
from nextcord.ext import commands

dice = None


class EducationCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=["주사위"])
    async def dice(self, ctx: nextcord.ext.commands.Context, challenge=None):
        global dice
        if challenge is None:
            if dice is None:
                dice = random.randint(1, 7)
                print(dice)
                await ctx.send("주사위 값 설정 완료! 맞춰보세요.")
            else:
                await ctx.send("주사위가 이미 존재합니다. 맞춰보세요!")
        else:
            if int(challenge) == dice:
                await ctx.send(f"정답입니다!! 정답은 '{dice}' 입니다.")
                dice = None
            else:
                await ctx.send(f'땡 ! 틀렸습니다.')


def setup(bot):
    bot.add_cog(EducationCog(bot))
