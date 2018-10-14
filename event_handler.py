import pygame
from pygame.locals import *
from constants import *
from clock import Clock


class EventHandler:
    def __init__(self, game):
        pygame.key.set_repeat(1,160)
        self.game = game
        self.running = True # is the application running
        self.clock = Clock(self.game.score)

    def run(self):
        while self.running:
            self.clock.tick()
            self.handle_events()
            self.game.draw.draw_game()

    def tick(self):
        self.game.move_player( (0,1) )

    def handle_events(self):
        keys_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == KEYDOWN:
                if event.key in (K_PAUSE, K_RETURN, K_p):
                    if not self.game.game_over:
                        self.game.set_paused()
                    else:
                        self.__init__()
                
            if self.game.playing:
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.game.rotate_player()
                    elif event.key == K_DOWN:
                        self.game.move_player( (0,1) )
                    elif event.key == K_RIGHT:
                        self.game.move_player( (1,0) )
                    elif event.key == K_LEFT:
                        self.game.move_player( (-1,0) )
                    elif event.key == K_SPACE:
                        if keys_pressed[K_RIGHT]:
                            self.game.move_piece_to_limit((1,0))
                        elif keys_pressed[K_LEFT]:
                            self.game.move_piece_to_limit((-1,0))
                        else:
                            self.game.move_piece_to_limit((0,1))
                elif event.type == LOWER_PIECE_EVENT_ID:
                    self.game.move_player( (0,1) )
