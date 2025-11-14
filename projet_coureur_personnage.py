import pygame, sys
from pygame.locals import *


#****************************************
# Classe pour gérer le personnage (Sonic)
class personnage:

    #constructeur de la classe
    def __init__(self):
        """Initialise le personnage avec ses sprites et ses états"""
        perso = pygame.image.load('sonic_104_114.png').convert_alpha()
        self.image = []
        for x in range(0, 9*104, 104):
            self.image.append(perso.subsurface(x, 0, 104, 114))

        self.index = 0
        self.court = False  # Indique si le personnage court actuellement

    def affichage_personnage(self, fenetre, index_image):
        """Affiche le personnage à l'écran
        Args:
            fenetre: surface pygame où afficher le personnage
            index_image: index de l'image du sprite à afficher
        """
        #blit permet d'afficher un élément à l'écran
        fenetre.blit(self.image[index_image], (400, 170))

    def bouge_personnage(self, fenetre):
        """Anime le personnage en cours de route
        Args:
            fenetre: surface pygame où afficher le personnage
        """
        if self.court:
            self.index = self.index + 1
            if self.index == len(self.image):
                self.index = 0
        self.affichage_personnage(fenetre, self.index)
    
    def demarrer_course(self):
        """Démarre la course du personnage"""
        self.court = True
    
    def arreter_course(self):
        """Arrête la course du personnage"""
        self.court = False
        self.index = 0  # Réinitialise l'animation

