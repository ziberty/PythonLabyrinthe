from objets.potion import Potion
from personnage import Personnage

import random

class Marchand(Personnage):
    """ Cette classe représente un marchant qui vend une potion aléatoire au joueur, en échange de pièces d'or. """

    def __init__(self, nbEnergiePotion):
        """ Constructeur. Paramètres :
        - nbEnergiePotion : la quantité d'énergie que contient la potion à vendre (entier)
        """
        self._nbEnergiePotion = nbEnergiePotion

    def description(self):
        """ Renvoie la description du marchand."""
        return "Un marchand clandestin"

    def rencontrer(self, joueur):
        """ Affiche un message de rencontre du marchand.
        TODO: on pourrait avoir un message de salutation plus varié en le tirant aléatoirement ici, ou dans le constructeur pour qu'un même perroquet salue toujours de la même façon.
        """
        print("Un marchand clandestin se cache dans l'ombre. Il semble vouloir vendre quelque chose...")
        input()

    def parler(self, joueur):
        """ Le marchand propose de vendre une de ses potions au joueur. """
        potion = Potion(self._nbEnergiePotion)
        nbPieces = joueur.getPieces()
        print("Marchand clandestin: Pssst! Je vend une " + potion.description() + " pour 5 pièces d'or.....")
        reponse = input("Acheter la potion? [O/N]")

        if reponse.lower() == "o":
            if nbPieces < 7:
                print("Pssst! Tu n'as pas assez de pièces.....")
            else:
                joueur.mettreObjetDansLeSac(potion)
                for i in range(7):
                    joueur.depenserPieces()
                print("Marchand clandestin: Merci pour votre achat....")
                print("Vous gagnez: " + potion.description())
        elif reponse.lower() == "n":
            print("Marchand clandestin: Dommage.... Adieu....")
            print("Vous repartez bredouille.")
        else:
            print("Marchand clandestin: Je n'ai pas compris ce que vous venez de me dire.....")
    
    def supprimer(self, joueur):
        print("Le marchand redisparait dans l'ombre!")
        joueur.getCaseCourante().getPersonnages().clear()