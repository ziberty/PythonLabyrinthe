class Case:
    """ Une cse du labyrinthe.
    Une case possède au maxiumum 4 voisins, aux nord, sud, est et ouest. Seules les cases du bord n'ont pas de voisin, l'attribut correspondant est alors None.
    Ces références servent à la navigation dans le labyrinthe d'une case à une autre.
    Même si la case a un mur, les références vers les voisins sont stockées au niveau de la case, au cas où on pourrait casser le mur.
    Une série de 4 attributs boolean indiquent si la case est ouverte pour chaque point cardinal. S'il est False, il y a un mur et on ne peut pas aller dans cette direction.
    Un boolean permet de savoir si la case a été découverte ou pas, pour l'affichage du labyrinthe au fur et à mesure qu'on le découvre.
    Enfin, chaque cose conserve une référence vers le joueur s'il est présent sur la case (pour l'affichage), ainsi que deux liste,
    une pour les objets sur la case, l'autre pour les personnages.
    """

    def __init__(self):
        # Les booleans qui indiquent s'il y a des murs ou pas (initialement tout fermé)
        self.__ouvertNord = False
        self.__ouvertSud = False
        self.__ouvertEst = False
        self.__ouvertOuest = False

        # Les références vers les cases voisines. Elle ne sont pas initialisées ici lorsqu'on crée une case unique.
        # C'est le rôle de la classe Labyrinthe de créer toutes les cases et de les positionner les unes par rapport aux autres.
        self.__caseNord = None
        self.__caseSud = None
        self.__caseEst = None
        self.__caseOuest = None

        # Si la case a été découverte ou pas
        self.__decouvert = False

        # Le joueur s'il est sur la case, None sinon
        self._joueur = None
        # La liste des personnages sur la case
        self._personnages = []
        # La liste des objets sur la case
        self._objets = []
        # La sortie
        self._sortie = []


    def ajouterJoueur(self,joueur):
        """ Stock la référence du joueur. A utiliser lorsque le joueur arrive sur la case. """
        self._joueur = joueur
        self.__decouvert = True

    def supprimerJoueur(self):
        """ Retire la référence du joueur, à utiliser lorsque le joueur quitte la case."""
        self._joueur = None

    def afficherLigne1(self):
        """ Affiche la première ligne (le haut) de la case. En fonction de la présence de mur en haut, on n'affiche pas la même chose. """
        if self.__decouvert or (self.__caseNord != None and self.__caseNord.estDecouvert()):
            if self.__ouvertNord: print("+   ", end="")
            else: print("+---", end="")
        else:
            print("####", end="")

    def afficherLigne2(self):
        """ Affiche la deuxième ligne de la case (le contenu). En fonction de ce qui est présent sur la case, on n'affiche pas la même chose. """
        if self.__decouvert or (self.__caseOuest != None and self.__caseOuest.estDecouvert()):
            print(" ", end="") if self.__ouvertOuest else print("|", end="")
        else:
            print("#",end="")
        if self.estDecouvert():
            ## Afficher le contenu de la case ici:
            if self._joueur:
                print(" "+self._joueur.getSymbole()+" ",end="") # Le joueur est présent
            elif len(self._sortie) > 0:
                print(" ▲ ", end="")# Sortie
            elif len(self._personnages) > 0 and len(self._objets) > 0:
                print(" % ", end="") # Il y a à la fois personnage(s) et objet(s)
            elif len(self._personnages) > 0:
                print(" P ", end="") # Il n'y a que des personnages
            elif len(self._objets) > 0:
                print(" . ", end="") # Il n'y a que des objets
            else:
                print("   ", end="") # Il n'y a rien
        else:
            print("###", end="")

    # Getters pour récupérer les cases voisines
    def getCaseNord(self): return self.__caseNord
    def getCaseSud(self): return self.__caseSud
    def getCaseEst(self): return self.__caseEst
    def getCaseOuest(self): return self.__caseOuest

    # Setters pour positionner les cases voisines
    def setCaseNord(self, caseDestination): self.__caseNord = caseDestination
    def setCaseSud(self, caseDestination): self.__caseSud = caseDestination
    def setCaseEst(self, caseDestination): self.__caseEst = caseDestination
    def setCaseOuest(self, caseDestination): self.__caseOuest = caseDestination

    # Getters pour récupérer la présence ou non de mur
    def estOuvertNord(self): return self.__ouvertNord
    def estOuvertSud(self): return self.__ouvertSud
    def estOuvertEst(self): return self.__ouvertEst
    def estOuvertOuest(self): return self.__ouvertOuest

    # Setters pour ouvrir un mur
    def ouvrirNord(self): self.__ouvertNord = True
    def ouvrirSud(self): self.__ouvertSud = True
    def ouvrirEst(self): self.__ouvertEst = True
    def ouvrirOuest(self): self.__ouvertOuest = True

    # Getter pour savoir si la case est déjà découverte ou non
    def estDecouvert(self): return self.__decouvert
    # Setter pour passer l'attribut _decouvert à True (case découverte)
    def decouvrir(self): self.__decouvert = True



    def ajouterObjet(self,objet):
        """ Ajoute un objet dans la liste des objets présents sur la case
        :param objet: l'objet à ajouter
        :return: rien
        """
        self._objets.append(objet)


    def supprimerObjet(self, objet):
        """ Supprime un objet présent sur la case. Passer la référence de l'objet à supprimer
        :param objet: l'objet à supprimer. Passer la référence de l'objet qui sera recherché dans la liste pour être supprimé.
        :return: rien
        """
        self._objets.remove(objet)

    def ajouterSortie(self, sortie):
        """ajouter une sortie dans a la liste sorties"""
        self._sortie.append(sortie)

    def ajouterPersonnage(self, personnage):
        """ Ajoute le personnage sur la case
        :param personnage: Un personnage
        :return: rien
        """
        self._personnages.append(personnage)

    def getSortie(self):
        """ Renvoie la liste des sorties présentes sur la case. """
        return self._sortie

    def getObjets(self):
        """ Renvoie la liste des objets présents sur la case. """
        return self._objets


    def getPersonnages(self):
        """ Renvoie la liste des personnages présents sur la case. """
        return self._personnages

