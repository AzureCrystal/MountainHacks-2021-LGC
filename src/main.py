import discord
import json
import os
from discord.ext import commands
from discord.ext.commands import CommandNotFound

client = commands.Bot(command_prefix = '/')
client.remove_command("help")

directory = os.path.dirname(os.path.abspath(__file__))
tokenPath = os.path.join(directory, 'token.txt')

tokenFile = open(tokenPath, 'r')
token = tokenFile.read()

# googleAPIKeyFile = open('googleApiKey.txt', 'r')
# googleAPIKey = googleAPIKeyFile.read()

bookPath = os.path.join(directory, 'books.json')
jsonBookList = open(bookPath)
bookList = {}

extensionList = ['cogs.help']

if __name__ == '__main__':
  for extension in extensionList:
    client.load_extension(extension)

@client.event
async def on_ready():
    print("Bot is ready.")
    bookList = json.load(jsonBookList)
    print(bookList)

client.run(token)
