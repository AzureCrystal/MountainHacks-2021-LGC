import discord
import json
import os

from discord.ext import commands

directory = os.path.dirname(os.path.abspath(__file__))
bookPath = os.path.join(directory, '../books.json')

class BookCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def printbook(self, ctx):
        jsonBookList = open(bookPath)
        bookList = json.load(jsonBookList)
        for i in range(len(bookList["books"])):
            await ctx.send(bookList["books"][i]["name"])
        print()

    


    
def setup(bot):
    bot.add_cog(BookCommand(bot))