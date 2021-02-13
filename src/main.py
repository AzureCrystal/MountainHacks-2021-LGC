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

@client.event
async def on_ready():
    print("Bot is ready.")

@client.command()
async def help(ctx, *args):
    argCount = len(args)
    await ctx.send("Nothing here")

client.run('ODEwMjIzMjE1NjQwNTc2MDEw.YCghKw.R3qcwbgsQVSBhPwX2nl8F4tk73Y')