'''
   This is an experimental game (will probably be called Hanafuda Battle if ever ported to android)
'''

# I - IMPORT AND INITIALIZE
import pygame, hanafuda_sprites, random
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1024,768))
pySprites = hanafuda_sprites

# Create a list of Joystick objects.
joysticks = []
for joystick_no in range(pygame.joystick.get_count()):
    stick = pygame.joystick.Joystick(joystick_no)
    stick.init()
    joysticks.append(stick)

QUIT = 0
START = 1
BACK = 2

def main():
    '''This function defines the 'mainline logic' for our game.'''
      
    # DISPLAY
    pygame.display.set_caption("Hanafuda prototype")
    
    background = pygame.image.load("images\\background\\Tatami.JPG")
    thanks = pygame.image.load("images\\Thanks.gif")
    
    gameToBeInit = True
    
    
    
    # ENTITIES 
    buttonsSS = pySprites.ScreenSection("buttonsSS" ,screen.get_width()/2 -200, screen.get_height()/2 -100, 
                                         screen.get_width()/2 + 200, screen.get_height() -100)
    
    titleBarSS = pySprites.ScreenSection("titleBarSS", 0,screen.get_height() /3,
                                         screen.get_width() / 5, screen.get_height() * 2 /3)
    
    bottomPlayerSS = pySprites.ScreenSection("bottomPlayerSS", 50, screen.get_height() *2 /3,
                                         screen.get_width() /2, screen.get_height()-100)
    
    centerBoardSS = pySprites.ScreenSection("centerBoardSS", screen.get_width() / 3 ,screen.get_height() /3,
                                         screen.get_width()-50, screen.get_height() *2 /3)
    
    DeckSS = pySprites.ScreenSection("DeckSS", screen.get_width() / 5 ,screen.get_height() /3,
                                             screen.get_width() / 3, screen.get_height() *2 /3)   
    
    localPlayer_handSS = pySprites.ScreenSection("hand", screen.get_width() / 5 , screen.get_height() *2 /3 + 50, 
                                                 screen.get_width() - 200, screen.get_height())
    
    localPlayer_scoreSS = pySprites.ScreenSection("score", screen.get_width() - 200 , screen.get_height() *2 /3 + 50, 
                                                     screen.get_width() - 200, screen.get_height()- 50)    
    
    
    titleBarButtons = []
    MenuButtons = []
    localPlayer_handSprites =[]
    localPlayer_scoreSprites = []
    remotePlayer_handSprites = []
    remotePlayer_scoreSprites = []
    centerBoardSprites = []
    deck = []
    deckSprites = []
    maxCardsInHand = 8
    cardHighlights = []
    matchedCards = []
    hoveredCard = 0
    
    backButton = pySprites.Button(screen,titleBarSS, BACK)
    startGameButton = pySprites.Button(screen,buttonsSS, START)
    quitButton = pySprites.Button(screen,buttonsSS, QUIT)
    MenuButtons.append(startGameButton)
    MenuButtons.append(quitButton)
    titleBarButtons.append(backButton)
    
    deck[:] = []
    centerBoardSprites[:] = []
    deckSprites[:] = []
                    
    #clearing hands and score for reinisialization
    localPlayer_handSprites[:] = []
    remotePlayer_handSprites[:] = []
    localPlayer_scoreSprites[:] = []
    remotePlayer_scoreSprites[:] = []
                    
    #inisializing deck
    deckCol = 6
    deckRow = 2
    tempdeck = range(1,49)
    deck = random.sample(tempdeck, 48)
    
    for i in deck:
        deckSprites.append(pySprites.Card(screen, DeckSS, i))
        #initialzing centerBoard
        centerBoard =  pySprites.Board(centerBoardSS, deckCol, deckRow)
        localPlayer_handBoard =  pySprites.Board(localPlayer_handSS, maxCardsInHand, 1)
        localPlayer_scoreBoard = pySprites.Board(localPlayer_scoreSS, 10,5)
        
    #inisializing cards on board
    for i in range((deckCol-2) * deckRow):
        #print deckSprites
        centerBoardSprites.append(deckSprites.pop())
        centerBoardSprites[i].setScreenSection(centerBoard.slots[i][0])
        centerBoardSprites[i].faceUp = True
        centerBoardSprites[i].updateImage()
        centerBoard.slots[i][1] = True
            
    #inisializing cards on local hand
    for i in range(maxCardsInHand):
        localPlayer_handSprites.append(deckSprites.pop())
        localPlayer_handSprites[i].setScreenSection(localPlayer_handBoard.slots[i][0])
        localPlayer_handSprites[i].faceUp = True
        localPlayer_handSprites[i].updateImage()
        localPlayer_handBoard.slots[i][1] = True
                        
                    
    gameToBeInit = False    
    localPlayer_handGroup = pygame.sprite.Group(localPlayer_handSprites)
    centerBoardSpritesGroup = pygame.sprite.Group(centerBoardSprites)
    deckSpritesGroup = pygame.sprite.Group(deckSprites)        
    cardHighlightsGroup =  pygame.sprite.Group(cardHighlights)
    #the "base line" for the ground
    #topy = screen.get_height()- 200
    
    
    #while len(ground) < screen.get_width():
        
        #hill_chance = random.randrange(0, 18)
        ##if hill chance is anything but 0 it will generate a flat ground, else it will generate a hill for the next couple pixels
        #if (hill_chance != 0):
            #ground.append(pySprites.Ground(screen,leftx, topy))
            #leftx =leftx + 1
        #else:
            ## generating random hill sizes each time
            #hill_size = random.randrange(5,15,2)
            ##first loop for left side up to top of hill   
            #for pixel in range(1,hill_size, 1):
                ##a "less than 1" exponent for rounding effect of the hill
                #ground.append(pySprites.Ground(screen,leftx, topy- (pixel**0.85)))
                #leftx =leftx + 1
            ##2nd loop for the top of hill flat section
            #for pixel in range(1,int(hill_size/1.5)):
                #ground.append(pySprites.Ground(screen,leftx, topy- hill_size**0.85))
                #leftx = leftx + 1
            ##3rd loop for the right half of the hill
            #for pixel in range(hill_size, 0, -1):
                #ground.append(pySprites.Ground(screen,leftx, topy- (pixel**0.85)))
                #leftx =leftx + 1
                
    #groundgroup = pygame.sprite.Group(ground)
    menuButtonGroup = pygame.sprite.Group(MenuButtons)
    titleBarGroup = pygame.sprite.Group(titleBarButtons)
    #deckSpritesGroup = pygame.sprite.Group(deckSprites)
    # ASSIGN
    clock = pygame.time.Clock()
    keepGoing = True
    menu = True
    game = True    
    NumOFCardsMatched = 0
    scoreSlot = 0   
    
    # Hide the mouse pointer
    #pygame.mouse.set_visible(False)
    
    # LOOP
    while keepGoing:
        clock.tick(30)
        
        while menu:
            # TIME
            #clock.tick(30)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menu = False
                    game = False                    
                    keepGoing = False      
                    
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mousex,mousey = pygame.mouse.get_pos()
                    #print quitButton.within( mousex, mousey)
                    if quitButton.within(mousex, mousey):
                        quitButton.pressed()
                        #print "quit"
                        
                    elif startGameButton.within(mousex, mousey):
                        startGameButton.pressed()
                        
                elif event.type == pygame.MOUSEBUTTONUP:
                    if quitButton.pressedDown:
                        quitButton.released()
                        pygame.time.delay(1000)
                        menu = False
                        game = False
                        keepGoing = False   
                    elif startGameButton.pressedDown:
                        startGameButton.released()
                        menu = False
                        game = True                        
                    
        
                        # REFRESH SCREEN
        
            #allSprites.update()
            #allSprites.draw(screen)  
            #groundgroup.update()
            #groundgroup.draw(screen)
            screen.blit(background, (0, 0))
            menuButtonGroup.draw(screen)
            pygame.display.flip()
            
        while game:
            
            #if(gameToBeInit):
                #clearing board and deck for reinisialization
                #print "done"
                
            for event in pygame.event.get():
                for card in localPlayer_handSprites:
                    mouseX, mouseY = pygame.mouse.get_pos()
                                
                    #print mouseX
                    if card.within(mouseX, mouseY) and not card.mousedOnTF:
                    
                        #cardHighlights.append([card.cardID,card.mousedOn()])
                        for cardB in centerBoardSprites:
                            #for each in centerBoardSprites:
                            #print each                        
                            if card.matches(cardB):
                                matchedCards.append(cardB)
                                hoveredCard = card
                                #if cardB not in matchedCards:
                                    #NumOFCardsMatched += 1
                                #print str(card.cardID) + " :: " + str(cardB.cardID)
                                cardB.mousedOn()
                               
                                        
                            
                            card.mousedOn()
                            #print "true"
                            card.mousedOnTF = True
                    elif card.mousedOnTF and  not card.within(mouseX, mouseY) and not card.keepHighlighted:
                        card.match = False
                        NumOFCardsMatched = 0
                        for cardB in matchedCards:
                            cardB.match = False
                            cardB.mousedOff()
                        matchedCards[:] = []
                        #print matchedCards
                        card.mousedOff()
                        card.mousedOnTF = False
                if event.type == pygame.MOUSEBUTTONUP:
                    print matchedCards
                    if len(matchedCards) == 1:
                        index = centerBoardSprites.index(matchedCards[0])
                        for i in localPlayer_scoreBoard.slots:
                            #if the slot isn't taken put the card in
                            if not i[1]:
                                scoreSlot = localPlayer_scoreBoard.slots.index(i)
                                i[1] = True
                        localPlayer_scoreSprites.append(localPlayer_handSprites.pop(localPlayer_handSprites.index(hoveredCard)))
                        localPlayer_scoreSprites.append(centerBoardSprites.pop(index))
                        hoveredCard.setScreenSection(localPlayer_scoreBoard.slots[scoreSlot][0])
                        matchedCards[0].setScreenSection(localPlayer_scoreBoard.slots[scoreSlot - 1][0])
                        centerBoard.slots[index][1] = False     
                        hoveredCard.updateImage()
                        matchedCards[0].updateImage()
                        print localPlayer_scoreBoard
           
                if event.type ==  pygame.QUIT:
                    menu = False
                    game = False
                    keepGoing = False  
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mousex,mousey = pygame.mouse.get_pos()
                    if backButton.within(mousex, mousey):
                                    
                        backButton.pressed()
                                    
                elif event.type == pygame.MOUSEBUTTONUP:
                    if backButton.pressedDown:
                        gameToBeInit = True
                        backButton.released()
                        menu = True
                        game = False                                    
            
            
            #clock.tick(30) 
            pygame.display.update()
                
                        
            screen.blit(background, (0, 0))
            #cardHighlightsGroup.draw(screen)
            #for item in cardHighlights:
                #item[1].draw(screen)
                   
            localPlayer_handGroup.draw(screen)
            centerBoardSpritesGroup.draw(screen)
            deckSpritesGroup.draw(screen)
            titleBarGroup.draw(screen)
            pygame.display.flip()
    
    pygame.mouse.set_visible(True)
    screen.blit(background,(0,0))
    screen.blit(thanks, (screen.get_width() / 2 - thanks.get_width() /2 , screen.get_height() /4))
    pygame.display.flip()
    pygame.time.delay(1500)
    pygame.quit()
        

main()
