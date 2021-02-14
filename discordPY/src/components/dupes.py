import os
import json

directory = os.path.dirname(os.path.abspath(__file__))
bookPath = os.path.join(directory, '../assets/books.json')

def checkDupes(check):
    with open(bookPath) as json_file :
        books = json.load(json_file)
    for element in books["books"]:
        if (element["name"].lower() == str(check).lower()):
            return False
    return True

