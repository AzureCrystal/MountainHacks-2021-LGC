import discord
from discord.ext import commands

client = discord.Client()

@client.event
async def on_ready():
    print("Bot is ready.")

client.run('ODEwMjIzMjE1NjQwNTc2MDEw.YCghKw.R3qcwbgsQVSBhPwX2nl8F4tk73Y')