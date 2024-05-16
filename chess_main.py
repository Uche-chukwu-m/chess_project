#main driver file. responsible for handling user input and displaying the current gamestate

import pygame as p
import chessEngine

WIDTH = HEIGHT = 400
DIMENSION = 8 #DIMENSIONS OF A CHESS BOARD ARE 8X8
SQ_SIZE = HEIGHT//DIMENSION
MAX_FPS = 15 #FOR ANIMATIONS LATER ON
IMAGES = {}
'''
Initialize a global directory of images. This will be called exactly once in the main
'''
def loadImages():
    pieces = ["bR","bN","bB","bQ","bK","bB","bN","bR","bp","wR","wN","wB","wQ","wK","wB","wN","wR","wp"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("Images/"+piece +".png"), (SQ_SIZE,SQ_SIZE))
        #note: we can access an image by saying 'IMAGES['wp']'

'''
This is the main driver for our code. It will handle user input and update it in the graphics
'''

def main():
    p.init()
    screen = p.display.set_mode((WIDTH,HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = chessEngine.GameState()
    
    loadImages()#only once
    running = True
    sqSelected = () #no square is selected initially. it will keep track of the users last clicks as a tuple (row, col)
    playerClicks = [] #keep tracks of player clicks in form of two tuples.[(start_row,start_col),(end_row, end_col)]
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos() #(x,y) location of mouse
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                if sqSelected == (row,col): #if user doubleclicks the same square
                    sqSelected = () #deselect the square
                    playerClicks = [] #empty the player clicks
                else:
                    sqSelected = (row,col)
                    playerClicks.append(sqSelected)
                
                if len(playerClicks) == 2: #after the second click
                    move = chessEngine.Move(playerClicks[0],playerClicks[1],gs.board)
                    print(move.getChessNotation())
                    gs.makeMove(move)
                    sqSelected = () #resets user clicks
                    playerClicks = []

        drawGameState(screen,gs)
        clock .tick(MAX_FPS)
        p.display.flip()


'''
responsible for all graphics within a current gamestate
'''

def drawGameState(screen,gs):
    drawBoard(screen) #draw squares on the board
    #add in piece highlighting or move suggestions (later)
    drawPieces(screen, gs.board) #draw pieces on top of those squares

'''
draw squares on the board
'''
def drawBoard(screen):
    colors = [p.Color("white"),p.Color("grey")]
    for r in range(DIMENSION):
        for c in range (DIMENSION):
            color = colors[((r+c)%2)]
            p.draw.rect(screen, color,p.Rect(c*SQ_SIZE,r*SQ_SIZE,SQ_SIZE,SQ_SIZE))



'''
Draw the pieces on the poard using the current GameState.board
'''
def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range (DIMENSION):
            piece = board[r][c]
            if piece != '--': #if piece is not an empty square
                screen.blit(IMAGES[piece],p.Rect(c*SQ_SIZE,r*SQ_SIZE,SQ_SIZE,SQ_SIZE))

if __name__ == "__main__":
    main()



