import random
from labyrinthe.case import Case

class Labyrinthe:
    """ La classe Labyrinthe représente un ensemble de cases ajencées entre elles pour former un labyrinthe.
    L'algorithme utilisé pour générer un Labyrinthe aléatoirement est celui de fusion aléatoire de chemin présentés
    sur Wikipedia : https://fr.wikipedia.org/wiki/Mod%C3%A9lisation_math%C3%A9matique_de_labyrinthe.
    Utiliser cette classe pour générer le labyrinthe et le personnaliser en y ajoutant des objets, personnages, et un joueur.
    """

    @staticmethod
    def genererLabyrinthe():
        """ Méthode statique qui permet de générer un Labyrinthe aux dimensions paramétrées du jeu (facile/moyen/difficile par exemple) """
        ## TODO: Mettre en place un système de paramétrage du jeu et l'utiliser ici pour renvoyer un Labyrinthe de la bonne dimension.
        ## Ex.: facile : 10x10, moyen : 20x20, difficile : 20x40
        pass

    def __init__(self,tailleX, tailleY):
        """
        Construit un Labyrinthe de taille déterminée, en générant aléatoirement les chemins.
        :param tailleX: taille horizontale du labyrinthe, en nombre de cases
        :param tailleY: taille verticale du labyrinthe, en nombre de cases.
        """
        # Stockage de la taille du labyrinthe
        self.tailleX = tailleX
        self.tailleY = tailleY

        # Initialisation des cases (toutes fermées par défaut
        self.cases = []
        for y in range(self.tailleY):
            for x in range(self.tailleX):
                self.cases.append(Case())

        # Positionnement des liens entre les cases
        for y in range(self.tailleY):
            for x in range(self.tailleX):
                case = self.getCase(x,y)
                if y > 0:                case.setCaseNord(self.getCase(x,y-1))
                if y < self.tailleY - 1: case.setCaseSud(self.getCase(x, y+1))
                if x > 0:                case.setCaseOuest(self.getCase(x-1,y))
                if x < self.tailleX - 1: case.setCaseEst(self.getCase(x+1,y))

        # Lancement de l'algo pour ouvrir les murs et générer un vrai labyrinthe
        self.ouvrirMurs()


    def getCase(self,x,y) -> Case:
        """ Renvoie la case aux coordonnées X et Y. (0,0) correspond à la case en haut à gauche. On va vers la droite en augmentant X et vers le bas en augmentant Y. """
        return self.cases[y*self.tailleX+x]

    def afficher(self):
        """ Affiche le labyrinthe.
        L'algo est assez simple : on boucle sur les lignes des cases (donc Y) et pour chaque ligne on affiche d'abord la ligne du haut de chaque Case
        (via Case.afficherLigne1() puis la seconde ligne (via Case.afficherLigne2()). La ligne du bas d'une case correspond à la ligne du haut de la
        Case inférieure."""
        
        for y in range(self.tailleY):
            for x in range(self.tailleX):
                self.getCase(x,y).afficherLigne1()
            print("+\n",end="")
            for x in range(self.tailleX):
                self.getCase(x,y).afficherLigne2()
            print("|\n", end="")
        for x in range(self.tailleX):
            print("+---",end="")
        print("|\n",end="")
       

    def deposerJoueurAleatoirement(self,joueur):
        """ Ajoute le joueur passé en paramètre sur une case du labyrinthe choisie aléatoirement. """
        case = random.choice(self.cases)
        case.ajouterJoueur(joueur)
        joueur.setCaseCourante(case)

    def deposerObjetAleatoirement(self, objet):
        """ Dépose l'objet passé en paramètre sur une case du labyrinthe choisie aléatoirement. """
        case = random.choice(self.cases)
        case.ajouterObjet(objet)

    def deposerSortieAleatoirement(self, sortie):
        """Dépose la sortie une case du labyrinthe choisie aléatoirement."""
        case = random.choice(self.cases)
        case.ajouterSortie(sortie)

    def deposerPersonneAleatoirement(self, personne):
        """ Dépose le personnage passé en paramètre sur une case du labyrinthe choisie aléatoirement. """
        case = random.choice(self.cases)
        case.ajouterPersonnage(personne)



    def ouvrirMurs(self):
        """ Implémente l'algorithme de génération du labyrinthe, en partant d'un labyrinthe dont tous les murs sont
        fermés.
        Cette méthode ne doit être appelée qu'une fois à l'intialisation du labyrinthe !
        """
        # Structure pour mémoriser les chemins créés
        chemins = [*range(0,self.tailleX*self.tailleY)]
        # Structure pour memoriser les murs que l'on pourrait tenter d'ouvrir
        murs = []
        for y in range(0,self.tailleY):
            for x in range(0,self.tailleX):
                if y > 0: murs.append({"x":x,"y":y,"pos":"nord"})
                if x < self.tailleX - 1: murs.append({"x":x, "y":y, "pos":"est"})

        # On supprime des murs autant de fois que de cases moins 1
        nbMursSupprimes = 0
        while nbMursSupprimes < self.tailleX*self.tailleY-1:
            # Tirer un mur au hasard
            murASupprimer = random.choice(murs)

            case = self.getCase(murASupprimer["x"],murASupprimer["y"])

            if murASupprimer["pos"] == "nord":
                # On supprime un mur haut
                chemin1 = chemins[murASupprimer["y"] * self.tailleX + murASupprimer["x"]]
                chemin2 = chemins[(murASupprimer["y"]-1) * self.tailleX + murASupprimer["x"]]

                if not case.estOuvertNord() and not chemin1 == chemin2:
                    # Condition1 : Le mur n'est pas déjà ouvert...
                    # Condition2 : les chemins ne sont pas identiques
                    caseOrigine = self.getCase(murASupprimer["x"],murASupprimer["y"])
                    caseDestination = self.getCase(murASupprimer["x"], murASupprimer["y"]-1)
                    caseOrigine.ouvrirNord()
                    caseDestination.ouvrirSud()
                    # Mettre à jour les chemins
                    for i in range(len(chemins)):
                        if chemins[i] == chemin2: chemins[i] = chemin1
                    # On a ouvert un mur, on incrémente !
                    nbMursSupprimes += 1

            elif murASupprimer["pos"] == "est":
                # On supprime un mur haut
                chemin1 = chemins[murASupprimer["y"] * self.tailleX + murASupprimer["x"]]
                chemin2 = chemins[murASupprimer["y"] * self.tailleX + murASupprimer["x"]+1]

                if not case.estOuvertEst() and not chemin1 == chemin2:
                    # Les chemins sont différentsn on fusionne !
                    caseOrigine = self.getCase(murASupprimer["x"],murASupprimer["y"])
                    caseDestination = self.getCase(murASupprimer["x"]+1, murASupprimer["y"])
                    caseOrigine.ouvrirEst()
                    caseDestination.ouvrirOuest()
                    # Mettre à jour les chemins
                    for i in range(len(chemins)):
                        if chemins[i] == chemin2: chemins[i] = chemin1
                    # On a ouvert un mur, on incrémente !
                    nbMursSupprimes += 1

            murs.remove(murASupprimer)


