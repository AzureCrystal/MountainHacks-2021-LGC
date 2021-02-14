import discord
import json
import os

from discord.ext import commands
from discord.ext.commands import CommandNotFound
from dotenv import load_dotenv

load_dotenv()
client = commands.Bot(command_prefix = '/')
client.remove_command("help")

directory = os.path.dirname(os.path.abspath(__file__))

token = os.getenv('DISCORD_TOKEN')

# googleAPIKeyFile = open('googleApiKey.txt', 'r')
# googleAPIKey = googleAPIKeyFile.read()

bookPath = os.path.join(directory, 'books.json')
jsonBookList = open(bookPath)
bookList = {}

extensionList = ['cogs.help', 'cogs.books']


if __name__ == '__main__':
  for extension in extensionList:
    client.load_extension(extension)

@client.event
async def on_ready():
    print("Bot is ready.")
    bookList = json.load(jsonBookList)
    print(bookList)

client.run(token)
