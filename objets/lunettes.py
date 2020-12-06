from objet import ObjetRamassable


class Lunettes(ObjetRamassable):
    """ Représente des lunettes qui permettent de voir a travers les murs """

    def utiliser(self, joueur):
        joueur.lunettes()

    def description(self):
        return "Lunettes pour voir a travers les murs"