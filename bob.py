# bot.py
import os

import discord 
from dotenv import load_dotenv   
from discord import app_commands 
from discord.ext import commands 

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD_ID')

class Client(commands.Bot):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord yay!')
         
        try:
            guild = discord.Object(GUILD)
            synced = await self.tree.sync(guild=guild)
            print(f'Synced {len(synced)} commands to guild {guild.id}')

        except Exception as e:
            print(f'Error syncing commands: {e}')

            
    async def on_message(self,message):
        if message.author == self.user:
            return

        if message.content.startswith('hello'):
            await message.channel.send(f'hi there {message.author}')
    

intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix="!", intents=intents)

GUILD_ID= discord.Object(id=GUILD)


@client.tree.command(name="hello" , description= "say hello!", guild=GUILD_ID)
async def sayHello(interaction: discord.Interaction):
    await interaction.response.send_message("Hi there")
   
@client.tree.command(name="copycat" , description= "i will copy whatever you say!", guild=GUILD_ID)
async def sayHello(interaction: discord.Interaction, printer: str):
    await interaction.response.send_message(printer)

client.run(TOKEN) 