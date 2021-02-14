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
        helpText += "/search <Type> <\"Search term\"> <#ofResults>\n"
        helpText += "\tType:\n"
        helpText += "\t\tOne of: title, author, subject\n"
        helpText += "\tTerm:\n"
        helpText += "\t\tThis is the term you would like to search for.\n"
        helpText += "\t#ofResults:\n"
        helpText += "\t\t(Optional: Default 1) Enter the number of results you would like to receive.\n"
        helpText += "\n"
        helpText += "/addbook <Title>\n"
        helpText += "\tTitle:\n"
        helpText += "\t\tEnter the title of the book\n"
        helpText += "\t\tyou would like to add.\n"
        helpText += "\n"
        helpText += "/printbook\n"
        helpText += "\tDisplays all the books in your list.\n"
        helpText += "\n"
        helpText += "/delbook <Number>\n"
        helpText += "\tNumber:\n"
        helpText += "\t\tEnter the number of the book you would like to delete.\n"
        helpText += "\n"
        helpText += "```\n"
        await ctx.send(helpText)

    
def setup(bot):
    bot.add_cog(HelpCommand(bot))