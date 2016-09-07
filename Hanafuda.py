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
    
    localPlayer_handSS = pySprites.ScreenSection("localPlayer_handSS", 50 , screen.get_height() *2 /3, 
                                                 screen.get_width() -10, screen.get_height() -10)
    
    
    titleBarButtons = []
    MenuButtons = []
    localPlayer_hand =[]
    localPlayer_score = []
    remotePlayer_hand = []
    remotePlayer_score = []
    centerBoardSprites = []
    deck = []
    deckSprites = []
    
    backButton = pySprites.Button(screen,titleBarSS, BACK)
    startGameButton = pySprites.Button(screen,buttonsSS, START)
    quitButton = pySprites.Button(screen,buttonsSS, QUIT)
    MenuButtons.append(startGameButton)
    MenuButtons.append(quitButton)
    titleBarButtons.append(backButton)
    
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
    
    # Hide the mouse pointer
    #pygame.mouse.set_visible(False)
    
    # LOOP
    while keepGoing:
        clock.tick(30)
        
        while menu:
            # TIME
            clock.tick(30)
            
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
            
            if(gameToBeInit):
                #clearing board and deck for reinisialization
                deck[:] = []
                centerBoardSprites[:] = []
                deckSprites[:] = []
                
                #clearing hands and score for reinisialization
                localPlayer_hand[:] = []
                remotePlayer_hand[:] = []
                localPlayer_score[:] = []
                remotePlayer_score[:] = []
                
                #inisializing deck
                col = 4
                row = 2
                tempdeck = range(1,49)
                deck = random.sample(tempdeck, 48)
                
                for i in deck:
                    deckSprites.append(pySprites.Card(screen, DeckSS, i))
                #initialzing centerBoard
                centerBoard =  pySprites.Board(centerBoardSS, col, row)
                
                #inisializing cards on board
                for i in range(col * row):
                    centerBoardSprites.append(deckSprites.pop())
                    centerBoardSprites[i].setScreenSection(centerBoard.slots[i][0])
                    centerBoardSprites[i].faceUp = True
                    centerBoardSprites[i].updateImage()
                    centerBoard.slots[i][1] = True
                
                gameToBeInit = False
                
            centerBoardSpritesGroup = pygame.sprite.Group(centerBoardSprites)
            deckSpritesGroup = pygame.sprite.Group(deckSprites)
            
            
            clock.tick(30)
            for event in pygame.event.get():
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
                        
            screen.blit(background, (0, 0))
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