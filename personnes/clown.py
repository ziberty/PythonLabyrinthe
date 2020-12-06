from joueur import Joueur
from personnage import Personnage
import random


class Clown(Personnage):
    """ Cette classe représente un clown qui salut le joueur lorsqu'il arrive sur la même case.
        Le clown a un caractère qu'on lui passe à la création dans le constructeur. Si il est méchant
        il nous attaque, si il est gentil il nous raconte une blague quand on lui parle"""

    def __init__(self, caractere):
        """ Constructeur. Paramètres :
        - blague : la blague du clown (chaine de caractères)
        """
        self._caractere = caractere

    def description(self):
        """ Renvoie la description du clown."""
        return "Il s'agit d'un clown " + self._caractere + "."

    def rencontrer(self, joueur):
        """ Affiche un message de salutation au joueur.
        TODO: on pourrait avoir un message de salutation plus varié en le tirant aléatoirement ici, ou dans le constructeur pour qu'un même perroquet salue toujours de la même façon.
        """
        print("Un clown vous dit bonjour. (Mais que fait un clown ici?)")
        input()

    def parler(self, joueur):
        """ Le clown est gentil, il va raconter une blague aléatoirement parmi la liste des blagues suivantes """
        if self._caractere == "gentil":
            numBlague = random.randint(1, 5)
            if numBlague == 1:
                blague = "Clown: Quand deux poissons s'énervent, on peut dire que le thon monte?"
            elif numBlague == 2:
                blague = "Clown: Deux gars discutent. - T'as une banane dans l'oreille. - Quoi? - T'as une banane dans l'oreille! - Quoi?? - T'AS UNE BANANE DANS L'OREILLE!!!!! - Parle plus fort, j'ai une banane dans l'oreille!!!!!"
            elif numBlague == 3:
                blague = "Clown: Pourquoi les Belges marchent-ils sur les tuyaux d'arrosage? Pour avoir de l'eau plate!"
            elif numBlague == 4:
                blague = "Clown: Quelle est la femme la plus rapide du monde? Laurence Ferrari"
            else:
                blague = "Clown: Que dit un oignon quand il se cogne? Ail"
            print(blague)

        else:
            for i in range(3):
                joueur.perdreEnergie()
            print("Clown: HAHAHAHA, je suis un clown MÉCHANT!!!!")
            print("Le clown vous attaque et vous fait perdre de l'énergie.")

    def supprimer(self, joueur):
        print("Le clown s'enfuit en rigolant!")
        joueur.getCaseCourante().getPersonnages().clear()