from objet import Objet

class morceauCle(Objet):
    """ Représente un morceau de clé, il vous en faut 3 pour ouvrir la trappe de sortie du labyrinthe """

    def donner(self, joueur):
        joueur.setNbMorceauCle()
        joueur.setNbCle()
        
    def description(self):
        return "Vous avez trouvé un morceau de clé, trouvez en d'autre.. cela ouvre forcément quelque chose"