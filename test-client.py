
import requests 
import json
  
# api-endpoint 
URL = "http://127.0.0.1:5000/"


# login request
request = requests.post(url = URL + "login")
data = json.loads(request.text)
id = data["id"]
token = data["token"]

print(id, token)

# quotes request
request = requests.post(url = URL + "quotes", data={"id" : id, "token" : token})
print(request.text)


