"""
https://open.neis.go.kr/hub/mealServiceDietInfo?

Type=json
ATPT_OFCDC_SC_CODE=B10
SD_SCHUL_CODE=7130114
MLSV_YMD=20220419
"""
from datetime import datetime
import json

from nextcord.ext import commands
import requests


async def getMeal(when):
    url = "https://open.neis.go.kr/hub/mealServiceDietInfo"
    param = {
        "Type": "json",  # json으로 받아와라
        "ATPT_OFCDC_SC_CODE": "B10",  # 시도교육청 코드
        "SD_SCHUL_CODE": "7130114",  # 학교코드
        "MLSV_YMD": when  # 날짜
    }
    response = requests.get(url, param)
    json_obj = json.loads(response.text)
    meals = json_obj['mealServiceDietInfo'][1]['row'][0]['DDISH_NM'].replace("<br/>", "\n")

    return meals


class MealCommandCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=['급식', '밥', '식사'])
    async def meals(self, ctx, *, when=datetime.today().strftime("%Y%m%d")):    #!급식 20220419
        """
        급식 정보를 받아오는 명령어
        """
        meals = await getMeal(when)
        await ctx.send(meals)


def setup(bot):
    bot.add_cog(MealCommandCog(bot))
