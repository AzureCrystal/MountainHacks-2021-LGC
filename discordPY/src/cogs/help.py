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

        helpText = "```\n"
        # addbook
        helpText += "/addbook <Title>\n"
        helpText += "\tEnter the title of the book you would like to add.\n"
        helpText += "\n"
        # availability
        helpText += "/availability <ISBN>\n"
        helpText += "\tEnter the ISBN of the book you would like to check availability for.\n"
        helpText += "\n"
        # delbook
        helpText += "/delbook <Title>\n"
        helpText += "\tDelete books from your list by number as given by the /printbook function.\n"
        helpText += "\t<Title> is case sensetive!\n"
        helpText += "\n"
        # printbook
        helpText += "/printbook\n"
        helpText += "\tDisplays all the books in your list.\n"
        helpText += "\n"
        # preview
        helpText += "/preview <Title>\n"
        helpText += "\tEnter the title of the book you would like to preview.\n"
        helpText += "\n"
        # search
        helpText += "/search <Type> <\"Search term\"> <#ofResults>\n"
        helpText += "\tType:\n"
        helpText += "\t\tOne of: title, author, subject\n"
        helpText += "\tSearch term:\n"
        helpText += "\t\tThis is the term you would like to search for.\n"
        helpText += "\t#ofResults:\n"
        helpText += "\t\t(Optional: Default 1) Enter the number of results you would like to receive.\n"
        helpText += "\n"
        # suggest
        helpText += "/suggest <Search terms>\n"
        helpText += "\tThis command recommends a random book based on your search.\n"
        helpText += "\n"
        helpText += "```\n"
        await ctx.send(helpText)

    
def setup(bot):
    bot.add_cog(HelpCommand(bot))