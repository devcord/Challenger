import discord
import json
from cmd import hello, __all__

# Load secrets for the bot, should include the token and prefix
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
    args = msg.content.split()
    # Remove the "!commandName" from the array
    args.pop(0)

    if (msg.content[0] == bot_info["prefix"]):
        # If command exists, run it
        if cmd in __all__:
            cmdFun = getattr(globals()[cmd], cmd)
            await cmdFun(msg, args)
        else:
            # Send error embed
            embedVar = discord.Embed(title="Sorry but..", description="This command doesn't exist", color=0xeb3d34)
            await msg.channel.send(embed=embedVar)
            return

client.run(bot_info['token'])