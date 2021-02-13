import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound

client = commands.Bot(command_prefix = '/')
client.remove_command("help")

class HelpCommand:
    
    def __init__(self, bot):
        self.bot = bot

    @client.command()
    async def help(self, *args):
        self.argCount = len(args)
        await self.send("hi")

    def send(self, message):
        self.bot.send(message)

    def setup(self, bot):
        bot.help(HelpCommand(bot))

