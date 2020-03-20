import os
import random

import discord
from discord.ext import commands 
from dotenv import load_dotenv
from discord.ext.commands import Bot                                                                                                                    
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name = 'casino')
async def casino(ctx):
    await ctx.send('1. Flip the coin')
    await ctx.send('2. Roll the dice')
    await ctx.send("which number game do you want to play e.g:!1 " )

@bot.command(name = '1')
async def coin_flip(ctx):
    await ctx.send(random.choice(['Head','Tail']))

@bot.command(name = '2')
async def dice_roll(ctx):
    await ctx.send(random.randint(1,7))

bot.run(TOKEN)


