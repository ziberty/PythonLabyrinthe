from objet import ObjetRamassable


class CoussinPetteur(ObjetRamassable):
    """ Représente un coussin petteur """

    def utiliser(self,joueur):
        print()
        print("PPRRRRRROOOOUUUUTTTT")
        input()

    def description(self):
        return "Ce coussin est très etrange"