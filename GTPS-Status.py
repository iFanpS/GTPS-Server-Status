#Made by iFanpS
#Inspired from KIPAS#1823
import discord
from datetime import datetime
import os
from discord import client
from discord.ext import commands

def install_discord():
    os.system('python3 -m pip install -U discord.py')

bot = commands.Bot(command_prefix="s.")

client = discord.Client()
@bot.event
async def on_ready():
    print(f"{client.user} is on now")

@bot.command()
async def status(ctx):
    player = open('online.txt').readlines()
    listworld = len(os.listdir('worlds'))
    time = datetime.now()
    clock = time.strftime('%H:%M %p')
    embed1 = discord.Embed(color=0x00ff00, title="STATUS SERVER")
    embed1.add_field(name="Player online:", value=player[0])
    embed1.add_field(name="Wolrd created:", value=listworld)
    embed1.set_footer(text="Last update today" + clock)
    msgstatus = await ctx.send(embed=embed1)
    while True:
            player = open('online.txt').readlines()
            listworld = len(os.listdir('worlds'))
            time = datetime.now()
            clock = time.strftime('%H %M %p')
            embed2 = discord.Embed(color=0x00ff00, title="STATUS SERVER")
            embed1.add_field(name="Player online:", value=player[0])
            embed1.add_field(name="Wolrd created:", value=listworld)
            embed2.set_footer(text="Last update today " + clock)
            await msgstatus.edit(embed=embed2)

bot.run('YOUR-TOKEN')