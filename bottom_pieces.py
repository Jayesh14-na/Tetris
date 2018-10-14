from constants import *


class BottomPieces(list):
    def __init__(self, game):
        super(BottomPieces, self).__init__()
        self.game = game

    def __contains__(self, element):
        if super(BottomPieces, self).__contains__(element):
            return True
        else:
            for piece in self:
                if element in piece:
                    return True
        return False

    def check_rows(self):
        blocks_deleated = 0
        acc = {}
        for piece in self:
            for block in piece:
                if block[1] not in acc.keys():
                    acc[block[1]] = []
                acc[block[1]].append(block[0])

        for key, value in sorted(acc.items()):
            if len(value) == STAGE_WIDTH+1:
                blocks_deleated += self.delete_row(key)

        lines_cleared = blocks_deleated // (STAGE_WIDTH + 1)
        if lines_cleared:
            self.game.bottom_pieces_call(lines_cleared)

    def delete_row(self, row):
        blocks_deleated = 0
        for piece_index in range(len(self)-1, -1, -1):
            for box_index in range(len(self[piece_index])-1,-1, -1):
                if self[piece_index][box_index][1] == row:
                    del self[piece_index][box_index]
                    blocks_deleated += 1
                    if not len(self[piece_index]):
                        del self[piece_index]
                elif self[piece_index][box_index][1] < row:
                    self[piece_index][box_index][1] += 1
        return blocks_deleated
