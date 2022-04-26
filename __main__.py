import os
from os import listdir

import nextcord
from nextcord.ext import commands
import logging

from dotenv import load_dotenv

# loading the .env file
load_dotenv()

# logging
logger = logging.getLogger('nextcord')
logger.setLevel(logging.DEBUG)  # CRITICAL, ERROR, WARNING, INFO, DEBUG :: defaults to WARNING.
handler = logging.FileHandler(filename='nextcord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

#
bot = commands.Bot(command_prefix=os.getenv('COMMAND_PREFIX'))

# Load all cogs existing in dir 'cog/'
for filename in listdir('cog'):
    if filename.endswith('.py'):
        bot.load_extension(f'cog.{filename[:-3]}')
        print(f'Cog {filename}을[를] 로드 완료')


# Main
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
    await bot.change_presence(status=nextcord.Status.online, )


# Default Error Processing
@bot.event
async def on_command_error(ctx, error):
    embed = nextcord.Embed(title="Warning!")
    embed.add_field(name="Context", value=f'```{error}```')
    await ctx.send(embed=embed)


# @bot.event
# async def on_member_join(member):
#     fmt = '{1.name} 에 오신것을 환영합니다., {0.mention} 님'
#     channel = member.server.get_channel("channel_id_here")
#     await bot.get_guild(951113812130545704).get_channel(951113812130545707).send(fmt.format(member, member.server))
#
#
# @bot.event
# async def on_member_remove(member):
#     channel = member.server.get_channel("channel_id_here")
#     fmt = '{0.mention} 님이 서버에서 나가셨습니다.'
#     await bot.get_guild(951113812130545704).get_channel(951113812130545707).send(fmt.format(member, member.server))

# Running bot with Token.
if __name__ == '__main__':
    bot.run(os.getenv('BOT_TOKEN'))
