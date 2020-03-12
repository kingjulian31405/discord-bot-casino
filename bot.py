import os
from discord.ext import commands
#from dotenv import load_dotenv

#load_dotenv()
token = os.getenv('DISCORD_TOKEN')
Guild = os.getenv('DISCORD_GUILD')
bot = commands.Bot(command_prefix='!')
