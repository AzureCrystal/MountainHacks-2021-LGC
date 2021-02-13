import discord
import json
from help import HelpCommand
from discord.ext import commands
from discord.ext.commands import CommandNotFound

client = commands.Bot(command_prefix = '/')

x = {
  "books": [
    {"name": "BMW 230"},
    {"name": "Ford Edge"}
  ]
}

@client.event
async def on_ready():
    print("Bot is ready.")

help


client.run('ODEwMjIzMjE1NjQwNTc2MDEw.YCghKw.R3qcwbgsQVSBhPwX2nl8F4tk73Y')