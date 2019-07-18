import json
import random


class Quote:
    """
    Notre objet Quote est composé de :
    - Le contenu (un texte càd str)
    - Un auteur (le nom de l'auteur càd str)
    - Une origine (titre de l'oeuvre dont elle est extraitre càd str)
    - Année de publication càd int
    """

    def __init__ (self, content, author, origin, date):
        self.content = content
        self.author = author
        self.origin = origin
        self.date = date

    def __str__(self):
        if self.date == -1 and not self.origin:
            return "« {} » par {}".format(self.content, self.author)
        return "« {} » par {} en {}, extrait de {}".format(self.content, self.author, self.date, self.origin)


class Core:
    """
    Notre objet Core gère les données liées au jeu mais qui ne nécessitent
    pas d'être différentes selon les parties.
    Exemple : Lit le fichier data.json pour en extraire toutes les citations
    possibles (quotes) sans les modifier
    """
    
    def __init__(self):
        self.quotes = []
        #lit le fichier data.json et convertit son contenu en objets Quote
        with open('data.json') as json_file:
            for json_quote in json.load(json_file):
                self.quotes.append(Quote(**json_quote))

        #supprime les doublons (un set ne peut pas avoir d'élément en double)
        self.authors = set()
        for quote in self.quotes:
            self.authors.add(quote.author)


class Player:
    """
    Notre objet Player gère les données qui diffèrent en fonction
    d'un joueur ou d'une partie (un joueur ne joue qu'une partie à la fois)
    Exemple : emma = Player(core, 7) va créer un Player contenant une copie des citations
    du Core core avec l'identifiant 7. Quand on mettra à jour sa copie des citations
    (emma.quotes), cela n'impactera pas les citations du core (core.quotes)
    """

    players = []
    available_identifiers = []

    def __init__(self, core):
        self.score = 0
        self.turn = 0
        self.core = core
        self.quotes = core.quotes.copy()

        # on réutilise un identifiant si il est disponible
        if len(Player.available_identifiers) > 0:
            self.id = Player.available_identifiers[0]
            Player.players[self.id] = self
            del Player.available_identifiers[0]
        # sinon on en crée un nouveau
        else:
            Player.players.append(self)
            self.id = len(Player.players)-1

        # définit la citation à trouver pendant le tour, càd self.quote_to_find
        self._draw_the_quote_to_find()
        # définit les suggestions d'auteurs
        self.authors_suggestion = Suggestion(self)

    def __del__(self):
        print("Player with id {} successfully deleted".format(self.id))

    # tire au sort la citation à trouver
    def _draw_the_quote_to_find(self):
        random_index = random.randrange(len(self.quotes))
        self.quote_to_find = self.quotes[random_index]
        del self.quotes[random_index]

    # s'active lorsqu'un tour est terminé
    def update(self):

        # attribue les points
        if (self.valid_answer):
            self.score += 1
        else:
            self.score -= 2

        self.turn += 1
        if self.turn > 20:
            # le joueur est supprimé, on rend l'id disponible pour un autre joueur
            Player.available_identifiers.append(self.id)
            Player.players[self.id] = None
            # on s'assure que l'objet est bien supprimé pour ne pas encombrer la mémoire
            del self
        else:
            # définit la citation à trouver pendant le tour, càd self.quote_to_find
            self._draw_the_quote_to_find()
            # définit les suggestions d'auteurs
            self.authors_suggestion = Suggestion(self)

    def check_answer(self, answer):
        self.valid_answer = self.authors_suggestion.right_author_index == answer-1
        return self.valid_answer


class Suggestion:
    """
    Permet de structurer simplement la suggestion: une liste d'auteurs aléaoire contenant
    l'auteur que le joueur doit trouver
    """

    def __init__(self, player, amount=6):
        #génère une liste d'auteurs aléatoire contenant celui que le joueur doit trouver
        suggestions = {player.quote_to_find.author}
        while len(suggestions) < amount:
            fake_author = random.choice(list(player.quotes)).author
            suggestions.add(fake_author)

        self.authors = list(suggestions)
        random.shuffle(self.authors)

        self.right_author_index = self.authors.index(player.quote_to_find.author)

    def __str__(self):
        designed_authors = ""
        for i in range (len(self.authors)):
            designed_authors += "\n{} - {}".format(str(i+1), self.authors[i])
        return designed_authors