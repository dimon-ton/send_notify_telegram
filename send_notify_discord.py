import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv('DISCORD_TOKEN')
app_id = os.getenv('DISCORD_APP_ID')
public_key = os.getenv('DISCORD_PUBLIC_KEY')


bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Bot ready')


bot.run(token)