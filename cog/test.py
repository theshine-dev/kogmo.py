import os

import nextcord
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from nextcord.ext import commands


class TestCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def ss(self, ctx, query):
        api_key = os.getenv('YOUTUBE_API')
        youtube_api_service_name = "youtube"
        youtube_api_version = "v3"

        youtube = build(youtube_api_service_name, youtube_api_version,
                        developerKey=api_key)

        # Call the search.list method to retrieve results matching the specified
        # query term.
        search_response = youtube.search().list(
            q=query,
            order="relevance",
            part="id,snippet",  # id는 video_id만 response
            maxResults=5
        ).execute()

        # videos = []
        # channels = []
        # playlists = []

        emb = nextcord.Embed(title='유튜브 검색결과 Top 5')
        count = 0
        for search_result in search_response.get("items", []):
            if search_result["id"]["kind"] == "youtube#video":
                count += 1
                emb.add_field(name=f'{count}',
                              value='https://www.youtube.com/watch?v=' + search_result["id"]["videoId"], inline=False)

        await ctx.send(embed=emb)


def setup(bot):
    bot.add_cog(TestCog(bot))
