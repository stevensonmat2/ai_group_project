from board import Board
from state_node import StateNode

class Agent:
    def __init__(self, board: Board) -> None:
        self.board = board
        self.root_state = self.initialize_root_state()

    def initialize_root_state(self) -> StateNode:
        pass

    def calculate_move(self) -> list:
        pass
    