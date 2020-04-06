import os
import random
import asyncio

import discord
from discord.ext import commands 
from dotenv import load_dotenv
from discord.ext.commands import Bot  

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

class MyClient(discord.Client):
    async def on_message(self, message):

        if message.author.id == self.user.id:
            return

        if message.content.startswith('!casino'):
            await message.channel.send('1. Dice Roll')
            await message.channel.send('2. Coin Toss')
            await message.channel.send('Which game do you want to play?')
       
        if message.content.startswith('Dice Roll'):
            await message.channel.send('Guess a number between 1 and 6.')
    
            def is_correct(m):
                return m.author == message.author and m.content.isdigit()

            answer = random.randint(1, 6)

            try:
                guess = await self.wait_for('message', check=is_correct, timeout=30.0)
            except asyncio.TimeoutError:
                return await message.channel.send('Sorry, you took too long it was {}.'.format(answer))

            if int(guess.content) == answer:
                await message.channel.send('You are right!')
                await message.channel.send('Do you want to play again? Yes or No')
                def ans(x):
                    return x.author == message.author and x.content
                d = 'Yes'

                try:
                    y = await self.wait_for('message',check=ans, timeout= 30.0)
                except asyncio. TimeoutError:
                    return await message.channel.send('Sorry, you took too long!')

                if y.content == d:
                    await message.channel.send('Which game do you want to play')
                else:
                    await message.channel.send('Thank You for playing')
            else:
                await message.channel.send('Oops. It is actually {}.'.format(answer))
                await message.channel.send('Do you want to play again? Yes or No')
                def ans(v):
                    return v.author == message.author and v.content
                d = 'Yes'

                try:
                    z = await self.wait_for('message',check=ans, timeout= 30.0)
                except asyncio. TimeoutError:
                    return await message.channel.send('Sorry, you took too long!')

                if z.content == d:
                    await message.channel.send('Which game do you want to play')
                else:
                    await message.channel.send('Thank You for playing')

        elif message.content.startswith('Coin Toss'):
            await message.channel.send('Do you want Heads or Tails.')

            def correct(n):
                return n.author == message.author and n.content

            a = random.choice(['Heads','Tails'])

            try:
                g = await self.wait_for('message',check=correct, timeout= 30.0)
            except asyncio.TimeoutError:
                return await message.channel.send('Sorry, you took too long it was {}.'.format(a))

            if g.content == a:
                await message.channel.send('You are right!')
                await message.channel.send('Do you want to play again? Yes or No')
                def ans(o):
                    return o.author == message.author and o.content
                d = 'Yes'

                try:
                    f = await self.wait_for('message',check=ans, timeout= 30.0)
                except asyncio. TimeoutError:
                    return await message.channel.send('Sorry, you took too long!')

                if f.content == d:
                    await message.channel.send('Which game do you want to play')
                else:
                    await message.channel.send('Thank You for playing')

            else:
                await message.channel.send('Oops. It is actually {}.' .format(a))
                await message.channel.send('Do you want to play again? Yes or No')
                def ans(p):
                    return p.author == message.author and p.content
                d = 'Yes'

                try:
                    h = await self.wait_for('message',check=ans, timeout= 30.0)
                except asyncio. TimeoutError:
                    return await message.channel.send('Sorry, you took too long!')

                if h.content == d:
                    await message.channel.send('Which game do you want to play')
                else:
                    await message.channel.send('Thank You for playing')


client = MyClient()
client.run(TOKEN)
