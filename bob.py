# bot.py
import os

import discord 
from dotenv import load_dotenv   
from discord import app_commands 
from discord.ext import commands 
from data import get_player_stats

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

@client.tree.command(name="stats" , description= "ask specific player stats", guild=GUILD_ID)
async def NBAstats(interaction: discord.Interaction, player_name: str, season: str):
    """
    Slash command to fetch NBA player stats.
    Example usage: /stats player_name: "Lebron James" season: 2022-23"
    Args:
        interaction (discord.Interaction): _description_
        player_name (str): _description_
        season (str): _description_
    """
    # bot is loading a response
    await interaction.response.defer()

    try: 
        # grab specific player stats
        stats = get_player_stats(player_name, season)
        if isinstance(stats, str):
            await interaction.followup.send(stats)
        else:
        # format data properly
            formatted_stats = "\n".join(f"{key}:{value}" for key, value in stats.items())
            await interaction.followup.send(f"Stats for {player_name} in {season}:\n{formatted_stats}")
    except Exception as e:
        # return error if unsuccessful
        await interaction.followup.send(f"An error occurred: {str(e)}")
        return

@client.tree.command(name="news" , description= "will share important nba updates", guild=GUILD_ID)
async def NBANews(interaction: discord.Interaction):
    await interaction.response.send_message("coming soon")

@client.tree.command(name="trivia" , description= "fun facts about teams and players or league history", guild=GUILD_ID)
async def NBATrivia(interaction: discord.Interaction):
    await interaction.response.send_message("coming soon")

client.run(TOKEN) 