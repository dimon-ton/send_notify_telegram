import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()


channel_id = os.getenv('CHANNEL_ID')
token = os.getenv('DISCORD_TOKEN')

int_channel_id = int(channel_id)

print(int_channel_id)

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f'Bot ready')

    guild = discord.utils.get(bot.guilds)

    channel = bot.get_channel(int_channel_id)

    if channel:
        file_path = 'image.jpg'
        
        try:
            with open(file_path, "rb") as image:
                file = discord.File(image)

                embed_image = discord.Embed(title="สวัสดี", description="ส่งรูปภาพ", color=discord.Color.green())

                embed_image.set_image(url=f"attachment://{file.filename}")
                await channel.send(embed=embed_image, file=file)
        except FileNotFoundError:
            print("ไม่พบไฟล์ กรุณาตรวจสอบเส้นทาง")


    else:
        print("ไม่พบช่องที่ต้องการส่งข้อความ")


bot.run(token)