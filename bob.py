# bot.py
import os

import discord 
from dotenv import load_dotenv   
from discord import app_commands 
from discord.ext import commands 
import aiohttp  
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

@bot.command() 
async def gpt(ctx: commands.Context, *, prompt:str)
    async with aiohttp.ClientSession() as session:
        payload = {
            "model": "text-curie-001"
            "prompt" prompt,
            "temperature": 0.5,
            "max_tokens": 50,
            "presence_penalty": 0,
            "frequency_penalty": 0,
            "best_of":1,
        }
headers = {"Authorization": f"Bearer{API_KEY}"}    
async def with session.post("https://api.openai.com/v1/completions"), json=payload, headers=headers) as resp: