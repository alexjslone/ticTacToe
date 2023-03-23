import pygame
#where I left off. Working on the bug that I got when I tried to run 
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
createBoard()
xImage= pygame.image.load('x.png')
oImage = pygame.image.load('o.png')

#need to resize the image to fit the square 
xImage= pygame.transform.scale(xImage, (133,133))
oImage = pygame.transform.scale(oImage, (133, 133))

BOARD.blit(oImage, (0,0))
BOARD.blit(xImage, (0,0))
pygame.display.update()



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
    xImage= pygame.transform.scale(xImage, (133,133))
    oImage = pygame.transform.scale(oImage, (133, 133))
    BOARD.blit(oImage, (0,0))
    BOARD.blit(xImage, (0,0))

    #now I need to figure out how to assign a value to a user 
    #ask the user to pick either x or o 
    userSymbol = input("if you would like to be X please respond X, otherwise respond O")
    #what is the condition for a user to be X or a user to be O? 
    #each time they click on the board then you would fill the board with whatever they picked

def userTurn():
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
    waiting= True
    while waiting: 
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                waiting= False
    BOARD.fill((bg_color))
    pygame.display.flip()
    createBoard()
    #pygame.draw.rect(BOARD, (0, 0, 0), message_rect)
    #pygame.draw.rect(BOARD, (0,0,0), (x, y, square_size, square_size))
    #pygame.display.flip()
#def userClicks():
    #run this function after showing the message to prompt the user to click 
    #use chatGPT to figure out how to record a click


    #now I need to figure out where the user clicks

userTurn()

if __name__ == "__main__":
    main()