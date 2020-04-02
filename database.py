from discord.ext import commands
import json
import discord

bot = commands.Bot('!')

users = {}

@bot.event
async def on_ready():
    global users
    try:
        with open('users.json') as f:
            users = json.load(f)
    except FileNotFoundError:
        print("Could not load users.json")
        users = {}

@bot.command(name = 'check')
async def balance(ctx):
    id = ctx.message.author.name
    if id in users:
        await ctx.send("You have {} in your account".format(users[ctx.message.author.name]))
    else:
        await ctx.send("Register first")

@bot.command(name = 'register')
async def register(ctx):
    id = ctx.message.author.name
    if id not in users:
        users[id] = 100
        await ctx.send("You are now registered")
    else:
        await ctx.send("You already have an account")

@bot.command(name = 'accounts')
async def active(ctx):
        await ctx.send(users)

@bot.command(name = 'save')
async def save(ctx):
    with open('users.json', 'w+') as f:
        json.dump(users, f)
    await ctx.send("everything was save")
    
    
@bot.command(name = 'up')
async def testing(ctx):
    users[id] += 2
    await ctx.send("up")

bot.run("NjkwNzAwMjQzNDMxNDU2ODM4.XoPMjg.CvJPW5q2dEiYvFL3o69lbyfdlos")
