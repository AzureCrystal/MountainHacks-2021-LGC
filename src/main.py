import discord
import json
from discord.ext import commands
from discord.ext.commands import CommandNotFound

client = commands.Bot(command_prefix = '/')
client.remove_command("help")

tokenFile = open('token.txt', 'r')
token = tokenFile.read()

# googleAPIKeyFile = open('googleApiKey.txt', 'r')
# googleAPIKey = googleAPIKeyFile.read()

jsonBookList = open('books.json')
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
