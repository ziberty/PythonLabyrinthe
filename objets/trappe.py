from sortie import Sortie
from finVictoire import FinVictoire
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

class Trappe(Sortie):
    """ Représente une trappe, la sortie du labyrinthe """

    def ouvrir(self, joueur):
        if joueur.getCle() == 1:
            cls()
            FinVictoire.finDuJeu(joueur)
        else:
            print("Cette trappe ressemble à une sortie, il y a surement une clé quelque part") 

    def description(self):
        return "Cette trappe semble etre une sortie. Il y a surement une clé dans ce labyrinthe"