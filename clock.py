import pygame
from constants import *

class Clock:
    def __init__(self, score):
        self.score = score
        self.clock = pygame.time.Clock()
        self.fps = FPS
        self.lower_piece_data = {n:int(48 - 2.4 * n) for n in range(21)}
        self.time_accumulated_to_lower_piece = 0

    lower_piece_every = property(lambda self: self.lower_piece_data[self.score.level] or 2)

    def tick(self):
        elapsed_time = self.clock.tick(self.fps)
        self.process_lower_piece(elapsed_time)

    def process_lower_piece(self, elapsed_time):
        self.time_accumulated_to_lower_piece += elapsed_time
        if self.time_accumulated_to_lower_piece >= self.lower_piece_every * 1000//FPS:
            self.time_accumulated_to_lower_piece = 0
            event_lower_piece = pygame.event.Event(LOWER_PIECE_EVENT_ID)
            pygame.event.post(event_lower_piece)