import pygame
#where I left off. 
#Need to figure out how to quit the user turn so then it 
#goes to the computer turn


#the font portion of the userTurn function
#Need to figure out that bug and then check to make sure it properly shows the message
#When someone clicks they need to remove the message.


#since these are constant variables 
#I'm capitalizing them
pygame.init()

WIDTH, HEIGHT= 400, 400 
FONT= 0
BOARD = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
square_size = 133.33
spacing = 5

moveList = [0] * 9
dictionary1 = {"0" : (0,0), "1" : (138.33, 0), "2": (276.66,0),
"3": (0, 138.33), "4" : (138.33, 138.33), "5" : (276.66, 138.33),
"6" : (0, 276.66), "7": (138.33, 276.66), "8": (276.66, 276.66)
}
bg_color = (255, 255, 255)
BOARD.fill(bg_color)

#create the grid
def createBoard():
    for row in range(3):
        for col in range(3):
            x= col * (square_size+spacing)
            y = row * (square_size + spacing)

        #now drawing the square 
            pygame.draw.rect(BOARD, (0,0,0), (x, y, square_size, square_size))
    pygame.display.flip()
#pygame.display.update()
#creating the images

def main():

    run = True 
    while run: 
       #in this line you want to loop through the events 
       # For example if a user quits this would pick it up
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                run = False
def chooseSymbol():
    #create the two symbols
    #ask the user to decide which symbol they want
    #assign that symbol to the user and assign the other symbol to the computer
    xImage= pygame.image.load('x.png')
    oImage = pygame.image.load('o.png')
    #resizing the image to fit the board
    xImage= pygame.transform.scale(xImage, (133,133))
    oImage = pygame.transform.scale(oImage, (133, 133))
    #BOARD.blit(oImage, (0,0))
    #BOARD.blit(xImage, (0,0))

    #now I need to figure out how to assign a value to a user 
    #ask the user to pick either x or o 
    USERSYMBOL = input("if you would like to be X please respond X, otherwise respond O:  ")
    if USERSYMBOL == 'x':
        USERSYMBOL = xImage
    else: 
        USERSYMBOL= oImage
    return USERSYMBOL
    

    #what is the condition for a user to be X or a user to be O? 
    #each time they click on the board then you would fill the board with whatever they picked

def promptUserTurn():
    #here you will want to ask the user to make a move
    #wherever the user clicks on the board then you will fill 
    #it in with an X or an O 

    font = pygame.font.Font('Arial.ttf', 27)
    message1 = "Make your move - click a square"
    message_surface = font.render(message1, True, (144, 238, 144))
    #dimensions 

    message_rect = message_surface.get_rect()

    #position in center of screen
    message_rect.center = (WIDTH //2 , HEIGHT//2)
    BOARD.blit(message_surface, message_rect)
    pygame.display.flip()
    #This code ensures that we do not reset the board until the user clicks
    waiting= True
    while waiting: 
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                waiting= False
    #fill removes the message from the board
    BOARD.fill((bg_color))
    pygame.display.flip()
    #Then I call the function that creates the board to reset the board
    createBoard()
#def userClicks():
    #run this function after showing the message to prompt the user to click 
    #use chatGPT to figure out how to record a click


    #now I need to figure out where the user clicks

def userTurn():
#there are 9 possible coordinate areas for a user to click on(each box)
#each box has a width of 
    USERSYMBOL = chooseSymbol()
    run= True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Get the position where the mouse was clicked
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]
                print("Clicked at:", pos)
                #now 9 if else conditions for the square clicked on
                if x < 138.33 and y < 138.33:
                    xImage= pygame.image.load('x.png')
                    xImage= pygame.transform.scale(xImage, (133,133))
                    BOARD.blit(USERSYMBOL, (0,0))
                    pygame.display.flip()
                    moveList[0]= 'U'
                    print("triggered 1")
                    return
                elif x < 276.66 and y < 138.33:
                    #xImage= pygame.image.load('x.png')
                    #xImage= pygame.transform.scale(xImage, (133,133))
                    BOARD.blit(USERSYMBOL, (138.33,0))
                    pygame.display.flip()
                    print("triggered 2")
                    moveList[1]= 'U'
                    return 
                elif x < 414.99 and y < 138.33:    
                    BOARD.blit(USERSYMBOL, (276.66,0))
                    pygame.display.flip()
                    print("triggered 3")
                    moveList[2]= 'U'
                    return 
                elif x < 138.33 and y < 276.66:
                    BOARD.blit(USERSYMBOL, (0,138.33))
                    pygame.display.flip()
                    print("triggered 4")
                    moveList[3]= 'U'
                    return
                elif x < 276.66 and y < 276.66:    
                    BOARD.blit(USERSYMBOL, (138.33,138.33))
                    pygame.display.flip()
                    print("triggered 5")
                    moveList[4]= 'U'
                    return 
                elif x < 414.99 and y < 276.66:    
                    BOARD.blit(USERSYMBOL, (276.66, 138.33))
                    pygame.display.flip()
                    print("triggered 6")
                    moveList[5]= 'U'
                    return 
                elif x < 138.33 and y < 414.99:    
                    BOARD.blit(USERSYMBOL, (0, 276.66))
                    pygame.display.flip()
                    print("triggered 7")
                    moveList[6]= 'U'
                    return 
                elif x < 276.66 and y < 414.99:    
                    BOARD.blit(USERSYMBOL, (138.33, 276.66))
                    pygame.display.flip()
                    print("triggered 8")
                    moveList[7]= 'U'
                    return 
                elif x < 414.99 and y < 414.99:    
                    BOARD.blit(USERSYMBOL, (276.66, 276.66))
                    pygame.display.flip()
                    print("triggered 9")
                    moveList[8]= 'U'
                    return
                #need to finish up the rest of the elif statements
def computerTurn1():
    #this function is responsible for the computer turn where it will determine the best 
    #or most optimal move for the computer
    #first move from the computer it can pick anywhere on the board
    #for i in moveList: 
    #    if i != 'U':
    #        loc1 = moveList.index(i)
    #        break
    oImage = pygame.image.load('o.png')
    oImage = pygame.transform.scale(oImage, (133, 133))
    loc1 = '4'
    BOARD.blit(oImage, (dictionary1[str(loc1)]))
    pygame.display.flip()
    
    #now the challenge I'm facing is how do i translate a 0-8 location 
    # to coordinates
    #put it into a dictionary? 


#pos keeps track of where the user clicked. If it is first quadrant it will be less than 
#each square has a width of 138.33 so that tells you which quadrant it is in. 

def computerTurn2():
    #now in this case the computer needs to first check if the other person has two in a row
    for i in moveList: 
        if i == 'U':
            loc1 = moveList.index(i)
            #condition for first row 
            if loc1 < 3:
                #first check down
                if moveList[loc1+3]== 'U' and moveList[loc1+6]!='U':
                    oImage = pygame.image.load('o.png')
                    oImage = pygame.transform.scale(oImage, (133, 133))
                    BOARD.blit(oImage, (dictionary1[str(loc1+6)]))
                    pygame.display.flip()
                #diagonal condition
                elif loc1 == 0 and moveList[loc1+4] == 'U' and moveList[loc1+8] != 'U':
                    oImage = pygame.image.load('o.png')
                    oImage = pygame.transform.scale(oImage, (133, 133))
                    BOARD.blit(oImage, (dictionary1[str(loc1+6)]))
                    pygame.display.flip()
                elif loc1 == 2 and moveList[loc1+2] == 'U' and moveList[loc1+4] != 'U':
                    oImage = pygame.image.load('o.png')
                    oImage = pygame.transform.scale(oImage, (133, 133))
                    BOARD.blit(oImage, (dictionary1[str(loc1+4)]))
                    pygame.display.flip()
                elif loc1 == 0: 
                    if moveList[loc1+4]== 'U' and moveList[loc1+8] != 'U':
                        oImage = pygame.image.load('o.png')
                        oImage = pygame.transform.scale(oImage, (133, 133))
                        BOARD.blit(oImage, (dictionary1[str(loc1+8)]))
                        pygame.display.flip()
                #now solve for horizontal 
                elif loc1 ==0 and moveList[loc1+1] == 'U' and moveList[loc1+2] != 'U':
                        oImage = pygame.image.load('o.png')
                        oImage = pygame.transform.scale(oImage, (133, 133))
                        BOARD.blit(oImage, (dictionary1[str(loc1+2)]))
                        pygame.display.flip()
                elif loc1 == 1 and moveList[loc1+1] == 'U' and moveList[loc1-1] != 'U':
                        oImage = pygame.image.load('o.png')
                        oImage = pygame.transform.scale(oImage, (133, 133))
                        BOARD.blit(oImage, (dictionary1[str(loc1-1)]))
                        pygame.display.flip()
                elif loc1 == 2 and moveList[loc1-1] == 'U' and moveList[loc1-2] != 'U':
                        oImage = pygame.image.load('o.png')
                        oImage = pygame.transform.scale(oImage, (133, 133))
                        BOARD.blit(oImage, (dictionary1[str(loc1-)]))
                        pygame.display.flip()
                #elif moveList[loc1+3] and moveList[loc1+6]:


 #this function is responsible for the computer turn where it will determine the best 
    #or most optimal move for the computer


createBoard()
promptUserTurn()
userTurn()
computerTurn1()
userTurn()
computerTurn2()

if __name__ == "__main__":
    main()