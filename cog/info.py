from nextcord.ext import commands
import pymongo

from datetime import datetime


class UserInfoCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=['내정보', ])
    async def info(self, ctx):
        # 접속된 객체를 conn으로 받는다
        conn = pymongo.MongoClient("192.168.219.99", 27017)
        print(1)
        guild = ctx.guild
        # test 데이터베이스가 없으면 자동으로 생성됩니다.
        db = conn.guild
        print(2)
        # 컬렉션은 테이블같은 개념. sql에서는 table , mongodb는 컬렉션.
        # members 컬렉션 없을 경우 생성됨.
        col = db.members
        print(3)

        post = {"author": ctx.author.id,
                }

        # 정보 삽입 (반복해서 수행할 경우 같은 정보가 계속 인서트 됩니다. --> 중복 가능)
        _id = col.insert_one(post).inserted_id
        print(post)
        print(_id)

def setup(bot):
    bot.add_cog(UserInfoCog(bot))
