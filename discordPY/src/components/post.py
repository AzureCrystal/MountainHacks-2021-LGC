import requests

def postFunc(bookName, id):
    url = 'http://localhost:8080/api/userList/' + str(id)
    myobj = {'name' : bookName}

    x = requests.post(url, json = myobj)

    print(x.text)