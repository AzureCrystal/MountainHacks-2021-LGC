import requests

def getUserData(id):
    return(requests.get("http://localhost:8080/api/userList/" + str(id)).json())
