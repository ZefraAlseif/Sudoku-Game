import pygame

from logic import Logic

WIDTH = HEIGHT = 576
DIMENSION = 9
MAX_FPS = 15
SQ_SIZE = WIDTH // DIMENSION
IMAGES = {}

def loadImages():
    pieces = ["n1","n2","n3","n4","n5","n6","n7","n8","n9"]
    for piece in pieces:
        IMAGES[piece] = pygame.transform.scale(pygame.image.load("Number_Sprites/"+piece+".png"),(SQ_SIZE,SQ_SIZE))

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    clock = pygame.time.Clock()
    screen.fill(pygame.Color("white"))
    game_state = Logic()
    loadImages()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        drawGameState(screen,game_state)
        clock.tick(MAX_FPS)
        pygame.display.flip()

def drawGameState(screen,game_state):
    drawBoard(screen)
    drawPieces(screen,game_state.board)

def drawBoard(screen):
    colors = [pygame.Color("gold"),pygame.Color("blue")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c) % 2)]
            pygame.draw.rect(screen,color,pygame.Rect(c * SQ_SIZE,r * SQ_SIZE,SQ_SIZE,SQ_SIZE))
            
def drawPieces(screen,board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece],pygame.Rect(c * SQ_SIZE,r * SQ_SIZE,SQ_SIZE,SQ_SIZE))

if __name__ == "__main__":
    main()