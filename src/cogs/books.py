import discord
import json
from discord.ext import commands

class BookCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def printbook(self, ctx):
        jsonBookList = open("books.json")
        bookList = json.load(jsonBookList)

        await ctx.send(bookList["books"][2])
        print()

    


    
def setup(bot):
    bot.add_cog(BookCommand(bot))