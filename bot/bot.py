import nextcord as discord
from nextcord.ext import commands
from discord.utils import get
import logging # import python logging abilities
import random # import python random abilities
import typing # tbh dont know what this is, but it's necessary to make optional parameters for commands
import os # import the OS details, including our hidden bot token
import asyncio # import the asyncio functionality, which allows our background task i.e. changing status every minute
import asyncpg
import datetime
import io
import DiscordUtils
import json
from aiohttp import request
import aiohttp
import bcrpyt

db = None

## Connecting the DB ----------------------------------------------------------
async def run():
    global db
    
    dbURL = os.environ.get('DATABASE_URL')
    db = await asyncpg.connect(dsn=dbURL, ssl='require')
    
## Bot Setup ----------------------------------------------------------
    
token = os.environ.get('DISCORD_BOT_TOKEN') # This is hosted on HEROKU

client = discord.Client()

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="prefix!", intents=intents, db=db)

## Code Here ----------------------------------------------------------


## Bot Setup & Activation ----------------------------------------------------------
asyncio.get_event_loop().run_until_complete(run())
bot.run(token)
