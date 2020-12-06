from objet import Objet

class Bouclier(Objet):
    """ Représente d'un bouclier qui diminue par 2 les dégats subits. """

    def ramasser(self, joueur):
        joueur.getBouclier()
        
    def description(self):
        return "Vous avez trouvé un bouclier, vous subirez 2x moins de dégats"