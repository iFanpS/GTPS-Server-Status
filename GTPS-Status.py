#Made by iFanpS
#Inspired from KIPAS#1823
from inspect import isroutine
from sys import platform
import discord
import time
from datetime import datetime
import os, glob
import psutil
from discord import client
from discord.ext import commands

def install_discord():
    os.system('python3 -m pip install -U discord.py')

prefix = "c."
bot = commands.Bot(command_prefix=prefix)

client = discord.Client()
    
@bot.event
async def on_ready():
    print(f"{Client.user} is on")
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(f"My prefix is [{prefix}]"))

@bot.command()
async def status(ctx):
    player = open('online.txt').readlines()
    listworld = len(os.listdir('worlds'))
    time = datetime.now()
    clock = time.strftime(' %H:%M %p')
    embed1 = discord.Embed(color=0x00ff00, title="STATUS SERVER")
    for proc in psutil.process_iter():
        if 'enet' in proc.name():
            embed1.add_field(name="Server Status:", value="UP")
            break;
        else:
            if 'enet' not in proc.name():
                embed1.add_field(name="Server Status:", value="DOWN")
                break;
    embed1.add_field(name="Player online:", value=player[0])
    embed1.add_field(name="Wolrd created:", value=listworld)
    players =  os.listdir('your players online path folder')
    adk = ""
    for x in players:
        adk += x + ",";
    embed1.add_field(name="Player online name:\n", value=adk)
    embed1.set_footer(text="Last update today" + clock)
    msgstatus = await ctx.send(embed=embed1)
    while True:
            player = open('online.txt').readlines()
            listworld = len(os.listdir('worlds'))
            time = datetime.now()
            clock = time.strftime(' %H:%M %p')
            embed2 = discord.Embed(color=0x00ff00, title="STATUS SERVER")
            for proc in psutil.process_iter():
                if 'enet' in proc.name():
                    embed2.add_field(name="Server Status:", value="UP")
                    break;
                else: 
                    if 'enet' not in proc.name():
                        embed2.add_field(name="Server Status:", value="DOWN")
                        break;
            embed2.add_field(name="Player online:\n", value=player[0])
            embed2.add_field(name="World created:\n", value=listworld)
            players =  os.listdir('players')
            adk = ""
            for x in players:
                adk += x + ",";
            embed2.add_field(name="Player online name:\n", value=adk)
            embed2.set_footer(text="Last update today " + clock)
            await msgstatus.edit(embed=embed2)

bot.run('YOUR-TOKEN')
