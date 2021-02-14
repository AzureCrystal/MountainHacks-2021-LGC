import requests

def getUserData(id):
    return(requests.get("localhost:8080/api/userList/%d", id))