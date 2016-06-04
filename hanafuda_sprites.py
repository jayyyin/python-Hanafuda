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

class ScreenSection():
    '''this will contain information like x and y bounding boxes'''
    def __init__(self, topLeftX, topLeftY, bottomRightX, bottomRightY):
        self.tLX = topLeftX
        self.tLY = topLeftY
        self.bRX = bottomRightX
        self.bRY = bottomRightY
        self.centerX = (self.tLX + self.bRX) /2
        self.centerY = (self.tLY + self.bRY) / 2
        

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
        self.rect = self.image.get_rect()
        
        
class Button(pygame.sprite.Sprite):
    '''this is a button sprite'''
    
    def __init__(self, screen, screenSection, buttonType):
        
        pygame.sprite.Sprite.__init__(self)  
        
        self.__screen = screen
        self.screenSection = screenSection
        self.buttonType = buttonType
        
        if buttonType == "Quit":
            self.image = pygame.image.load("images/buttons/Quit.gif").convert()
            self.rect = self.image.get_rect()
            self.rect.centerx = screenSection.centerX
            self.rect.centery = screenSection.centerY - 100
            
    def get_centerx(self):
        '''this method returns the center x of the tank'''
        return self.rect.centerx 
    def get_centery(self):
        '''this method returns the center y of the tank'''
        return self.rect.centery   
            
    def get_rect_left(self):
        '''this method returns the left of the tank'''
        return self.rect.left
    def get_rect_bottom(self):
        '''this method returns the bottom of the tank'''
        return self.rect.bottom  
    def get_rect_right(self):
        '''this method returns the right of the tank'''
        return self.rect.right
    def get_rect_top(self):
        '''this method returns the top of the tank'''
        return self.rect.top
    
    def within(self, x, y):
        print "x:" + str(x)
        print "y:" + str(y)
        print "x1:" + str(self.rect.left)
        print "x2:" + str(self.rect.right)
        print "y1:" + str(self.rect.top)
        print "y2:" + str(self.rect.bottom)        
        return x > self.rect.left and x < self.rect.right and y > self.rect.top and y < self.rect.bottom
            
        