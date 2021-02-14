import discord
import requests
import os
<<<<<<< HEAD

=======
import json
>>>>>>> 191cc965da8a9db7038de57b52e52e0ab92d9009
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from dotenv import load_dotenv

load_dotenv()
client = commands.Bot(command_prefix = '/')
client.remove_command("help")

<<<<<<< HEAD
directory = os.path.dirname(os.path.abspath(__file__))

=======
>>>>>>> 191cc965da8a9db7038de57b52e52e0ab92d9009
token = os.getenv('DISCORD_TOKEN')

bookList = {}

extensionList = ['cogs.help', 'cogs.search', 'cogs.books']

if __name__ == '__main__':
  for extension in extensionList:
    client.load_extension(extension)

@client.event
async def on_ready():
    print("Bot is ready.")

client.run(token)
