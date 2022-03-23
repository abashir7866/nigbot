import os
import sys
import discord_rpc
import datetime
import asyncio
import json
from discord.ext import commands


TOKEN = json.load(open("config/config.json"))["token"]
PREFIX = json.load(open("config/config.json"))["prefix"]

bot = commands.Bot(command_prefix=PREFIX, self_bot=True)

now = datetime.datetime.now()

@bot.event
async def on_connect():
    print('Logged into a nigger')

@bot.command()
async def time(ctx):
    await ctx.message.delete
    await ctx.send ('Current date and time:')
    await ctx.send (now.strftime('%Y-%m-%d %H:%M:%S'))

@bot.command()
async def ping(ctx):
    await ctx.message.delete()
    await ctx.send('pong')

@bot.command()
async def cocks(ctx):
    await ctx.message.delete()
    await ctx.send('balls')

bot.run(TOKEN)