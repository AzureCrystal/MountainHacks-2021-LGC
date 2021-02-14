import requests

def getUserData(id):
    return(requests.get("https://localhost:8080/api/userList/%d", id))