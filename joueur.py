from labyrinthe.case import Case
import sys
class Joueur:

    def __init__(self, symbole,  energieInitiale):
        # La case sur laquelle se situe le joueur
        self.__caseCourante = Case()
        self.__symbole = symbole
        self.__energieMax = 100 # TODO: mettre le niveau d'énergie max en fonction du paramétrage du jeu
        self.__energie = 0
        self.__nbPieces = 0
        self.__bouclier = False
        self.__nbMorceauCle = 0
        self.__cle = 0
        self.__lampe = False
        self._objetsRares = [] #On commence sans équipement
        self._sac = [] # On commence avec un sac vide
        self.setEnergie(energieInitiale)
        
    #gestion energie
    def getEnergie(self):
        """ Renvoie le niveau d'énergie du joueur. """
        return self.__energie

    def setEnergie(self,valeur):
        """ Fixe l'energie du joueur à une valeur donnée, sans pouvoir dépasser le maximum autorisé. """
        self.__energie = min(valeur, self.__energieMax)

    def perdreEnergie(self):
        """ Retire un point d'énergie au joueur. """
        if self.__bouclier == True:
            self.__energie -= 1
        else:
            self.__energie -= 2
            
    def perdreUneEnergie(self):
        self.__energie -=1

    def gagnerEnergie(self, combien):
        """ Ajoute de l'énergie au joueur. Paramètres :
        - combien : le montant d'énergie ajouté
        """
        self.__energie = min(self.__energie + combien, self.__energieMax)

    def printEnergie(self):
        """ Petite fonction utilitaire pour afficher la jauge d'énergie sur la console. """
        print(" ENERGIE " + ">"*self.__energie + " "*(self.__energieMax-self.__energie) + "|")

    #gestion cases
    def getCaseCourante(self):
        return self.__caseCourante

    def setCaseCourante(self, case):
        # Enlève le joueur de la case sur laquelle il se trouve actuellement
        self.__caseCourante.supprimerJoueur()
        # Ajoute le joueur sur la nouvelle case
        self.__caseCourante = case
        case.ajouterJoueur(self)
        # Découvre les cases alentour
        if self.__lampe == True:
            self.decouvreAlentour()
            self.Decouvrelampe()
        else:
            self.decouvreAlentour()
        # Rencontre tous les personnages potentiellements présents sur la case
        for personnage in case.getPersonnages():
            personnage.rencontrer(self)

    def decouvreAlentour(self):
        self.__caseCourante.decouvrir()
        if self.__caseCourante.estOuvertNord(): self.__caseCourante.getCaseNord().decouvrir()
        if self.__caseCourante.estOuvertSud(): self.__caseCourante.getCaseSud().decouvrir()
        if self.__caseCourante.estOuvertEst(): self.__caseCourante.getCaseEst().decouvrir()
        if self.__caseCourante.estOuvertOuest(): self.__caseCourante.getCaseOuest().decouvrir()

    #gestion lunettes
    def lunettes(self):
        self.__caseCourante.decouvrir()
        self.__caseCourante.getCaseNord().decouvrir()
        self.__caseCourante.getCaseSud().decouvrir()
        self.__caseCourante.getCaseEst().decouvrir()
        self.__caseCourante.getCaseOuest().decouvrir()

    def Decouvrelampe(self):
        if self.__caseCourante.estOuvertNord() and self.__caseCourante.getCaseNord().estOuvertNord(): 
            self.__caseCourante.getCaseNord().getCaseNord().decouvrir()
        if self.__caseCourante.estOuvertSud() and self.__caseCourante.getCaseSud().estOuvertSud(): 
            self.__caseCourante.getCaseSud().getCaseSud().decouvrir()
        if self.__caseCourante.estOuvertEst() and self.__caseCourante.getCaseEst().estOuvertEst():
            self.__caseCourante.getCaseEst().getCaseEst().decouvrir()
        if self.__caseCourante.estOuvertOuest() and self.__caseCourante.getCaseOuest().estOuvertOuest():
            self.__caseCourante.getCaseOuest().getCaseOuest().decouvrir()

    def getLampe(self):
        self.__lampe = True

    def getSymbole(self):
        return self.__symbole

    #gestion pieces
    def addPiece(self):
        self.__nbPieces += 1

    def getPieces(self):
        return self.__nbPieces

    def depenserPieces(self):
        self.__nbPieces -= 1


    #gestion equipement
    def getObjetsRares(self):
        return self._objetsRares

    #gestion bouclier
    def getBouclier(self):
        self._objetsRares.append("Bouclier")
        self.__bouclier = True

    def ifBouclier(self):
        return self.__bouclier

    #gestion morceauClé
    def setNbMorceauCle(self):
        self.__nbMorceauCle += 1

    def getNbMorceauCle(self):
        return self.__nbMorceauCle

    def setNbCle(self):
        self._objetsRares.append("Morceau de clé")

    #gestion clé
    def ajouterCle(self):
        self._objetsRares.append("Clé")
        self.__cle += 1

    def removeMorceauCle(self):
        for i in range(3):
            self._objetsRares.remove("Morceau de clé")
        self.__nbMorceauCle = 0

    def getCle(self):
        return self.__cle

    #gestion déplacements
    def avancerNord(self):
        caseCourante = self.__caseCourante
        if caseCourante.estOuvertNord(): self.setCaseCourante(caseCourante.getCaseNord())
        else: raise ValueError("Pas de passage par là...")

    def avancerSud(self):
        caseCourante = self.__caseCourante
        if caseCourante.estOuvertSud(): self.setCaseCourante(caseCourante.getCaseSud())
        else: raise ValueError("Pas de passage par là...")

    def avancerEst(self):
        caseCourante = self.__caseCourante
        if caseCourante.estOuvertEst(): self.setCaseCourante(caseCourante.getCaseEst())
        else: raise ValueError("Pas de passage par là...")

    def avancerOuest(self):
        caseCourante = self.__caseCourante
        if caseCourante.estOuvertOuest(): self.setCaseCourante(caseCourante.getCaseOuest())
        else: raise ValueError("Pas de passage par là...")

    
    #gestion sac
    def getSac(self):
        return self._sac

    def mettreObjetDansLeSac(self,objet):
        """ Met l'objet passé en paramètre dans le sac du joueur."""
        self._sac.append(objet)