import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot("/")

bot.run(os.getenv("TOKEN"))
