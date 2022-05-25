from abc import ABC, abstractmethod

class Piece(ABC):
    """
    Abstract base class
    """
    def __init__(self) -> None:
        self.name = None
        self.value = 0
        self.max_move_spaces = 0
        self.move_vectors = []
        self.attack_vectors = []

    def __str__(self) -> str:
        return self.name

    @abstractmethod
    def is_legal_move(self, xy: list) -> bool:
        pass


class Pawn(Piece):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Pawn"
        self.value = 1
        self.max_move_spaces = 2
        self.move_vectors = [(0, 1), (0, 2)]
        self.attack_vectors = [(1, 1), (-1, 1)]
        self.has_moved = False # for en passant


class Knight(Piece):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Knight"
        self.value = 3
        self.max_move_spaces = 1
        self.move_vectors = [(-2, 1), (-1, 2), (1, 2), (2, 1)]
        self.attack_vectors = self.move_vectors


class Bishop(Piece):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Bishop"
        self.value = 3
        self.max_move_spaces = 8
        self.move_vectors = [(1, 1), (-1, -1), (-1, 1), (1, -1)]
        self.attack_vectors = self.move_vectors


class Rook(Piece):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Rook"
        self.value = 5
        self.max_move_spaces = 8
        self.move_vectors = [(0, 1), (-1, 0), (1, 0), (-1, 0)]
        self.attack_vectors = self.move_vectors


class Queen(Piece):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Queen"
        self.value = 9
        self.max_move_spaces = 8
        self.move_vectors = [(1, 1), (-1, -1), (-1, 1), (1, -1), (0, 1), (-1, 0), (1, 0), (-1, 0)]
        self.attack_vectors = self.move_vectors


class King(Piece):
    def __init__(self) -> None:
        super().__init__()
        self.name = "King"
        self.value = 100
        self.max_move_spaces = 1
        self.move_vectors = [(1, 1), (-1, -1), (-1, 1), (1, -1), (0, 1), (-1, 0), (1, 0), (-1, 0)]
        self.attack_vectors = self.move_vectors
