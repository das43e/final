import discord
import python_weather
import asyncio
import os
from discord.ext import commands
from key import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def getweather(ctx, city_1):
  # declare the client. the measuring unit used defaults to the metric system (celcius, km/h, etc.)
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
    # fetch a weather forecast from a city
        weather = await client.get(city_1)
    
    # returns the current day's forecast temperature (int)
        x = (weather.temperature)
        x = int((x - 32)//1.8)
        await ctx.send (f"{x} градусов")
        if x <= 0:
            await ctx.send("у вас ПРОХЛАДНО одевайте кофточки https://tenor.com/view/прохладно-холодно-пофиг-gif-10165769616949418659")
        elif x > 0 and x < 15:
            await ctx.send("у вас нормально https://tenor.com/view/russian-walrus-gif-20380833")
        elif x >= 15 and x <= 25:
            await ctx.send("У вас уже все окей можно ходить купатся https://tenor.com/view/gorilla-bath-warm-shower-happy-gif-9037913 ")
        elif x > 25:
            await ctx.send("У вас ЖАРКО БЕГИТЕ АААААААААААА")
            await ctx.send("https://images-ext-1.discordapp.net/external/rdw-Vytou-jan9rQvrBqckxudivqoFNETudkv_4FDV8/https/media.tenor.com/Vy3EdabkUo0AAAPo/yang-gang-fitness-yanggang.mp4you")
bot.run(key())