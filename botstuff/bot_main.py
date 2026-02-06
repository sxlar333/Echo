from pystyle import Colorate, Colors
import asyncio, os, subprocess, random, discord
from discord.ext import commands
from datetime import datetime

TOKEN = ''

intents = discord.Intents.default()
intents.message_content = True  # only if you read messages

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("current tool in very early dev")