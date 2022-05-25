from piece import Pawn, Knight, Bishop, Rook, Queen, King

class Board:
    def __init__(self) -> None:
        self.board = self.initialize_board()
        self.legal_moves_black = []
        self.legal_moves_white = []
        self.update_legal_moves()

    def initialize_board(self):
        piece_counts = {
            "p": 8,
            "n": 2,
            "b": 2,
            "r": 2,
            "q": 1,
            "k": 1,
        }
        pass

    def update_board(self, xy: list) -> None:
        pass

    def update_legal_moves(self) -> None:
        pass