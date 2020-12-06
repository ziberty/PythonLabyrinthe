import random

class Action():
    def execute(self, joueur, cmd):

        actions = {
            "look": LookAction(),
            "move": MoveAction(),
            "pick": PickAction(),
            "talk": TalkAction(),
            "bag": BagAction(),
            "rareItems": RareItemsAction(),
            "open": Open()
        }

        move = cmd.split(" ", 1)
        if cmd == "look" or cmd == "pick" or cmd == "talk" or cmd == "bag" or cmd == "rareItems" or cmd == "open": 
            try:
                actions[cmd].execute(joueur)
            except KeyError:
                print("Commande inconnue")
        elif move == ['move', 'n'] or move == ['move', 's'] or move == ['move', 'o'] or move == ['move', 'e']:
            [action,param] = move
            try:
                actions[action].execute(joueur, param)
            except KeyError:
                print("Commande inconnue")
        else:
            print("Moi pas comprendre...")
            print("Mon vocabulaire est limité  à move n, move s, move e, move o, look, pick, talk, bag, rareItems et open ")
            input()

class LookAction(Action):
    def execute(self, joueur):
        case = joueur.getCaseCourante()
        personnages = case.getPersonnages()
        objets = case.getObjets()
        sorties = case.getSortie()
        if(len(personnages) == 0 and len(objets) == 0 and len(sorties) == 0):
            print(random.choice([
                "Je vois une salle poussièreuse, sans rien de plus que quelques cailloux.",
                "Des toiles d'araignées un peu partout.",
                "C'est déseperement vide..."
            ]))
        else:
            print("Je vois :")
            for objet in objets:
                print(" - " + objet.description())
            for personnage in personnages:
                print(" - " + personnage.description())
            for sortie in sorties:
                print(" - " + sortie.description())
        input()

class PickAction(Action):
    def execute(self, joueur):
        case = joueur.getCaseCourante()
        if len(case.getObjets()) == 0:
            print("Mais... il n'y a rien à ramasser !")
        else:
            print("J'ai ramassé :")
            for objet in case.getObjets():
                objet.ramasser(joueur)
                print(" - " + objet.description())
            case.getObjets().clear()
        input()

class TalkAction(Action):
    def execute(self, joueur):
        personnages = joueur.getCaseCourante().getPersonnages()
        if len(personnages) == 0:
            print("Allo ? allo allo allo allo allo répète l'écho")
        else:
            for personnage in personnages:
                personnage.parler(joueur)
            personnage.supprimer(joueur)
            nbMorceauCle = joueur.getNbMorceauCle()
            if nbMorceauCle >= 3:
                joueur.ajouterCle()
                joueur.removeMorceauCle()
        input()

class BagAction(Action):
    def execute(self, joueur):
        sac = joueur.getSac()
        if(len(sac)) == 0:
            print("Le sac est vide")
            input()
        else:
            print("Le sac contient: ")
            index = 0
            for obj in sac:
                print(str(index+1)+" - "+obj.description())
                index += 1
            choice = input("Pour utiliser un objet, taper son numéro, ou entrée pour ne rien faire. ")
            try:
                num = int(choice)
                obj = sac[num-1]
                sac.remove(obj)
                obj.utiliser(joueur)
            except:
                pass # En cas d'erreur, c'est que l'entrée est invalide, on ne fait rien

class RareItemsAction(Action):
    def execute(self, joueur):
        rare = joueur.getObjetsRares()
        if(len(rare)) == 0:
            print("Vous n'avez aucun objets rares")
            nbPieces = joueur.getPieces()
            print(str(nbPieces) + " pieces")
            input()
        else:
            print("Vous avez:")
            for i in range(len(rare)):
                print("- " + rare[i])
            nbPieces = joueur.getPieces()
            if nbPieces == 1:
                print(str(nbPieces) + " piece")
            else:
                print(str(nbPieces) + " pieces")
            input()

class Open(Action):
    def execute(self, joueur):
        sorties = joueur.getCaseCourante().getSortie()
        if len(sorties) == 0:
            print("Mais que voulez vous ouvrir??? il n'y a rien...")
        else:
            for sortie in sorties:
                sortie.ouvrir(joueur)
        input()

class MoveAction(Action):
    def execute(self, joueur, param):
        param = str(param)
        if param == "n":
            try:
                joueur.avancerNord()
            except:
                print("Ouch, ce mur fait mal...")
                input()
        elif param == "s":
            try:
                joueur.avancerSud()
            except:
                print("Ouch, ce mur fait mal...")
                input()
        elif param == "e":
            try:
                joueur.avancerEst()
            except:
                print("Ouch, ce mur fait mal...")
                input()
        elif param == "o":
            try:
                joueur.avancerOuest()
            except:
                print("Ouch, ce mur fait mal...")
                input()