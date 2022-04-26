import asyncio
import os

import nextcord
import youtube_dl
from googleapiclient.discovery import build

# Suppress noise about console usage from errors
youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'  # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


class YTDLSource(nextcord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(nextcord.FFmpegPCMAudio(filename,
                                           executable=os.getenv('DIR_FFMPEG'),
                                           **ffmpeg_options), data=data)


async def youtube_search(query):
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
        maxResults=10
    ).execute()

    # videos = []
    # channels = []
    # playlists = []

    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            return search_result["id"]["videoId"]

    # # Add each result to the appropriate list, and then display the lists of
    # # matching videos, channels, and playlists.
    # for search_result in search_response.get("items", []):
    #     if search_result["id"]["kind"] == "youtube#video":
    #         videos.append("%s (%s)" % (search_result["snippet"]["title"],
    #                                    search_result["id"]["videoId"]))
    #     elif search_result["id"]["kind"] == "youtube#channel":
    #         channels.append("%s (%s)" % (search_result["snippet"]["title"],
    #                                      search_result["id"]["channelId"]))
    #     elif search_result["id"]["kind"] == "youtube#playlist":
    #         playlists.append("%s (%s)" % (search_result["snippet"]["title"],
    #                                       search_result["id"]["playlistId"]))
    #
    # print("Videos:\n", "\n".join(videos), "\n")
    # print("Channels:\n", "\n".join(channels), "\n")
    # print("Playlists:\n", "\n".join(playlists), "\n")