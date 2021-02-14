import discord
import json
import os
from discord.ext import commands
from components.dupes import checkDupes

directory = os.path.dirname(os.path.abspath(__file__))
bookPath = os.path.join(directory, '../assets/books.json')

class BookCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def printbook(self, ctx):
        usrId = ctx.message.author.id
        jsonBookList = getUserData(usrId)
        bookList = json.load(jsonBookList)
        if len(bookList["books"]) != 0:
            strName = "```\n"
            for i in range(len(bookList["books"])):
                listNum = i + 1
                strName += str(listNum) + ". " + bookList["books"][i]["name"] + "\n"
            strName += "\n```"
            await ctx.send(strName)
        else:
            await ctx.send("Book list is empty!")

    @commands.command()
    async def delbook(self, ctx, *args):
        usrId = ctx.message.author.id
        jsonBookList = getUserData(usrId)
        bookList = json.load(jsonBookList)
        if len(args) != 0:
            if args[0].isnumeric():
                if len(bookList["books"]) != 0:
                    index = int(args[0]) - 1
                    if (index + 1) > 0 and (index + 1) <= len(bookList["books"]):
                        data = getUserData(usrId)
                        data["books"].pop(index)
                        await ctx.send("Book Removed!")
                        with open(bookPath, 'w') as f:
                            json.dump(data, f, indent = 4)
                    else:
                        await ctx.send("Parameter out of bounds.")
                else:
                    await ctx.send("List is empty")
            else:
                await ctx.send("Invalid parameter.")
        else:
            await ctx.send("Missing parameter. Use: /delbook <Number>")

    @commands.command()
    async def addbook(self, ctx, *args):
        usrId = ctx.message.author.id
        if len(args) != 0:
            books_loaded = getUserData(usrId)
            books_loaded["books"].append({"name":' '.join(str(elem) for elem in args)})
            if(not checkDupes(' '.join(str(elem) for elem in args)), usrId):
                await ctx.send("This book is already in your library!")
            else:
                with open(bookPath,'w') as json_dumped :
                    json.dump(books_loaded,json_dumped,indent = 4,sort_keys = True)

                await ctx.send("Book added!")
        else:
            await ctx.send("Missing parameter. Use: /addbook <Title>")


def setup(bot):
    bot.add_cog(BookCommand(bot))