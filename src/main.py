import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound

client = discord.Bot(command_prefix = '/')
client.remove_command("help")

@client.event
async def on_ready():
    print("Bot is ready.")

@client.command()
async def help(ctx, *args):
    argCount = len(args)

client.run('ODEwMjIzMjE1NjQwNTc2MDEw.YCghKw.R3qcwbgsQVSBhPwX2nl8F4tk73Y')