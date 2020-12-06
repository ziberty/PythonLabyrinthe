from joueur import Joueur
from personnage import Personnage
import random


class Minotaure(Personnage):
    """ Cette classe représente un minotaure qui charge le joueur quand il tombe sur sa case. """

    def __init__(self, nbEnergieCoup, estCritique):
        """ Constructeur. Paramètres :
        - nbEnergieCoup : Nombre de dégats (int)
        - estCritique : Si le coup est critique, le nombre de dégats est multiplié par 2 (bool)
        """
        self._nbEnergieCoup = nbEnergieCoup
        self._estCritique = estCritique

    def description(self):
        """ Renvoie la description du clown."""
        return "Il s'agit d'un minotaure."

    def rencontrer(self, joueur):
        nbDegat = self._nbEnergieCoup
        nbIteration = int(nbDegat/2)
        print("Minotaure: CHAAAAAAAARGE!")
        if self._estCritique:
            nbIteration += nbIteration
            nbCoupCrit = nbDegat * 2
            print("Coup critique! (x2 dégats)")
            print("Le minotaure vous a chargé et vous a infligé " + str(nbCoupCrit) + " d'énergie.")
        else:
            print("Le minotaure vous a chargé et vous a infligé " + str(nbDegat) + " d'énergie.")
        for i in range(nbIteration):
            joueur.perdreEnergie()
        input()

    def parler(self, joueur):
        print("Minotaure: Pousse toi de là, minus!!")

    def supprimer(self, joueur):
        print("Le minotaure s'en va en vous poussant brusquement.")
        joueur.getCaseCourante().getPersonnages().clear()