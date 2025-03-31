import discord
from discord import Webhook
import aiohttp
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()

webhooks = os.getenv('WEBHOOK_URL')


async def anything(webhook_url):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(webhook_url, session=session)
        embed = discord.Embed(title="นี่่คือ webhook จาก uncle engineer")
        await webhook.send(embed=embed, username="Harry")
        print("webhook sent successfully")

if __name__ == "__main__":
    
    loop = asyncio.new_event_loop()
    loop.run_until_complete(anything(webhooks))
    loop.close()