from telnetlib import GA
from agent import Agent
from chess import Board


class Game:
    def __init__(self) -> None:
        self.board = Board()
       # self.agent = Agent(self.board)
       # self.score = 0

    def playAgentVsAgent(self):
        wPlayer = Agent(True)
        bPlayer = Agent(False)
        board = self.board
        move = 0
        

        while not self.board.is_game_over():
            wMove = wPlayer.calculate_move(board)
            print('white',wMove)
            board.push_san(wMove)
            print(board)
            print()
            if(board.is_game_over()):
                break
            bMove = bPlayer.calculate_move(board)
            print('black',bMove)
            board.push_san(bMove)
            print(board)
            print()
            move += 1
        print("GAME OVER") 
        print(board.outcome())
        print()

    def playHumanVsAgent(self):
        pass

    def agent_move(self):
        pass
