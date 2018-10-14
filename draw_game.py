import pygame
from pygame.locals import *
from constants import *

class DrawGame:
    def __init__(self, game):
        pygame.init()
        self.screen = pygame.display.set_mode(coord_in_px(SCREEN_SIZE))
        pygame.display.set_caption(NAME_OF_THE_GAME)
        self.game = game
        self.font = pygame.font.SysFont("Arial", 22)

    def draw_game(self):
        self.screen.fill((0, 0, 0))
        self.draw_text()
        if DRAW_SPOTLIGHT:
            self.draw_spotlight()
        self.draw_pieces()
        self.draw_borders()
        pygame.display.flip()

    def render_text(self, text, position, color):
        txt_pos = list(coord_in_px(position))
        text = self.font.render(text, True, color)
        txt_pos[0] -= text.get_width()//2
        self.screen.blit(text, txt_pos)    

    def draw_txt_number_of_lines(self):
        self.render_text("LINES", (BOARD_CENTER_X, 1.5), TITLE_COLOR)
        self.render_text(str(self.game.score.lines), (BOARD_CENTER_X, 2.5), TEXT_COLOR)

    def draw_txt_level_number(self):
        self.render_text("LEVEL", (BOARD_CENTER_X, 4.5), TITLE_COLOR)
        self.render_text(str(self.game.score.level), (BOARD_CENTER_X, 5.5), TEXT_COLOR)

    def draw_txt_score(self):
        self.render_text("SCORE", (BOARD_CENTER_X, 7.5), TITLE_COLOR)
        self.render_text(str(self.game.score.score), (BOARD_CENTER_X, 8.5), TEXT_COLOR)
 
    def draw_txt_game_over(self):
        self.render_text("GAME OVER", (BOARD_CENTER_X, 10.5), GAME_OVER_TEXT_COLOR)

    def draw_txt_pause(self):
        self.render_text("PAUSE", (BOARD_CENTER_X, 10.5), PAUSE_TEXT_COLOR)

    
    def draw_txt_next_piece(self):
        self.render_text("NEXT PIECE", (BOARD_CENTER_X, 12.5), TITLE_COLOR)
    
    def draw_text(self):
        if self.game.game_over:
            self.draw_txt_game_over()
        if self.game.paused:
            self.draw_txt_pause()
        self.draw_txt_number_of_lines()
        self.draw_txt_score()
        self.draw_txt_level_number()
        self.draw_txt_next_piece()
        

    def draw_piece(self, piece):
        size_rect = (BLOCK_SIZE, BLOCK_SIZE)
        for block_pos in piece:
            pixel_pos = coord_in_px(block_pos)
            pygame.draw.rect(self.screen, piece.color, Rect(pixel_pos, size_rect))

    def draw_spotlight(self):
        top_left_x = coord_in_px(self.game.player.blocks[0])[0]
        top_left_y = coord_in_px(STAGE_TOP_LEFT)[1]
        top_left = (top_left_x, top_left_y)
        x_for_bottom_x = self.game.player.blocks[-1][0] - self.game.player.blocks[0][0]
        bottom_right_x = coord_in_px((x_for_bottom_x + STAGE_MARGIN[0], 1))[0]
        bottom_right_y = coord_in_px(STAGE_BOTTOM_RIGHT)[1]
        bottom_right = (bottom_right_x, bottom_right_y)
        pygame.draw.rect(self.screen, SPOTLIGHT_COLOR, Rect(top_left, bottom_right))

    def draw_pieces(self):
        self.draw_piece(self.game.player)
        self.draw_piece(self.game.next_piece)
        for piece in self.game.bottom_pieces:
            self.draw_piece(piece)

    def draw_borders(self):
        stage_rect = Rect(coord_in_px(STAGE_TOP_LEFT), coord_in_px(STAGE_BOTTOM_RIGHT))
        pygame.draw.rect(self.screen, BORDER_COLOR, stage_rect, BORDER_WIDTH)
        right_area_top_left = BOARD_MARGIN
        right_area_bottom_right = (BOARD_WIDTH, STAGE_HEIGHT+1)
        right_area_rect = Rect(coord_in_px(right_area_top_left), coord_in_px(right_area_bottom_right))
        pygame.draw.rect(self.screen, BORDER_COLOR, right_area_rect, BORDER_WIDTH)
