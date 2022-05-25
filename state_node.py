from board import Board


class StateNode:
    def __init__(self, board: Board) -> None:
        self.board = board
        self.state_value = self.calculate_state_value()
        self.successor_states = []
        self.legal_moves = []

    def calculate_state_value(self):
        pass

    def calculate_successor_states(self):
        pass

    def calculate_legal_moves(self):
        pass
