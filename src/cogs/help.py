import discord
from discord.ext import commands

class HelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        await ctx.send('What do you need <@{}>?'.format(ctx.message.author.id))
        id = ctx.message.author.id
        name = ctx.message.author.name
        print(name, id, "has used the help command.")

    
def setup(bot):
    bot.add_cog(HelpCommand(bot))