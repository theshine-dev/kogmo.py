import pprint

from nextcord.ext import commands
import pymongo


#
#   id
#   닉네임
#   직급


class UserInfoCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=['등록', ])
    async def set_info(self, ctx):
        # 접속된 객체를 conn으로 받는다
        conn = pymongo.MongoClient("192.168.219.99", 27017)

        guild = ctx.guild
        # test 데이터베이스가 없으면 자동으로 생성됩니다.
        db = conn.guild
        # 컬렉션은 테이블같은 개념. sql에서는 table , mongodb는 컬렉션.
        # members 컬렉션 없을 경우 생성됨.
        col = db.members

        print(ctx.author.name)
        payload = {"userid": ctx.author.id,
                   "name": ctx.author.name,
                   }

        # 정보 삽입 (반복해서 수행할 경우 같은 정보가 계속 인서트 됩니다. --> 중복 가능)
        _id = col.insert_one(payload).inserted_id

    @commands.command(aliases=['내정보', ])
    async def get_info(self, ctx):
        # 접속된 객체를 conn으로 받는다
        conn = pymongo.MongoClient("192.168.219.99", 27017)

        guild = ctx.guild
        # test 데이터베이스가 없으면 자동으로 생성됩니다.
        db = conn.guild
        # 컬렉션은 테이블같은 개념. sql에서는 table , mongodb는 컬렉션.
        # members 컬렉션 없을 경우 생성됨.
        col = db.members

        pprint.pprint(col.find_one({"userid": ctx.author.id}))


def setup(bot):
    bot.add_cog(UserInfoCog(bot))
