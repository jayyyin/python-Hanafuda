'''
author: Jay Yin

Date: June 4

Discription : sprites for hanafuda

   ChangeLog:
   
   0.1a setting up "Card" sprite
        '''
import pygame
import math
import random
import time

class Card(pygame.sprite.Sprite):  
    '''this is the sprite that contains the card information
       screenSection will contain "player 1 hand or player 2 hand or player 1 score or deck or board?"
    '''
    def __init__(self, screen, screenSection):
        '''Init cards to facedown '''
        pygame.sprite.Sprite.__init__(self)  
        
        self.__screen = screen
        #card id 0 is back
        self.cardID = 0
        self.faceUp = False
        self.__screenSection = screenSection
        self.imageID = 0
        self.image = pygame.image.load("images/Hanafuda set1/" + str(self.imageID) + ".jpg")
        
        