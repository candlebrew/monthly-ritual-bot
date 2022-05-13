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
import bcrpyt # https://www.makeuseof.com/encrypt-password-in-python-bcrypt/
# https://github.com/pyca/bcrypt/
from config.sql import *

db = None
dbTimer = None
dbAlert = None

prefixList = ["m.","m!","m,","p.","p!","p,"]

## Connecting the DB ----------------------------------------------------------
async def run():
    global db
    global dbTimer
    global dbAlert
    
    dbURL = os.environ.get('DATABASE_URL')
    db = await asyncpg.connect(dsn=dbURL, ssl='require')
    dbTimer = await asyncpg.connect(dsn=dbURL, ssl='require')
    dbAlert = await asyncpg.connect(dsn=dbURL, ssl='require')
    
    for i in [userDataTableSQL,prefTableSQL,symptomsTableSQL,encountersTableSQL,defaultTermsTableSQL,customTermsTableSQL]: # found in config.sql
        await db.execute(i)
    
## Bot Setup ----------------------------------------------------------
    
token = os.environ.get('DISCORD_BOT_TOKEN') # This is hosted on Heroku

client = discord.Client()

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=prefixList, intents=intents, db=db, dbTimer=dbTimer, dbAlert=dbAlert)

## Code Here ----------------------------------------------------------


## Bot Setup & Activation ----------------------------------------------------------
asyncio.get_event_loop().run_until_complete(run())
bot.run(token)
