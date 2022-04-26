import nextcord
from cog.core.music.ytdl_source import YTDLSource


class Song:
    __slots__ = ('source', 'requester')

    def __init__(self, source: YTDLSource):
        self.source = source                # 유튜브 객체?
        self.requester = source.requester   # 요청한 사용자

    def create_embed(self):
        embed = (nextcord.Embed(title='Now playing',
                               description='```css\n{0.source.title}\n```'.format(self),
                               color=nextcord.Color.blurple())
                 .add_field(name='Duration', value=self.source.duration)
                 .add_field(name='Requested by', value=self.requester.mention)
                 .add_field(name='Uploader', value='[{0.source.uploader}]({0.source.uploader_url})'.format(self))
                 .add_field(name='URL', value='[Click]({0.source.url})'.format(self))
                 .set_thumbnail(url=self.source.thumbnail))

        return embed
