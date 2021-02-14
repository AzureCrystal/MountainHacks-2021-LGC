# MountainHacks-2021-LGC

The Book of Tomorrow 

A Discord bot that searches a library of books and gives suggestions based on search parameters

The Discord bot can also store the User's favourite books into a database help in REST API made with Springboot(Tomcat)

# Functions included:

Help Command (/help)
 - lists out the list of commands for the bot 
 
Suggestion Command (/suggest)
 - gives a random book based on genre selected 
 
Search Command (/search)
 - gives a book title and description when given (title or subject or author) 
 
Add Book to List (/addbook)
 - adds a book towards the user's list

Delete Book from List (/delbook)
 - deletes a book from the user's list

Print Book List (/printbook)
 - prints the user's book list
 
Notes:
 - Each user will have it's own indiviual library booklist (NOT IMPLEMENTED)
 
How to Run:
 - Create a file called .env in the src folder
 - Get a Discord Bot API and use your API key in .env using:
 - DISCORD_TOKEN="<YOUR_TOKEN>"
 - To run the bot, run main.py
 
