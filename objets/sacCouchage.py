from objet import ObjetRamassable

class SacCouchage(ObjetRamassable):
    """ Représente un sac de couchage permettant de se reposer quelques heures """

    def utiliser(self, joueur):
        joueur.gagnerEnergie(50)

    def description(self):
        return "Sac de couchage"