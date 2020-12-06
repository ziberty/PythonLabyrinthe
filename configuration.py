import niveau

def singleton(classe):
    instances = {}

    def getInstance(*liste, **dictionnaire):
        if classe not in instances:
            instances[classe] = classe(*liste, **dictionnaire)
        return instances[classe]

    return getInstance

@singleton
class Configuration:

    def __init__(self, lvl):
        self.lvl = lvl

    """"def choiceLvl(self):
        self.lvl = 0
        while not (self.lvl >= 1 and self.lvl <= 3):
           try:
               self.lvl = int(input("> Entrez un niveau : "))
           except ValueError:
               print("Votre entrée n'est pas correcte")

        return self.lvl"""

    def getLvl(self):
        return self.lvl

    def config(self, lvl):
        if lvl == 1:
            nomNiveau = "niveau 1"
            Niveau = niveau.creerNiveau(nomNiveau) 
            Niveau.game1()

        elif lvl == 2:
            nomNiveau = "niveau 2"
            Niveau = niveau.creerNiveau(nomNiveau) 
            Niveau.game2()

        elif lvl == 3:
            nomNiveau = "niveau 3"  
            Niveau = niveau.creerNiveau(nomNiveau) 
            Niveau.game3()

        return Niveau
