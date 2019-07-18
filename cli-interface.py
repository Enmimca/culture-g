from game import *

core = Core()
player = Player(core)

#game loop
for i in range (20):
    
    print("\nCitation: « {} »\nSuggestions: {}".format( player.quote_to_find.content, player.authors_suggestion ))
    answer = input("Rentre le numéro correspondant au bon auteur: ")
    if (player.check_answer(int(answer))):
        print("Bonne réponse")
    else:
        print("Mauvaise réponse")
    input("\nVoici la citation et ses informations complémentaires : {0}, pour passer à la question suivante appuie sur entrer !\n\n".format(player.quote_to_find))
    player.update()

#affiche le message final
print("Ton score est de:" + player.score)