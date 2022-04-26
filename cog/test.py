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

    @commands.command()
    async def ask(self, ctx):
        """Asks the user a question to confirm something."""
        # We create the view and assign it to a variable so we can wait for it later.
        view = Confirm()
        await ctx.send('Do you want to continue?', view=view)
        # Wait for the View to stop listening for input...
        await view.wait()
        if view.value is None:
            print('Timed out...')
        elif view.value:
            print('Confirmed...')
        else:
            print('Cancelled...')

    @commands.command()
    async def image(self, ctx):
        emb = nextcord.Embed()
        emb.set_image(url="https://i.ibb.co/NjNDZgV/image.png")
        await ctx.send(embed=emb)



class Confirm(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    # When the confirm button is pressed, set the inner value to `True` and
    # stop the View from listening to more input.
    # We also send the user an ephemeral message that we're confirming their choice.
    @nextcord.ui.button(label='Confirm', style=nextcord.ButtonStyle.green)
    async def confirm(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message('Confirming', ephemeral=True)
        self.value = True
        self.stop()

    # This one is similar to the confirmation button except sets the inner value to `False`
    @nextcord.ui.button(label='Cancel', style=nextcord.ButtonStyle.grey)
    async def cancel(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message('Cancelling', ephemeral=True)
        self.value = False
        self.stop()



def setup(bot):
    bot.add_cog(TestCog(bot))
