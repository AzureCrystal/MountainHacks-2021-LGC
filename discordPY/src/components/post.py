import requests

def postFunc(bookName, id):
    url = 'http://localhost:8080/api/userList/addBook/' + str(id)
    print()
    myobj = {'name' : bookName}

    x = requests.post(url, json = myobj)
