from constants import *
from random import choice
from copy import deepcopy


class Piece:
    """It's a piece of the game.
    contains a representation of it's shape and rotation.
    contains coordinates of it's components in the stage.
    contains capacity to move and rotate."""
    pieces = {
        "L":{"color" : (128, 94, 0),
             "offset": -1, # used to center the piece when it appears on screen
             "shape" : [[0,1,0],
                        [0,1,0],
                        [0,1,1]]},

        "J":{"color":  (0, 0, 128),
             "shape": [[0,1,0],
                       [0,1,0],
                       [1,1,0]]},
        
        "I":{"color" : (0, 128, 128),
             "offset": -1,
             "shape" : [[0,0,1,0,0],
                        [0,0,1,0,0],
                        [0,0,1,0,0],
                        [0,0,1,0,0]]},

        "S":{"color": (0, 128, 0),
             "shape": [[1,0,0],
                       [1,1,0],
                       [0,1,0]]},

        "Z":{"color": (128, 0, 0),
             "shape": [[0,1,0],
                       [1,1,0],
                       [1,0,0]]},

        "T": {"color": (128, 0, 128),
              "shape": [[0,0,0],
                        [1,1,1],
                        [0,1,0]]},

        "B": {"color": (128, 128, 0),
              "shape": [[1,1],
                        [1,1]]}}

    def __init__(self, piece_name = None, position = None):
        self.position = position or list(NEXT_PIECE_POSITION)
        self.name = piece_name or choice( list(self.pieces.keys()) )
        self.shape = deepcopy(self.pieces[self.name]["shape"])
        self.color = self.pieces[self.name]["color"]
        self.blocks = None
        self.update_blocks()
        self.offset_piece()

    def set_position(self, position):
        self.position = position
        self.update_blocks()
        self.offset_piece()

    def offset_piece(self):
        if "offset" in self.pieces[self.name].keys():
            self.move([self.pieces[self.name]["offset"], 0])

    def update_blocks(self):
        r = []
        for row_i, row in enumerate(self.shape):
            for col_i, block in enumerate(row):
                if block:
                    x = col_i + self.position[0] + STAGE_MARGIN[0]
                    y = row_i + self.position[1] + STAGE_MARGIN[1]
                    r.append([x, y])
        self.blocks = r
        if DRAW_SPOTLIGHT:
            self.blocks.sort()

    def rotate_ccw(self, update_blocks = True):
        r = []
        while self.shape:
            if self.shape[0]:
                r.append([])
                for row_i in range(len(self.shape)):
                    r[-1].append(self.shape[row_i][-1])
                    del self.shape[row_i][-1]
            else: self.shape = []
        self.shape = r
        if update_blocks:
            self.update_blocks()

    def rotate_cw(self):
        self.rotate_ccw(False)
        self.rotate_ccw(False)
        self.rotate_ccw()

    def move(self, coord):
        self.position[0] += coord[0]
        self.position[1] += coord[1]
        for block in self.blocks:
            block[0] += coord[0]
            block[1] += coord[1]

    def __iter__(self):
        for block in self.blocks:
            yield block

    def __getitem__(self, key):
        return self.blocks[key]

    def __delitem__(self, item):
        del self.blocks[item]

    def __len__(self):
        return len(self.blocks)

