import pygame, sys
from pygame.locals import *


#****************************************
class personnage:

    #consctructeur de la classe
    def __init__(self):

        perso = pygame.image.load('sonic_104_114.png').convert_alpha()
        self.image=[]
        for x in range(0,9*104, 104):
            self.image.append(perso.subsurface(x,0,104,114))

        self.index=0

#fonction permettant d'affichr le personnage dans notre fenétre
    def affichage_personnage(self,fenetre,index_image):
        #blit permet d'afficher un elément à l'écran
        fenetre.blit(self.image[index_image],(400,170))

#fonction faisant bouger le perso
    def bouge_personnage(self,fenetre):
        self.index = self.index +1
        if self.index == len(self.image):
            self.index=0
        self.affichage_personnage(fenetre,self.index)
