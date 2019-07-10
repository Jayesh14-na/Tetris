import pygame
from constants import *

class Clock:
    def __init__(self, game):
        self.game = game
        self.clock = pygame.time.Clock()
        self.fps = FPS
        self.time_accumulated_to_lower_piece = 0

    lower_piece_every = property(lambda self: self.game.lower_piece_data[self.game.score.level] or 2) # TODO: explain

    def tick(self):
        elapsed_time = self.clock.tick(self.fps)
        self.time_accumulated_to_lower_piece += elapsed_time
        if self.time_accumulated_to_lower_piece >= self.lower_piece_every * 1000//FPS:
            self.game.trigger_event_lower_piece()
            self.time_accumulated_to_lower_piece = 0
