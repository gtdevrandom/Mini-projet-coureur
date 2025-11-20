import pygame, sys
from pygame.locals import *

# from projet_coureur_personnage import *
#from projet_coureur_arbre import *



#****************************************
def affichage_rue():
    pygame.draw.rect(window, (192,192,192),(0, 200, WIDTH, HEIGHT//2),0)

#***************** prog principal ********************
pygame.init()

#la fenêtre du jeu
WIDTH = 800
HEIGHT = 300
window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
CIEL = (135,206,235)

sonic = personnage()

#****** boucle infinie ************************

while True:
    window.fill(CIEL)
    affichage_rue()


    sonic.affichage_personnage(window,sonic.index)

#permet de gérer les evenements du clavier ou de la souris
    for event in pygame.event.get():
        if event.type == QUIT:  #croix rouge
            pygame.quit()
            sys.exit()


#rafraichissement de l'écran
    pygame.display.flip()





