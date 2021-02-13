import discord
import json

from help import HelpCommand
from discord.ext import commands
from discord.ext.commands import CommandNotFound

client = commands.Bot(command_prefix = '/')
client.remove_command("help")

tokenFile = open('token.txt', 'r')
token = tokenFile.read()

googleAPIKeyFile = open('googleApiKey.txt', 'r')
googleAPIKey = googleAPIKeyFile.read()

jsonBookList = open('books.json')
bookList = {}

@client.event
async def on_ready():
    print("Bot is ready.")
    bookList = json.load(jsonBookList)
    print(bookList)


@client.command()
async def help(ctx, *args):
    ctx.argCount = len(args)
    await ctx.send_message("hi")


client.run(token)