import discord
import requests
from discord.ext import commands

class Search(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    async def search(self, ctx, *args):
        parameters = ["title", "author", "subject"]
        bookListLength = 1
        descWordCap = 1000
        if args[0] in parameters:
            response = requests.get("https://www.googleapis.com/books/v1/volumes?q=" + args[0] + ":" + '\"' + str(args[1]) + '\"')
            if (int(len(args)) < 3):
                if args[2].isnumeric():
                    bookListLength = (args[2] + 1)
            for booksIterator in range(bookListLength):
                if "items" in response.json():
                    googleBooksList = response.json()['items']
                    result = "```\n"
                    if "title" in googleBooksList[booksIterator]["volumeInfo"]:
                        result += ("Title: " + str(googleBooksList[booksIterator]["volumeInfo"]["title"]) + "\n")
                    if "subtitle" in googleBooksList[booksIterator]["volumeInfo"]: 
                        result += ("Subtitle: " + str(googleBooksList[booksIterator]["volumeInfo"]["subtitle"]) + "\n")
                    if "authors" in googleBooksList[booksIterator]["volumeInfo"]: 
                        result += "Authors: "
                        for i in range(len(googleBooksList[booksIterator]["volumeInfo"]["authors"])):
                            result += (str(googleBooksList[booksIterator]["volumeInfo"]["authors"][i]) + ", " )
                        result += "\n"
                    if "publishedDate" in googleBooksList[booksIterator]["volumeInfo"]: 
                        result += ("Published date: " + googleBooksList[booksIterator]["volumeInfo"]["publishedDate"] + "\n")
                    if "description" in googleBooksList[booksIterator]["volumeInfo"]: 
                        desc = str(googleBooksList[booksIterator]["volumeInfo"]["description"])
                        if len(desc) > descWordCap:
                            desc = desc[:descWordCap] + "..."
                        result += desc
                    result += "\n```"
                    
                    def check(reaction, user):
                        return user == ctx.author and str(reaction.emoji) in ['\N{WHITE HEAVY CHECK MARK}']

                    embedMsg = await ctx.send(result)                
                    await embedMsg.add_reaction('\N{WHITE HEAVY CHECK MARK}')
                    confirmation = await self.bot.wait_for("reaction_add", check=check)
                    if confirmation :    
                        #add the book to the list       
                        print("something")
                else:
                    if booksIterator == 0:
                        await ctx.send("No books found.")
                    else:
                        await ctx.send("No more books found.")
                    break
        else:
            await ctx.send("Invalid parameters. Use: /search <type> <query>")

    @commands.command()
    async def availability(self, ctx, *args):
        response = requests.get("https://www.googleapis.com/books/v1/volumes?q=isbn:" + '\"' + str(args[1]) + '\"')
        if "items" in response.json():
            googleBooksList = response.json()['items']
            result = ""
            result += ("PDF available: " + googleBooksList["pdf"] + "\n")
            result += ("Access info: " + googleBooksList["accessinfo"] + "\n")
            result += ("Sales info: " + googleBooksList["saleInfo"] + "\n")
            await ctx.send(result)
        else:
            await ctx.send("Invalid ISBN given. Use: /availability <ISBN number>")

   

def setup(bot):
    bot.add_cog(Search(bot))