import discord
import json
import os
import sys
sys.path.insert(0, '../components/')
from discord.ext import commands
from components.dupes import checkDupes
from components.post import postFunc, delFunc
from components.get import getUserData
#from discordPY.src.components import checkDupes, postFunc, getUserData

directory = os.path.dirname(os.path.abspath(__file__))
bookPath = os.path.join(directory, '../assets/books.json')

class BookCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def printbook(self, ctx):
        usrId = ctx.message.author.id
        bookList = getUserData(usrId)
        if len(bookList) != 0:
            strName = "```\n"
            for i in range(len(bookList)):
                listNum = i + 1
                strName += str(listNum) + ". " + bookList[i]["name"] + "\n"
            strName += "\n```"
            await ctx.send(strName)
        else:
            await ctx.send("Book list is empty!")

    @commands.command()
    async def delbook(self, ctx, *args):
        usrId = ctx.message.author.id
        bookList = getUserData(usrId)
        if len(args) != 0:
            bookName = ' '.join(str(elem) for elem in args)
            if len(bookList) != 0:
                data = getUserData(usrId)
                delFunc(bookName, usrId)
                await ctx.send("Book Removed!")
            else:
                await ctx.send("List is empty")
        else:
            await ctx.send("Missing parameter. Use: /delbook <Book Name>")

    @commands.command()
    async def addbook(self, ctx, *args):
        usrId = ctx.message.author.id
        if len(args) != 0:
            tmpStr = ' '.join(str(elem) for elem in args)
            if (not checkDupes(tmpStr, usrId)):
                await ctx.send("This book is already in your library!")
            else:
                postFunc(tmpStr, usrId)
                await ctx.send("Book added!")
        else:
            await ctx.send("Missing parameter. Use: /addbook <Title>")


def setup(bot):
    bot.add_cog(BookCommand(bot))