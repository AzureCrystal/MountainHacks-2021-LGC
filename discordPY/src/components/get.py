import requests

def getUserData(id):
    return(requests.get("http://localhost:8080/api/userList/getBook/" + str(id)).json())