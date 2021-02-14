import os
import json
from components.get import getUserData
directory = os.path.dirname(os.path.abspath(__file__))
bookPath = os.path.join(directory, '../assets/books.json')

def checkDupes(check, usrId):
    books = getUserData(usrId)
    for element in books:
        if (element["name"].lower() == str(check).lower()):
            return False
    return True

