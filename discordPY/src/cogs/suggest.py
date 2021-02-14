import discord
import json
import os
import requests
import random
import sys
sys.path.insert(0, '../components/')
from discord.ext import commands
from components.dupes import checkDupes
from components.post import postFunc
from components.get import getUserData
#from discordPY.src.components import checkDupes, postFunc, getUserData

directory = os.path.dirname(os.path.abspath(__file__))
bookPath = os.path.join(directory, '../books.json')

class Suggest(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def suggest(self, ctx, *args):
        descWordCap = 1000
        usrId = ctx.message.author.id
        if len(args) >= 1: 
            initResp = requests.get("https://www.googleapis.com/books/v1/volumes?q=subject:" + '\"' + '+'.join(str(elem) for elem in args) + '\"')
            if initResp.json()["totalItems"] != 0:
                if initResp.json()["totalItems"] >= 40:
                    maxVal = 40
                else:
                    maxVal = initResp.json()["totalItems"]
                response = requests.get("https://www.googleapis.com/books/v1/volumes?q=subject:" + '\"' + '+'.join(str(elem) for elem in args) + '\"' + "&maxResults=" + str(maxVal))
                random.seed()
                print(maxVal)
                index = random.randint(0,int(maxVal)-1)
                print(index)
                googleBooksList = response.json()['items']
                result = "```\n"
                if "imageLinks" in googleBooksList[index]["volumeInfo"]:
                    if "thumbnail" in googleBooksList[index]["volumeInfo"]["imageLinks"]:
                        await ctx.send(str(googleBooksList[index]["volumeInfo"]["imageLinks"]["thumbnail"]))
                    elif "smallThumbnail" in googleBooksList[index]["volumeInfo"]["imageLinks"]:
                        await ctx.send(str(googleBooksList[index]["volumeInfo"]["imageLinks"]["smallThumbnail"]))
                if "title" in googleBooksList[index]["volumeInfo"]:
                    result += ("Title: " + str(googleBooksList[index]["volumeInfo"]["title"]) + "\n")
                    bookName = str(googleBooksList[index]["volumeInfo"]["title"])
                if "subtitle" in googleBooksList[index]["volumeInfo"]: 
                    result += ("Subtitle: " + str(googleBooksList[index]["volumeInfo"]["subtitle"]) + "\n")
                if "authors" in googleBooksList[index]["volumeInfo"]: 
                    result += "Authors: "
                    for i in range(len(googleBooksList[index]["volumeInfo"]["authors"])):
                        result += (str(googleBooksList[index]["volumeInfo"]["authors"][i]) + ", " )
                    result += "\n"
                if "publishedDate" in googleBooksList[index]["volumeInfo"]: 
                    result += ("Published date: " + googleBooksList[index]["volumeInfo"]["publishedDate"] + "\n")
                if "description" in googleBooksList[index]["volumeInfo"]: 
                    desc = str(googleBooksList[index]["volumeInfo"]["description"])
                    if len(desc) > descWordCap:
                        desc = desc[:descWordCap] + "..."
                    result += desc
                result += "\n```"

                def check(reaction, user):
                    return user == ctx.author and str(reaction.emoji) in ["✅", "❌"]

                embedMsg = await ctx.send(result)                
                await embedMsg.add_reaction('✅')
                await embedMsg.add_reaction('❌')
                reaction, user = await self.bot.wait_for("reaction_add", check=check)

                if str(reaction.emoji) == "✅":
                    await embedMsg.remove_reaction(reaction, user)
                    if checkDupes(bookName, usrId):
                        postFunc(bookName, usrId)
                        await ctx.send("Book Added!")
                    else:
                        await ctx.send("This book is already in your library!")
                elif str(reaction.emoji) == "❌":
                    await embedMsg.remove_reaction(reaction, user)
            else:
                await ctx.send("No books found.")
        else:
            await ctx.send("Missing parameter. Use: !suggest <Search Term>")

def setup(bot):
    bot.add_cog(Suggest(bot))