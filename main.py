import os
import sys
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
    await ctx.message.delete()
    await ctx.send ('Current date and time:')
    await ctx.send (now.strftime('%Y-%m-%d %H:%M:%S'))

@bot.command()
async def ping(ctx):
    await ctx.message.delete()
    await ctx.send('pong')

@bot.command()
async def neko(ctx):
    await ctx.message.delete()
    neko = requests.get("https://nekos.life/api/v2/img/neko").json()["url"]
    await ctx.send(neko)

@bot.command()
async def vaporeon(ctx):
    await ctx.message.delete()
    await ctx.send("Hey guys, did you know that in terms of male human and female Pokémon breeding, Vaporeon is the most compatible Pokémon for humans? Not only are they in the field egg group, which is mostly comprised of mammals, Vaporeon are an average of 3”03’ tall and 63.9 pounds, this means they’re large enough to be able handle human dicks, and with their impressive Base Stats for HP and access to Acid Armor, you can be rough with one. Due to their mostly water based biology, there’s no doubt in my mind that an aroused Vaporeon would be incredibly wet, so wet that you could easily have sex with one for hours without getting sore. They can also learn the moves Attract, Baby-Doll Eyes, Captivate, Charm, and Tail Whip, along with not having fur to hide nipples, so it'd be incredibly easy for one to get you in the mood. With their abilities Water Absorb and Hydration, they can easily recover from fatigue with enough water. No other Pokémon comes close to this level of compatibility. Also, fun fact, if you pull out enough, you can make your Vaporeon turn white. Vaporeon is literally built for human dick. Ungodly defense stat+high HP pool+Acid Armor means it can take cock all day, all shapes and sizes and still come for more")

@bot.command()
async def minion(ctx):
    await ctx.message.delete()
    minion = requests.get("https://api.benny.fun/v1/minion").json()["minion"]
    await ctx.send(minion)

@bot.command()
async def risesrc(ctx):
    await ctx.message.delete()
    await ctx.send('guys i found rise src')
    await ctx.send('https://github.com/reactdev1337/reactselfbot')

@bot.command()
async def cocks(ctx):
    await ctx.message.delete()
    await ctx.send('balls')

bot.run(TOKEN)