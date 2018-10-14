from pygame.locals import USEREVENT

NAME_OF_THE_GAME = "Tetris"
BLOCK_SIZE = 30

def coord_in_px(coord):
    return (coord[0] * BLOCK_SIZE,
            coord[1] * BLOCK_SIZE)

DRAW_SPOTLIGHT = True # the spotlight is a guide the width of the player that extends to where it would fall.
STAGE_WIDTH = 9 # stage is where the game takes place.
STAGE_HEIGHT = 17
STAGE_MARGIN = (1,1)
BOARD_WIDTH= 5 # the board shows the next piece, the score and lines
BOARD_MARGIN = (STAGE_WIDTH+3, STAGE_MARGIN[1])
BOARD_CENTER_X = BOARD_MARGIN[0] + BOARD_WIDTH/2

PIECE_STAGE_STARTING_POSITION = (4,0)
NEXT_PIECE_POSITION = (BOARD_CENTER_X - 2, 13)
SCREEN_SIZE = (BOARD_MARGIN[0] + BOARD_WIDTH + 1   , STAGE_HEIGHT + 3)
STAGE_TOP_LEFT = STAGE_MARGIN
STAGE_BOTTOM_RIGHT = (STAGE_MARGIN[0] + STAGE_WIDTH, STAGE_MARGIN[1] + STAGE_HEIGHT)

BORDER_COLOR = (160,160,160)
BORDER_WIDTH = 1 #the borders surrounding areas

SPOTLIGHT_COLOR = (15,15,15)
TITLE_COLOR = (0, 64, 128)
TEXT_COLOR = (255,255,255)
GAME_OVER_TEXT_COLOR = (255,0,0)
PAUSE_TEXT_COLOR = (255,255,255)

FPS = 60
LOWER_PIECE_EVENT_ID = USEREVENT+1
