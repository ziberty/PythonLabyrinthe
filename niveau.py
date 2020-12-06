from labyrinthe.labyrinthe import Labyrinthe
from joueur import Joueur

"""importation objets"""
from objets.potion import Potion
from objets.lunettes import Lunettes
from objets.trappe import Trappe
from objets.piece import Piece
from objets.bouclier import Bouclier
from objets.lampe import Lampe
from objets.sacCouchage import SacCouchage
from objets.coussinPetteur import CoussinPetteur
"""importation personnages"""
from objets.potion import Potion
from personnes.perroquet import Perroquet
from personnes.clown import Clown
from personnes.chatpardeur import Chatpardeur
from personnes.gardienclef import Gardienclef
from personnes.marchand import Marchand
from personnes.minotaure import Minotaure

import random

class Niveau:
    def __init__(self, nomNiveau, 
                    nbSortie, nbPotions, nbLunettes, nbPieces, nbBouclier, nbLampe, nbSacCouchage, nbCoussinPetteur, 
                    nbPerroquets, nbClown, nbChatpardeur, nbGardienclef, nbMarchand, nbMinotaure,
                    joueur, labyrinthe):

        self.nomNiveau = nomNiveau

        self.nbSortie = nbSortie
        self.nbPotions = nbPotions
        self.nbLunettes = nbLunettes
        self.nbPieces = nbPieces
        self.nbBouclier = nbBouclier
        self.nbLampe = nbLampe
        self.nbSacCouchage = nbSacCouchage
        self.nbCoussinPetteur = nbCoussinPetteur

        self.nbPerroquets = nbPerroquets
        self.nbClown = nbClown
        self.nbChatpardeur = nbChatpardeur
        self.nbGardienclef = nbGardienclef
        self.nbMarchand = nbMarchand
        self.nbMinotaure = nbMinotaure

        self.joueur = joueur
        self.labyrinthe = labyrinthe

class Niveau1(Niveau):

    def __init__(self):
        Niveau.__init__(self, "niveau 1", 1, 45, 5, 30, 1, 1, 1, 1, 5, 10, 5, 1, 5, 0, Joueur("X", 100), Labyrinthe(10,10))

    def game1(self):
        # Création perso
        self.labyrinthe.deposerJoueurAleatoirement(self.joueur)

        """Génération des objets"""
        # Ajouter des sorties
        for i in range(self.nbSortie):
           sortie = Trappe()
           self.labyrinthe.deposerSortieAleatoirement(sortie)
        #Ajouter des potions 
        for i in range(self.nbPotions):
            potion = Potion(random.choice([10,5]))
            self.labyrinthe.deposerObjetAleatoirement(potion) 
        # Ajouter des lunettes
        for i in range(self.nbLunettes):
            lunettes = Lunettes()
            self.labyrinthe.deposerObjetAleatoirement(lunettes)
        # Ajouter des pieces
        for i in range(self.nbPieces):
            piece = Piece()
            self.labyrinthe.deposerObjetAleatoirement(piece)
        # Ajouter des boucliers
        for i in range(self.nbBouclier):
            bouclier = Bouclier()
            self.labyrinthe.deposerObjetAleatoirement(bouclier)
        # Ajouter des lampes
        for i in range(self.nbLampe):
            lampe = Lampe()
            self.labyrinthe.deposerObjetAleatoirement(lampe)
        # Ajouter des sacs de couchage
        for i in range(self.nbSacCouchage):
            sacCouchage = SacCouchage()
            self.labyrinthe.deposerObjetAleatoirement(sacCouchage)
        # Ajouter des coussins petteurs
        for i in range(self.nbCoussinPetteur):
            coussinPetteur = CoussinPetteur()
            self.labyrinthe.deposerObjetAleatoirement(coussinPetteur)

        """Génération des personnages"""
        # Ajouter des perroquets
        for i in range(self.nbPerroquets):
            self.labyrinthe.deposerPersonneAleatoirement(Perroquet(random.choice(['vert','bleu','rouge','orange','jaune','rose','violet'])))
        #Ajouter des clowns
        for i in range(self.nbClown):
            self.labyrinthe.deposerPersonneAleatoirement(Clown(random.choice(["gentil", "méchant"])))
        #Ajout des chat-pardeurs
        for i in range(self.nbChatpardeur):
            self.labyrinthe.deposerPersonneAleatoirement(Chatpardeur(random.choice(["discret", "sinistre", "lugubre", "terrifiant", "petit"])))
        #Ajout des gardiens de la clef
        for i in range(self.nbGardienclef):
            self.labyrinthe.deposerPersonneAleatoirement(Gardienclef("Passe Muraille"))
            self.labyrinthe.deposerPersonneAleatoirement(Gardienclef("Passe Partout"))
            self.labyrinthe.deposerPersonneAleatoirement(Gardienclef("Père Fouras"))
        #Ajout des marchands
        for i in range(self.nbMarchand):
            self.labyrinthe.deposerPersonneAleatoirement(Marchand(random.randint(15, 20)))

    def getJoueur(self):
        return self.joueur

    def getLabyrinthe(self):
        return self.labyrinthe

class Niveau2(Niveau):

    def __init__(self):
        Niveau.__init__(self, "niveau 2", 1, 75, 10, 60, 1, 1, 1, 1, 10, 25, 15, 1, 10, 3, Joueur("X", 69), Labyrinthe(20,10))

    def game2(self):
        self.labyrinthe.deposerJoueurAleatoirement(self.joueur)

        """Génération des objets"""
        # Ajouter des sorties
        for i in range(self.nbSortie):
           sortie = Trappe()
           self.labyrinthe.deposerSortieAleatoirement(sortie)
        #Ajouter des potions 
        for i in range(self.nbPotions):
            potion = Potion(random.choice([10,5]))
            self.labyrinthe.deposerObjetAleatoirement(potion) 
        # Ajouter des lunettes
        for i in range(self.nbLunettes):
            lunettes = Lunettes()
            self.labyrinthe.deposerObjetAleatoirement(lunettes)
        # Ajouter des pieces
        for i in range(self.nbPieces):
            piece = Piece()
            self.labyrinthe.deposerObjetAleatoirement(piece)
        # Ajouter des boucliers
        for i in range(self.nbBouclier):
            bouclier = Bouclier()
            self.labyrinthe.deposerObjetAleatoirement(bouclier)
        # Ajouter des lampes
        for i in range(self.nbLampe):
            lampe = Lampe()
            self.labyrinthe.deposerObjetAleatoirement(lampe)
        # Ajouter des sacs de couchage
        for i in range(self.nbSacCouchage):
            sacCouchage = SacCouchage()
            self.labyrinthe.deposerObjetAleatoirement(sacCouchage)
        # Ajouter des coussins petteurs
        for i in range(self.nbCoussinPetteur):
            coussinPetteur = CoussinPetteur()
            self.labyrinthe.deposerObjetAleatoirement(coussinPetteur)

        """Génération des personnages"""
        # Ajouter des perroquets
        for i in range(self.nbPerroquets):
            self.labyrinthe.deposerPersonneAleatoirement(Perroquet(random.choice(['vert','bleu','rouge','orange','jaune','rose','violet'])))
        #Ajouter des clowns
        for i in range(self.nbClown):
            self.labyrinthe.deposerPersonneAleatoirement(Clown(random.choice(["gentil", "méchant"])))
        #Ajout des chat-pardeurs
        for i in range(self.nbChatpardeur):
            self.labyrinthe.deposerPersonneAleatoirement(Chatpardeur(random.choice(["discret", "sinistre", "lugubre", "terrifiant", "petit"])))
        #Ajout des gardiens de la clef
        for i in range(self.nbGardienclef):
            self.labyrinthe.deposerPersonneAleatoirement(Gardienclef("Passe Muraille"))
            self.labyrinthe.deposerPersonneAleatoirement(Gardienclef("Passe Partout"))
            self.labyrinthe.deposerPersonneAleatoirement(Gardienclef("Père Fouras"))
        #Ajout des marchands
        for i in range(self.nbMarchand):
            self.labyrinthe.deposerPersonneAleatoirement(Marchand(random.randint(15, 20)))

    def getJoueur(self):
        return self.joueur

    def getLabyrinthe(self):
        return self.labyrinthe


class Niveau3(Niveau):

    def __init__(self):
        Niveau.__init__(self, "niveau 3", 1, 140, 15, 100, 1, 1, 1, 1, 20, 35, 25, 1, 15, 5, Joueur("X", 55), Labyrinthe(20,20))

    def game3(self):
        self.labyrinthe.deposerJoueurAleatoirement(self.joueur)
        
        """Génération des objets"""
        # Ajouter des sorties
        for i in range(self.nbSortie):
           sortie = Trappe()
           self.labyrinthe.deposerSortieAleatoirement(sortie)
        #Ajouter des potions 
        for i in range(self.nbPotions):
            potion = Potion(random.choice([10,10,15]))
            self.labyrinthe.deposerObjetAleatoirement(potion)
        # Ajouter des lunettes
        for i in range(self.nbLunettes):
            lunettes = Lunettes()
            self.labyrinthe.deposerObjetAleatoirement(lunettes)
        # Ajouter des pieces
        for i in range(self.nbPieces):
            piece = Piece()
            self.labyrinthe.deposerObjetAleatoirement(piece)
        # Ajouter des boucliers
        for i in range(self.nbBouclier):
            bouclier = Bouclier()
            self.labyrinthe.deposerObjetAleatoirement(bouclier)
        # Ajouter des lampes
        for i in range(self.nbLampe):
            lampe = Lampe()
            self.labyrinthe.deposerObjetAleatoirement(lampe)
        # Ajouter des sacs de couchage
        for i in range(self.nbSacCouchage):
            sacCouchage = SacCouchage()
            self.labyrinthe.deposerObjetAleatoirement(sacCouchage)
        # Ajouter des coussins petteurs
        for i in range(self.nbCoussinPetteur):
            coussinPetteur = CoussinPetteur()
            self.labyrinthe.deposerObjetAleatoirement(coussinPetteur)

        """Génération des personnages"""
        # Ajouter des perroquets
        for i in range(self.nbPerroquets):
            self.labyrinthe.deposerPersonneAleatoirement(Perroquet(random.choice(['vert','bleu','rouge','orange','jaune','rose','violet'])))
        #Ajouter des clowns
        for i in range(self.nbClown):
            self.labyrinthe.deposerPersonneAleatoirement(Clown(random.choice(["gentil", "méchant"])))
        #Ajout des chat-pardeurs
        for i in range(self.nbChatpardeur):
            self.labyrinthe.deposerPersonneAleatoirement(Chatpardeur(random.choice(["discret", "sinistre", "lugubre", "terrifiant", "petit"])))
        #Ajout des gardiens de la clef
        for i in range(self.nbGardienclef):
            self.labyrinthe.deposerPersonneAleatoirement(Gardienclef("Passe Muraille"))
            self.labyrinthe.deposerPersonneAleatoirement(Gardienclef("Passe Partout"))
            self.labyrinthe.deposerPersonneAleatoirement(Gardienclef("Père Fouras"))
        #Ajout des minotaures
        for i in range(self.nbMinotaure):
            self.labyrinthe.deposerPersonneAleatoirement(Minotaure(random.choice([10, 12, 14]), random.choice([False, False, False, False, True])))

    def getJoueur(self):
        return self.joueur

    def getLabyrinthe(self):
        return self.labyrinthe

def creerNiveau(nomNiveau):
    if nomNiveau == "niveau 1":
        return Niveau1()
    elif nomNiveau == "niveau 2":
        return Niveau2()
    elif nomNiveau == "niveau 3":
        return Niveau3()
    else:
        raise ValueError()

