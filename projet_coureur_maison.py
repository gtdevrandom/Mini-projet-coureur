import pygame, sys
import random
from pygame.locals import *

#*************************************************
# Classe pour gérer les maisons du décor
class maison:
    
    # Liste des images de maisons disponibles
    images_maisons = [
        'maison/maison1.png',
        'maison/maison2.png',
        'maison/maison3.png',
        'maison/maison4.png',
        'maison/maison5.png',
        'maison/maison6.png'
    ]
    
    def __init__(self, x):
        """Constructeur - crée une maison à la position x
        Args:
            x: position horizontale initiale de la maison
        """
        # Choisir une image aléatoire parmi les maisons disponibles
        image_path = random.choice(self.images_maisons)
        try:
            self.image = pygame.image.load(image_path).convert_alpha()
        except:
            # Si l'image ne charge pas, utiliser l'image PNG par défaut
            self.image = pygame.image.load('maison/maison1.png').convert_alpha()
        
        self.x = x
        self.y = 150
        self.width = self.image.get_width()
        self.height = self.image.get_height()
    
    def affichage_maison(self, fenetre):
        """Affiche la maison à l'écran
        Args:
            fenetre: surface pygame où afficher la maison
        """
        fenetre.blit(self.image, (self.x, self.y))
    
    def bouge_maison(self, vitesse):
        """Déplace la maison vers la gauche
        Args:
            vitesse: vitesse de déplacement en pixels par frame
        """
        self.x -= vitesse
