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
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)
client.run(TOKEN)