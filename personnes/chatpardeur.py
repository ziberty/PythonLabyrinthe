from joueur import Joueur
from personnage import Personnage
import random


class Chatpardeur(Personnage):
    """ Cette classe représente un chat-pardeur qui vole un objet dans le sac du joueur lorsqu'on le rencontre. """

    def __init__(self, adjectif):
        self._adjectif = adjectif


    def description(self):
        """ Renvoie la description du clown."""
        return "Un " + self._adjectif + " chat-pardeur veut voler un objet!"

    def rencontrer(self, joueur):
        """ Le chat-pardeur vole un objet aléatoire au joueur.
        TODO: on pourrait avoir un message de salutation plus varié en le tirant aléatoirement ici, ou dans le constructeur pour qu'un même perroquet salue toujours de la même façon.
        """
        sac = joueur.getSac()
        if (len(sac)) == 0:
            print("Ce " + self._adjectif + " chat-pardeur a essayé de vous voler un objet mais votre sac est vide!")
            print("Chat-pardeur: Miaouuuu je t'aurais la prochaine fois! miaouuuuuu")
            input()
        else:
            numObjet = random.randint(0, len(sac))
            obj = sac[numObjet-1]
            print("Ce " + self._adjectif + " chat-pardeur vient de vous voler un objet: " + obj.description() + ". Mince!")
            sac.remove(obj)
            input()

    def parler(self, joueur):
        print("Vous demandez au chat-pardeur de vous rendre votre objet.")
        print("Chat-pardeur: Hihihi! Je ne te rendrai rien! miaaaaaouuuu")
    
    def supprimer(self, joueur):
        print("*pfff* le chat-pardeur s'enfuit en miaulant")
        joueur.getCaseCourante().getPersonnages().clear()