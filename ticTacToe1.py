import pygame
#since these are constant variables 
#I'm capitalizing them
WIDTH, HEIGHT= 400, 400 

BOARD = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
square_size = 133.33
spacing = 5

bg_color = (255, 255, 255)
BOARD.fill(bg_color)

#create the grid
for row in range(3):
    for col in range(3):
        x= col * (square_size+spacing)
        y = row * (square_size + spacing)

        #now drawing the square 
        pygame.draw.rect(BOARD, (0,0,0), (x, y, square_size, square_size))

pygame.display.update()
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
    BOARD.blit(oImage, (0,0))
    BOARD.blit(xImage, (0,0))


if __name__ == "__main__":
    main()