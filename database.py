from discord.ext import commands
import json
import discord
import os
 
bot = commands.Bot('!')
 
@bot.event
async def on_ready():
    global users
    if os.path.exists('users.json'):
        with open('users.json', 'r') as f:
            users = json.load(f)
        print("Everything is ready")
    else:
        users = {}
        print("Everything is ready")
 
@bot.command(name = 'check')
async def balance(ctx):
    ID = ctx.message.author.name
    if ID in users:
        await ctx.send("You have {} in your account".format(users[ID]))
    else:
        await ctx.send("Register first")
 
@bot.command(name = 'register')
async def register(ctx):
    ID = ctx.message.author.name
    if ID not in users:
        users[ID] = 100
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
    
 
@bot.command(name = 'losed')
async def subtract(ctx):
    ID = ctx.message.author.name
    users[ID] -= 10
    with open('users.json', 'w+') as f:
        json.dump(users, f)
    await ctx.send("Money taken away")
 
@bot.command(name = 'gain')
async def add(ctx):
    ID = ctx.message.author.name
    amount = users[ID] + 50
    with open('users.json', 'w+') as f:
        users[ID] = amount
        json.dump(users, f)
    await ctx.send("Money added")

bot.run("BOT-TOKEN")
