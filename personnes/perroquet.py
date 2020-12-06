from personnage import Personnage
import random

class Perroquet(Personnage):
    """ Cette classe représente un Perroquet qui salue le joueur lorsqu'il arrive sur la même case, et qui répète
        bêtement ce qu'on lui dit. Le perroquet a une couleur qu'on lui passe à la création dans le constructeur. """

    def __init__(self, couleur):
        """ Constructeur. Paramètres :
        - couleur : la couleur du perroquet (chaine de caractères)
        """
        self._couleur = couleur

    def description(self):
        """ Renvoie la description du perroquet."""
        return "Un perroquet " + self._couleur

    def rencontrer(self, joueur):
        """ Affiche un message de salutation au joueur."""
        print(random.choice([
            "Un perroquet "+self._couleur+" vous salue bien bas",
            "Un perroquet "+self._couleur+" se pose sur votre épaule "+random.choice(["gauche","droite"])+".",
            "Vous trouvez un petit perroquet "+self._couleur+" au sol."
            ]))
        
        input()

    def parler(self, joueur):
        """ Le perroquet répète ce qu'on lui dit avec son accent de perroquet (en accentuant les voyelles). """
        if self._couleur == "jaune":
            print("Ce perroquet semble différent des autres, il brille!")
            print("Perroquet " + self._couleur + ": Aventuuurier, vooooooiici un petiiiit doooooon")
            numPiece = random.randint(1, 3)
            for i in range(numPiece):
                joueur.addPiece()
            print("Le perroquet vient de vous donner " + str(numPiece) + " pièces d'or!")
            
        else:
            print("Peroquet "+self._couleur+": Saaaluuuut, noble aventuuurier. Quue me veuuuuux-tuuuuu ?")
            entree = input("#>")
            repetition = ""
            for lettre in entree:
                if lettre in ['a','e','i','o','u']:
                    repetition += lettre*random.randint(1,5) # Si c'est une voyelle, on la répète plusieurs fois
                else:
                    repetition += lettre # Si ce n'est pas une voyelle, on ne la répète qu'une fois
            print(repetition)
            
    def supprimer(self, joueur):
        print("*CROoOooC* le perroquet s'envole!")
        joueur.getCaseCourante().getPersonnages().clear()