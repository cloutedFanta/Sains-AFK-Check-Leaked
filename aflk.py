import asyncio
import json
import time
import traceback
import random
from os import system
from random import randint
from discord.ext import commands
import re, requests
from colorama import Fore, init
import platform

init()
data = {}

with open('token.json') as f:
    data = json.load(f)
token = data['token']

os = platform.system()

if os == "Windows":
    system("cls")
else:
    system("clear")
    print(chr(27) + "[2J")

print(Fore.RED + """\

            ███████╗ █████╗ ██╗███╗   ██╗     █████╗ ███████╗██╗  ██╗      ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗
            ██╔════╝██╔══██╗██║████╗  ██║    ██╔══██╗██╔════╝██║ ██╔╝     ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝
            ███████╗███████║██║██╔██╗ ██║    ███████║█████╗  █████╔╝█████╗██║     ███████║█████╗  ██║     █████╔╝ 
            ╚════██║██╔══██║██║██║╚██╗██║    ██╔══██║██╔══╝  ██╔═██╗╚════╝██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ 
            ███████║██║  ██║██║██║ ╚████║    ██║  ██║██║     ██║  ██╗     ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗
            ╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝    ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝      ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝
                                                                                                                                                                                    
""" + Fore.RESET)

client = commands.Bot(command_prefix=".", self_bot=True)
ready = False


@client.event
async def on_message(message):
    global ready
    if not ready:
        print(Fore.LIGHTCYAN_EX + 'Bypasing afk' + str(
            len(client.guilds)) + ' Servers 🔫\n' + Fore.RESET)
        print(Fore.LIGHTBLUE_EX + time.strftime("%H:%M:%S ", time.localtime()) + Fore.RESET, end='')
        print("[+] start ur madness")
        ready = True
    if message.author == client.user:
        return

    sain333 = [
        'never afk fat bitch',
        'never afk fat bitch',
        (
            'never afk fat bitch'
            'never afk fat bitch'
        ),
    ]

    if message.content == '6':
        response = random.choice(sain333)
        await message.channel.send(response)

client.run(token, bot=False)




