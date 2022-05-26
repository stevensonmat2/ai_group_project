from agent import Agent
from board import Board


class Game:
    def __init__(self) -> None:
        self.board = Board()
        self.agent = Agent(self.board)
        self.score = 0

    def play(self):
        pass

    def player_move(self):
        pass

    def agent_move(self):
        pass
