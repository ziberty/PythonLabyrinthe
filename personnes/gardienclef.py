from joueur import Joueur
from personnage import Personnage
from objets.morceauCle import morceauCle
from finDefaite import FinDefaite
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
import random


class Gardienclef(Personnage):
    """ Cette classe représente un gardien des clefs. Il prend la forme de passe partout, passe muraille ou le père
    fouras """

    def __init__(self, nom):
        self._nom = nom


    def description(self):
        """ Renvoie la description du gardien de la clef."""
        return "Le célèbre " + self._nom + " se trouve devant vous."

    def rencontrer(self, joueur):
        """ Rencontre avec un gardien de clef """
        print("Vous rencontrez le mythique " + self._nom + "!! Il détient peut-être un objet rare.")
        input()


    def parler(self, joueur):
        if self._nom == "Passe Muraille" or self._nom == "Passe Partout":
            print(self._nom + ": En m'éloignant du fort je me suis perdu et j'ai atterri ici! Voici ta récompense pour m'avoir trouvé!")
            print("Vous obtenez un morceau de clef")
            morceauCle.donner(self, joueur)
        else:
            print(self._nom + ": Bonjour à toi! Les deux nains se sont perdus et je suis à leur recherche! En attendant, je vais te poser une énigme. Si ta réponse est correcte, tu auras une récompense.")
            input("===ÉNIGME===")
            print("\nJ'ai une carapace pour me protéger.\n Je vie sur terre ou dans l'eau.\n Qui suis-je?")
            reponse = input("Votre réponse: ")

            if reponse.lower() == "tortue" or reponse.lower() == "la tortue" or reponse.lower() == "une tortue":
                print(self._nom + ": Bravo, c'est la bonne réponse. Voici ta récompense:")
                morceauCle.donner(self, joueur)
                print("Vous obtenez un morceau de clef")
            else:
                cls()
                print(self._nom + ": C'est faux! Tiens, prends ça!! *BAM*")
                print("Le Père Fouras vous frappe et vous emmène en prison,")
                FinDefaite.finDuJeu(joueur)
                
    
    def supprimer(self, joueur):
        print("*POUF* le gardien des clés a disparu!")
        joueur.getCaseCourante().getPersonnages().clear()



