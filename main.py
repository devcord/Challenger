import discord
import json
from cmd import hello
from cmd import __all__

bot_info = json.load(open("bot_info.json", "r"))

client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return

    cmd = msg.content[1:]

    if (msg.content[0] == bot_info["prefix"]):
        if cmd in __all__:
            cmdFun = getattr(globals()[cmd], cmd)
            await cmdFun(msg)
        else:
            # Send error embed
            embedVar = discord.Embed(title="Sorry but..", description="This command doesn't exist", color=0xeb3d34)
            await msg.channel.send(embed=embedVar)
            return

client.run(bot_info['token'])