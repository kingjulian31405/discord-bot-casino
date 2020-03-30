from discord.ext import commands
import json
import discord

bot = commands.Bot('!')

amounts = {}

@bot.event
async def on_ready():
    global amounts
    try:
        with open('amounts.json') as f:
            amounts = json.load(f)
    except FileNotFoundError:
        print("Could not load amounts.json")
        amounts = {}

@bot.command(name = 'check')
async def balance(ctx):
    id = ctx.message.author.id
    if id in amounts:
        await ctx.send("You have {} in your account".format(amounts[ctx.message.author.id]))
    else:
        await ctx.send("Created a user first")

@bot.command(name = 'register')
async def register(ctx):
    id = ctx.message.author.id
    if id not in amounts:
        amounts[id] = 100
        await ctx.send("You are now registered")
    else:
        await ctx.send("You already have an account")

@bot.command(name = 'accounts')
async def active(ctx):
        await ctx.send(amounts)

@bot.command(name = 'save')
async def save(ctx):
    with open('amounts.json', 'w+') as f:
        json.dump(amounts, f)
    await ctx.send("everything was save")
