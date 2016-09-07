'''
author: Jay Yin

Date: June 4

Discription : sprites for hanafuda

   ChangeLog:
   
   0.1a setting up "Card" sprite
   0.2  added showing cards on screen
      bug-- still need to fix locations of centerboard and make the function work for the future coming player stuff and the scoreboard as well
   0.3  fixed bug above
        made board work mostly for all types
        '''
import pygame
import math
import random
import time
#button numbers
QUIT = 0
START = 1
BACK = 2
#card type numbers
DREG = 0
LIGHT = 1
RIBBON = 2
ANIMAL = 3


class ScreenSection():
    '''this will contain information like x and y bounding boxes'''
    def __init__(self,name , topLeftX, topLeftY, bottomRightX, bottomRightY):
        self.name = name
        self.tLX = topLeftX
        self.tLY = topLeftY
        self.bRX = bottomRightX
        self.bRY = bottomRightY
        self.centerX = (self.tLX + self.bRX) /2
        self.centerY = (self.tLY + self.bRY) / 2
        self.width = abs(self.tLX - self.bRX)
        self.height = abs(self.tLY -  self.bRY)
        
class Board():
    '''initializes any board'''
    def __init__(self,SS, col, row):
        slotNumber = 0
        self.slots = [[0 for x in range(2)] for y in range(row * col) ] 
        colOffSet = 1
        rowOffSet = 1
        
        #set (i-... to 0 for both cases below
        #in case the row number or column number is 1
        #if col == 1:
            #colOffSet = 0
        #if row == 1:
            #rowOffSet = 0
            
        for j in range (1,row + 1):
            for i in range(1,col + 1):
                
                #self.slots[slotNumber][0] = ScreenSection("", SS.width * (i - 1) / i, SS.height * (j - 1) / j, SS.width / i, SS.height / j ) incorrect
                self.slots[slotNumber][0] = ScreenSection("", ((SS.width / col)* (i - colOffSet))  + SS.tLX, ((SS.height / row) * (j - rowOffSet)) + SS.tLY, 
                                                          ((SS.width / col)* (i)) + SS.tLX, ((SS.height / row) * (j)) + SS.tLY)
                self.slots[slotNumber][1] = False
                #false if the slot is empty
                slotNumber+= 1

#class CenterBoard():
    #'''initializes the center board'''
    #def __init__(self,SS):
        
        #slotNumber = 0
        #col = 4
        #row = 2
        #self.slots = [[0 for x in range(row)] for y in range(row * col)] 
        #for j in range (1,row + 1):
            #for i in range(1,col + 1):
                
                ##self.slots[slotNumber][0] = ScreenSection("", SS.width * (i - 1) / i, SS.height * (j - 1) / j, SS.width / i, SS.height / j ) incorrect
                #self.slots[slotNumber][0] = ScreenSection("", ((SS.width / col)* (i - 1)) + SS.tLX, ((SS.height / row) * (j - 1)) + SS.tLY, 
                                                          #((SS.width / col)* (i)) + SS.tLX, ((SS.height / row) * (j)) + SS.tLY)
                #self.slots[slotNumber][1] = False
                ##false if the slot is empty
                #slotNumber+= 1
            


class Card(pygame.sprite.Sprite):  
    '''this is the sprite that contains the card information
       screenSection will contain "player 1 hand or player 2 hand or player 1 score or deck or board?"
    '''
    def __init__(self, screen, screenSection, ID):
        '''Init cards to facedown '''
        pygame.sprite.Sprite.__init__(self)  
        
        self.__screen = screen
        #card id 0 is back
        self.cardID = ID
        self.faceUp = False
        self.mousedOnTF = False
        self.__screenSection = screenSection
        self.highlightColour = (255,255,0)
        self.month = 0
        self.imageID = 0
        self.cardType = 0
        self.originalImage = pygame.image.load("images\\Hanafuda set1\\" + str(self.imageID) + ".jpg").convert()
        self.scaledImage = pygame.transform.scale(self.originalImage, (int(self.originalImage.get_rect().width / 2), int (self.originalImage.get_rect().height /2)))
        self.image = self.scaledImage
        self.rect = self.image.get_rect()
        self.rect.left = screenSection.tLX
        self.rect.top = screenSection.tLY 
        self.highlight = 0
        
    def setCardID(self, ID):
        self.cardID = ID
        
    def mousedOn(self):
        #self.highlight = pygame.draw.rect(self.__screen,self.highlightColour, self.rect, 1)
        self.image =  pygame.transform.scale(self.originalImage, (int(self.originalImage.get_rect().width / 1.5), int (self.originalImage.get_rect().height /1.5)))
        #return self.highlight
        ##self.image = pygame.transform.scale(self.image, (int(self.image.get_rect().width *1.5), int (self.image.get_rect().height *1.5)))
        
    def mousedOff(self):
        self.image = self.scaledImage
        #self.highlight = 0
        ##self.image = pygame.transform.scale(self.image, (int(self.image.get_rect().width /1.5), int (self.image.get_rect().height /1.5)))    
    
    def updateImage(self):
        if self.faceUp and self.imageID != self.cardID:
            self.imageID = self.cardID  
        elif not self.faceUp:
            self.imageID = 0
        self.originalImage = pygame.image.load("images\\Hanafuda set1\\" + str(self.imageID) + ".jpg").convert()
        self.scaledImage = pygame.transform.scale(self.originalImage, (int(self.originalImage.get_rect().width / 2), int (self.originalImage.get_rect().height /2))) 
        self.image = self.scaledImage
            
    def setScreenSection(self, screenSection):
        self.__screenSection = screenSection
        self.rect.left = screenSection.tLX
        if screenSection.name == "hand":
            self.rect.bottom = screenSection.bRY
        else:
            self.rect.top = screenSection.tLY  
        
    def within(self, x, y):       
        return x >= self.rect.left and x <= self.rect.right and y >= self.rect.top and y <= self.rect.bottom    
    #def update(self):
    
    def match(self, card):
        self.cardID
        
class Button(pygame.sprite.Sprite):
    '''this is a button sprite'''
    
    def __init__(self, screen, screenSection, buttonType):
        
        pygame.sprite.Sprite.__init__(self)  
        
        self.__screen = screen
        self.screenSection = screenSection
        self.buttonType = buttonType
        self.image = pygame.image
        self.pressedDown = False
        
        
        if buttonType == QUIT:
            self.image = pygame.image.load("images/buttons/Quit.gif").convert()
            self.rect = self.image.get_rect()
            self.rect.centerx = screenSection.centerX
            self.rect.centery = screenSection.centerY - 90
        elif buttonType == START:
            self.image = pygame.image.load("images/buttons/Start.gif").convert()
            self.rect = self.image.get_rect()
            self.rect.centerx = screenSection.centerX
            self.rect.centery = screenSection.centerY - 160            
        elif buttonType == BACK:
            self.image = pygame.image.load("images/buttons/Back.gif").convert()
            self.rect = self.image.get_rect()
            self.rect.left = screenSection.tLX
            self.rect.top = screenSection.tLY
            
            
    def get_centerx(self):
        '''this method returns the center x of the button'''
        return self.rect.centerx 
    def get_centery(self):
        '''this method returns the center y of the button'''
        return self.rect.centery   
            
    def get_rect_left(self):
        '''this method returns the left of the button'''
        return self.rect.left
    def get_rect_bottom(self):
        '''this method returns the bottom of the button'''
        return self.rect.bottom  
    def get_rect_right(self):
        '''this method returns the right of the button'''
        return self.rect.right
    def get_rect_top(self):
        '''this method returns the top of the button'''
        return self.rect.top
    
    def within(self, x, y):
        #print "x:" + str(x)
        #print "y:" + str(y)
        #print "x1:" + str(self.rect.left)
        #print "x2:" + str(self.rect.right)
        #print "y1:" + str(self.rect.top)
        #print "y2:" + str(self.rect.bottom)        
        return x >= self.rect.left and x <= self.rect.right and y >= self.rect.top and y <= self.rect.bottom
    
    def pressed(self):
        self.pressedDown = True
        self.image = pygame.transform.scale(self.image, (int(self.rect.width * 0.9 ), int (self.rect.height * 0.9 )))
        
    def released(self):
        self.pressedDown = False
        self.image = pygame.transform.scale(self.image, (int(self.rect.width * 1), int (self.rect.height * 1 )))
        