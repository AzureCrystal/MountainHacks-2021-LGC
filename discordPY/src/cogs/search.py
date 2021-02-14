import discord
import requests
import os
import json
from discord.ext import commands
from components.dupes import checkDupes

directory = os.path.dirname(os.path.abspath(__file__))
bookPath = os.path.join(directory, '../assets/books.json')

class Search(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
   
    @commands.command()
    async def search(self, ctx, *args):
        parameters = ["title", "author", "subject"]
        bookListLength = 1
        descWordCap = 1000
        if args[0] in parameters:
            response = requests.get("https://www.googleapis.com/books/v1/volumes?q=" + args[0] + ":" + '\"' + str(args[1]).strip("\"") + '\"' + "&maxResults=40")
            if "items" in response.json():
                if (len(args) == 3):
                    if args[2].isnumeric():
                        bookListLength = int(args[2])
                for booksIterator in range(bookListLength):
                    print(booksIterator)
                    
                    googleBooksList = response.json()['items']
                    result = "```\n"
                    if "imageLinks" in googleBooksList[booksIterator]["volumeInfo"]:
                        if "thumbnail" in googleBooksList[booksIterator]["volumeInfo"]["imageLinks"]:
                            await ctx.send(str(googleBooksList[booksIterator]["volumeInfo"]["imageLinks"]["thumbnail"]))
                        elif "smallThumbnail" in googleBooksList[booksIterator]["volumeInfo"]["imageLinks"]:
                            await ctx.send(str(googleBooksList[booksIterator]["volumeInfo"]["imageLinks"]["smallThumbnail"]))
                    if "title" in googleBooksList[booksIterator]["volumeInfo"]:
                        result += ("Title: " + str(googleBooksList[booksIterator]["volumeInfo"]["title"]) + "\n")
                        bookName = str(googleBooksList[booksIterator]["volumeInfo"]["title"])
                    if "subtitle" in googleBooksList[booksIterator]["volumeInfo"]: 
                        result += ("Subtitle: " + str(googleBooksList[booksIterator]["volumeInfo"]["subtitle"]) + "\n")
                    if "authors" in googleBooksList[booksIterator]["volumeInfo"]: 
                        result += "Authors: "
                        for i in range(len(googleBooksList[booksIterator]["volumeInfo"]["authors"])):
                            result += (str(googleBooksList[booksIterator]["volumeInfo"]["authors"][i]) + ", " )
                        result += "\n"
                    if "industryIdentifiers" in googleBooksList[booksIterator]["volumeInfo"]: 
                        for i in range(len(googleBooksList[booksIterator]["volumeInfo"]["industryIdentifiers"])):
                            result += (str(googleBooksList[booksIterator]["volumeInfo"]["industryIdentifiers"][i]["type"]) + ": " + str(googleBooksList[booksIterator]["volumeInfo"]["industryIdentifiers"][i]["identifier"]) + "\n")
                    if "publishedDate" in googleBooksList[booksIterator]["volumeInfo"]: 
                        result += ("Published date: " + googleBooksList[booksIterator]["volumeInfo"]["publishedDate"] + "\n")
                    if "description" in googleBooksList[booksIterator]["volumeInfo"]: 
                        desc = str(googleBooksList[booksIterator]["volumeInfo"]["description"])
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
                        if checkDupes(bookName):
                            with open(bookPath) as json_file:
                                data = json.load(json_file)
                                listVar = data["books"]
                                tempVar = {"name": bookName}
                                listVar.append(tempVar)
                                await ctx.send("Book Added!")
                            with open(bookPath, 'w') as f:
                                json.dump(data, f, indent = 4)
                        else:
                            await ctx.send("This book is already in your library!")
                    elif str(reaction.emoji) == "❌":
                        await embedMsg.remove_reaction(reaction, user)

            else:
                await ctx.send("No books found.")
        else:
            await ctx.send("Invalid parameters. Use: /search <Type> <\"Search term\"> <#ofResults>")


    @commands.command()
    async def availability(self, ctx, *args):
<<<<<<< HEAD:discordPY/src/cogs/search.py
        response = requests.get("https://www.googleapis.com/books/v1/volumes?q=isbn:" + str(args[0]))
        if "items" in response.json():
            googleBooksList = response.json()['items'][0]
            result = ""
            result += ("PDF available: " + str(googleBooksList["accessInfo"]["pdf"]["isAvailable"]) + "\n")
            result += ("Ebook available: " + str(googleBooksList["saleInfo"]["isEbook"]) + "\n")
            result += ("Saleability: " + str(googleBooksList["saleInfo"]["saleability"]) + "\n")
            result += ("Country: " + str(googleBooksList["saleInfo"]["country"]) + "\n")
            await ctx.send(result)
        else:
            await ctx.send("Invalid ISBN given. Use: /availability <ISBN number>")

    @commands.command()
    async def preview(self, ctx, *args):
        response = requests.get("https://www.googleapis.com/books/v1/volumes?q=isbn:" +  str(args[0]) )
=======
        response = requests.get("https://www.googleapis.com/books/v1/volumes?q=isbn:" + '\"' + str(args[1]) + '\"')
>>>>>>> master:src/cogs/search.py
        if "items" in response.json():
            googleBooksList = response.json()['items'][0]
            result = ""
<<<<<<< HEAD:discordPY/src/cogs/search.py
            result += ("Preview Version: " + googleBooksList["volumeInfo"]["contentVersion"] + "\n")
            result += ("Preview Link: " + googleBooksList["volumeInfo"]["previewLink"] + "\n")
            result += ("Info Link: " + googleBooksList["volumeInfo"]["infoLink"] + "\n")
            result += ("Canonical Volume Link: " + googleBooksList["volumeInfo"]["canonicalVolumeLink"] + "\n")
=======
            result += ("PDF available: " + googleBooksList["pdf"] + "\n")
            result += ("Access info: " + googleBooksList["accessinfo"] + "\n")
            result += ("Sales info: " + googleBooksList["saleInfo"] + "\n")
>>>>>>> master:src/cogs/search.py
            await ctx.send(result)
        else:
            await ctx.send("Invalid ISBN given. Use: /availability <ISBN number>")

   

def setup(bot):
    bot.add_cog(Search(bot))