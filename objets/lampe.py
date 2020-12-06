from objet import ObjetRamassable


class Lampe(ObjetRamassable):
    """ Représente des lunettes qui permettent de voir a travers les murs """

    def utiliser(self, joueur):
        joueur.getLampe()

    def description(self):
        return "Lampe pour voir deux fois plus loin"