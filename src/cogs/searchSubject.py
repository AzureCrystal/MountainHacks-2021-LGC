import discord
import requests
from discord.ext import commands

class SearchSubject(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def searchSubject(self, ctx, *args):
        response = requests.get("https://www.googleapis.com/books/v1/volumes?q=subject:" + args[0])
        googleBooksList = response.json()['items']
        result = "```\n"
        if "title" in googleBooksList[0]["volumeInfo"]:
            result += (str(googleBooksList[0]["volumeInfo"]["title"]) + "\n")
        if "subtitle" in googleBooksList[0]["volumeInfo"]: 
            result += (str(googleBooksList[0]["volumeInfo"]["subtitle"]) + "\n")
        if "authors" in googleBooksList[0]["volumeInfo"]: 
            result += (str(googleBooksList[0]["volumeInfo"]["authors"]) + "\n")
        if "publishedDate" in googleBooksList[0]["volumeInfo"]: 
            result += (str(googleBooksList[0]["volumeInfo"]["publishedDate"]) + "\n")
        if "description" in googleBooksList[0]["volumeInfo"]: 
            result += str(googleBooksList[0]["volumeInfo"]["description"] )
        result += "\n```"
        await ctx.send(result)
        
        

def setup(bot):
    bot.add_cog(SearchSubject(bot))