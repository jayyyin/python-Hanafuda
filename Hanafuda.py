'''
   This is an experimental game 
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
    
def main():
    '''This function defines the 'mainline logic' for our game.'''
      
    # DISPLAY
    pygame.display.set_caption("Hanafuda prototype")
    
    background = pygame.image.load("images\\background\\Tatami.JPG")
    
    screen.blit(background, (0, 0))
    
    
    
    # ENTITIES 
    buttonsSS = pySprites.ScreenSection(screen.get_width()/2 -200, screen.get_height()/2 -100, 
                                         screen.get_width()/2 + 200, screen.get_height() -100)
    
    MenuButtons = []
    player1_hand =[]
    player1_score = []
    player2_hand = []
    player2_score = []
    gameboard = []
    deck = []
    quitButton = pySprites.Button(screen,buttonsSS, "Quit")
    MenuButtons.append(quitButton)
    
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
    # ASSIGN
    clock = pygame.time.Clock()
    keepGoing = True
    
    # Hide the mouse pointer
    #pygame.mouse.set_visible(False)
    
    # LOOP
    while keepGoing:
        menu = True
        while menu:
            # TIME
            clock.tick(30)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keepGoing = False        
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mousex,mousey = pygame.mouse.get_pos()
                    print quitButton.within( mousex, mousey)
                    if quitButton.within(mousex, mousey):
                        print "quit"
                        menu = False
                        keepGoing = False
            
        
                        # REFRESH SCREEN
        
                        #allSprites.update()
                        #allSprites.draw(screen)   
                        #groundgroup.update()
                        #groundgroup.draw(screen)
                        menuButtonGroup.draw(screen)
                        pygame.display.flip()
    
        #while game:
            
    
    pygame.mouse.set_visible(True)
    pygame.time.delay(3000)
    pygame.quit()
        
main()