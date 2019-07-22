import requests 
import json

class Connection():

    # api-endpoint 
    URL = "http://127.0.0.1:5000/"

    def __init__(self):
        
        # login request
        request = requests.post(url = Connection.URL + "login")
        data = json.loads(request.text)

        self.id = data["id"]
        self.token = data["token"]
        self.quote_to_find = data["quote_to_find"]
        self.suggestion = data["suggestion"]

    def _set_values(self, token, valid_answer, further_information, quote_to_find, suggestion):
        self.token = token
        self.valid_answer = valid_answer
        self.further_information = further_information
        self.quote_to_find = quote_to_find
        self.suggestion = suggestion

    def send_request(self, author_index):
        # quotes request
        request = requests.post(url = Connection.URL + "quotes", data = {"id" : self.id, "token" : self.token, "author_index" : author_index})
        data = json.loads(request.text)
        self._set_values(**data)


#game loop
for i in range (20):

    connection = Connection()
    
    print("\nCitation: « {} »\nSuggestions: {}".format( connection.quote_to_find, connection.suggestion ))
    author_index = int(input("Rentre le numéro correspondant au bon auteur: "))
    connection.send_request(author_index)

    if (connection.valid_answer):
        print("Bonne réponse")
    else:
        print("Mauvaise réponse")

    input("\nVoici la citation et ses informations complémentaires : {0}, pour passer à la question suivante appuie sur entrer !\n\n".format(connection.further_information))

#affiche le message final
print("Ton score est de:")