# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

class Client(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord yay!')
        
    async def on_message(self,message):
        if message.author == self.user:
            return

        if message.content.startswith('hello'):
            await message.channel.send(f'hi there {message.author}')


intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)
client.run(TOKEN)