from exceptions import AbstractMethodCallException

class Objet:
    """ Cette interface représente un objet que l'on peut ramasser et que le joueur peut transporter dans son sac"""

    def ramasser(self, joueur):
        """ Cette méthode est appelée lorsque le joueur ramasse un objet.
        En fonction de l'objet, celui-ci peut être ajouté au sac à dos pour utilisation ultérieur, ou utilisé tout de suite.
        Si l'objet ne peut pas être stocké et est utilisé dès qu'il est ramassé, on appelera la méthode self.utiliser(joueur)
        dans cette méthode plutôt que de coder la logique d'utilisation dans la méthode ramasser().
        """
        raise AbstractMethodCallException() # Méthode abstraite

    def utiliser(self, joueur):
        """ Cette méthode est appelée lorsque le joueur utilise un objet. """
        raise AbstractMethodCallException() # Méthode abstraite

    def description(self):
        """ Renvoie une description de l'objet, pour pouvoir l'afficher. """
        raise AbstractMethodCallException() # Méthode abstraite


class ObjetRamassable(Objet):
    """ Cette classe abstraite représente tout objet que l'on peut ramasser. La méthode ramasser implémente le code
    qui permet de mettre l'objet dans le sac du joueur. Il reste à définir la méthode utiliser().
    """

    def ramasser(self, joueur):
        """ Met l'objet dans le sac du joueur. """
        joueur.mettreObjetDansLeSac(self)

    def utiliser(self, joueur):
        raise AbstractMethodCallException() # Méthode abstraite

    def description(self):
        raise AbstractMethodCallException() # Méthode abstraite

