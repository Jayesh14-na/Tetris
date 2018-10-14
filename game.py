from constants import *
from piece import Piece
from draw_game import DrawGame
from score import Score
from event_handler import EventHandler
from bottom_pieces import BottomPieces

class Game:
    """Manages the interaction between the player and movement, margins, lower pieces, states, score, next piece and level."""
    def __init__(self, piece_name = None):
        self.playing = True
        self.paused = False
        self.game_over = False
        self.running = True
        self.player = Piece(piece_name, list(PIECE_STAGE_STARTING_POSITION))
        self.player.offset_piece()
        self.next_piece = Piece()
        self.score = Score()
        self.bottom_pieces = BottomPieces(self)
        self.draw = DrawGame(self)
        self.event_handler = EventHandler(self)
    
    def run(self):
        while self.running:
            self.event_handler.clock.tick()
            self.event_handler.handle_events()
            self.draw.draw_game()

    def set_paused(self, pause = None):
        self.paused = pause if pause != None else not self.paused
        self.playing = not self.paused and not self.game_over

    def player_oversteps_bottom_pieces(self):
        for coord in self.player.blocks:
            if coord in self.bottom_pieces:
                return True
        return False

    def player_oversteps_border(self):
        for coord in self.player.blocks:
            if not (STAGE_MARGIN[0] <= coord[0] <= STAGE_WIDTH+STAGE_MARGIN[0]) or \
               not (coord[1] <= STAGE_HEIGHT+STAGE_MARGIN[1]):
                return True
        return False

    def player_oversteps(self):
        return self.player_oversteps_border() or self.player_oversteps_bottom_pieces()

    def move_player(self, coord):
        self.player.move(coord)
        if self.player_oversteps():
            self.player.move([coord[0]*-1, coord[1]*-1])
            if coord[1]:
                self.change_player()

    def rotate_player(self):
        self.player.rotate_cw()
        if self.player_oversteps():
            self.player.rotate_ccw()

    def change_player(self):
        self.bottom_pieces.append(self.player)
        self.player = self.next_piece
        self.player.set_position(list(PIECE_STAGE_STARTING_POSITION))
        self.next_piece = Piece()
        self.bottom_pieces.check_rows()
        if self.player_oversteps_bottom_pieces():
            self.playing = False
            self.game_over = True

    def bottom_pieces_call(self, number):
        """BottomPieces uses this method when it clears lines"""
        self.score.add_lines(number)

    def move_piece_to_limit(self, coord):
        """It lowers the piece to the bottom in one movement,
        or it moves it to the right or left until a limit is met"""
        def has_advanced(previous_pos, current_pos):
            if   coord[0] > 0:
                return previous_pos[0] < current_pos[0]
            elif coord[0] < 0:
                return previous_pos[0] > current_pos[0]
            elif coord[1] > 0:
                return previous_pos[1] < current_pos[1]
            elif coord[1] < 0:
                return previous_pos[1] > current_pos[1]
            elif previous_pos == current_pos:
                return False

        keep_moving = True
        while keep_moving:
            old_position = self.player.position[:]
            self.move_player(coord)
            if not has_advanced(old_position, self.player.position):
                keep_moving = False

