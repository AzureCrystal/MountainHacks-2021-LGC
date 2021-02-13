import discord
import json
from discord.ext import commands
from discord.ext.commands import CommandNotFound

client = commands.Bot(command_prefix = '/')
client.remove_command("help")

x = {
  "books": [
    {"name": "BMW 230"},
    {"name": "Ford Edge"}
  ]
}

extensionList = ['cogs.help']

if __name__ == '__main__':
  for extension in extensionList:
    client.load_extension(extension)

@client.event
async def on_ready():
    print("Bot is ready.")

client.run('NzEzMjE1Mzk3MzczMTQ5MjI0.Xsdiig.axcHpLys2eiASOOeb1ADZuwuZq8')