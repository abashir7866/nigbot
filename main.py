import os
import sys
import discord_rpc
import json
from discord.ext import commands


TOKEN = json.load(open("config/config.json"))["token"]
PREFIX = json.load(open("config/config.json"))["prefix"]

bot = commands.Bot(command_prefix=PREFIX, self_bot=True)


@bot.event
async def on_connect():
    print('Logged into a nigger')



@bot.command()
async def ping(ctx):
    await ctx.message.delete()
    await ctx.send('pong')

@bot.command()
async def cocks(ctx):
    await ctx.message.delete()
    await ctx.send('balls')

bot.run(TOKEN)