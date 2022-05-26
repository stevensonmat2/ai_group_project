from piece import Pawn, Knight, Bishop, Rook, Queen, King


class Board:
    def __init__(self) -> None:
        self.board = self.initialize_board()

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

    def move_piece(self, piece_xy: list, destination_xy: list) -> None:
        pass

    def legal_moves_white(self) -> list:
        pass

    def legal_moves_black(self) -> list:
        pass

    def move_is_legal(xy: list) -> bool:
        pass
