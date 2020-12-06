from objet import Objet

class Piece(Objet):
    """ Représente une piece qui permet d'acheter dans la boutique """
    
    def ramasser(self, joueur):
        joueur.addPiece()

    def depenser(self,joueur):
        joueur.depenserPiece()
        
    def description(self):
        return "Vous avez trouvé une piece, peut etre trouverez vous un marchand"