from actions import Action
from configuration import Configuration

from niveau import Niveau1,Niveau2, Niveau3

from finDefaite import FinDefaite
from finVictoire import FinVictoire

import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls()

print(""" 

         _               _         _                                              _                             _                                
        | |             (_)       (_)                                            | |                           (_)                               
   ___  | |__     ___    _   ___   _   ___   ___    ___   ____   __   __   ___   | |_   _ __    ___     _ __    _  __   __   ___    __ _   _   _ 
  / __| | '_ \   / _ \  | | / __| | | / __| / __|  / _ \ |_  /   \ \ / /  / _ \  | __| | '__|  / _ \   | '_ \  | | \ \ / /  / _ \  / _` | | | | |
 | (__  | | | | | (_) | | | \__ \ | | \__ \ \__ \ |  __/  / /     \ V /  | (_) | | |_  | |    |  __/   | | | | | |  \ V /  |  __/ | (_| | | |_| |
  \___|_|_| |_| _\___/_ |_| |___/ |_|_|___/_|___/  \___| /___|     \_/    \___/   \__| |_|     \___|   |_| |_| |_|   \_/    \___|  \__,_|  \__,_|

   __  __       __  ___        __  ____   __  
  / / /_ |     / / |__ \      / / |___ \  \ \ 
 | |   | |    / /     ) |    / /    __) |  | |
 | |   | |   / /     / /    / /    |__ <   | |
 | |   | |  / /     / /_   / /     ___) |  | |
 | |   |_| /_/     |____| /_/     |____/   | |
  \_\                                     /_/ 
                                                                                                                                          
        """)
        
lvl = int(input("Entrez votre niveau : "))

configuration = Configuration(lvl)
Niveau = configuration.config(lvl)
joueur = Niveau.getJoueur()
l = Niveau.getLabyrinthe()

cls()

print("""

  _             
 | |            
 | |        ___ 
 | |       / _ \ 
 | |____  |  __/
 |______|  \___|       
  _                _                      _           _     _            
 | |              | |                    (_)         | |   | |           
 | |        __ _  | |__    _   _   _ __   _   _ __   | |_  | |__     ___  
 | |       / _` | | '_ \  | | | | | '__| | | | '_ \  | __| | '_ \   / _ \ 
 | |____  | (_| | | |_) | | |_| | | |    | | | | | | | |_  | | | | |  __/ 
 |______|  \__,_| |_.__/   \__, | |_|    |_| |_| |_|  \__| |_| |_|  \___| 
                            __/ |                                        
                           |___/                                         
        
        
""")

input("Appuyer sur 'Entrée' pour entrer dans le labyrinthe")

while True:
    cls()  # Effacer la console
    joueur.printEnergie()
    print()
    l.afficher()
    print()

    print(""" Que dois-je faire ? 
    look: Regarder autour de vous
    move n/s/o/e: Se déplacer dans le labyrinthe (Nord : n, Sud : s, Ouest : o, Est : e)
    pick: Prendre un objet
    talk: Parler à un personnage
    bag: Ouvrir votre sac et utiliser un objet    
    rareItems: Montre les objets rares que vous avez récupéré
    open: Ouvrir la trappe pour sortir du labyrinthe
    """)

    cmd = input("Votre choix ? #> ")

    action = Action()
    action.execute(joueur, cmd)

    joueur.perdreUneEnergie()
    energie = joueur.getEnergie()
    if energie <= 0:
        cls()
        print("Vous n'avez plus la force de continuer...")
        FinDefaite.finDuJeu(joueur)