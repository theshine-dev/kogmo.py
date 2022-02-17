import os
from os import listdir

import nextcord
from nextcord.ext import commands
import logging

from dotenv import load_dotenv

load_dotenv()

# logging
logger = logging.getLogger('nextcord')
logger.setLevel(logging.DEBUG)  # CRITICAL, ERROR, WARNING, INFO, DEBUG :: defaults to WARNING.
handler = logging.FileHandler(filename='nextcord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# the prefix is not used in this example
bot = commands.Bot(command_prefix='~')

# Load all cogs existing in dir 'cog'
for filename in listdir('cog'):
    if filename.endswith('.py'):
        bot.load_extension(f'cog.{filename[:-3]}')
        print(f'Cog {filename}을[를] 로드 완료')


# Main
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.event
async def on_command_error(ctx, error):
    embed = nextcord.Embed(title="Error occur!")
    embed.add_field(name="내용", value=f'```{error}```')
    await ctx.send(embed=embed)


# Running bot with Token.
if __name__ == '__main__':
    bot.run(os.getenv('BOT_TOKEN'))
