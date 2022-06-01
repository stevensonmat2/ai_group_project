from telnetlib import GA
from agent import Agent
from chess import Board
from chess import Move


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
            print("white", wMove)
            board.push_san(wMove)
            print(board)
            print()
            if board.is_game_over():
                break
            bMove = bPlayer.calculate_move(board)
            print("black", bMove)
            board.push_san(bMove)
            print(board)
            print()
            move += 1
        print("GAME OVER")
        print(board.outcome())
        print()

    def playHumanVsAgent(self):
        bPlayer = Agent(False)
        board = self.board
        move = 0
        print(board)
        print()
        print("Your move... (ex: a2a4)")
        print()

        while not self.board.is_game_over():
            wMove = input()
            print("white", wMove)
            while Move.from_uci(wMove) not in board.legal_moves:
                print("Invalid move, try again")
                wMove = input()
            board.push_san(wMove)
            print(board)
            print()
            if board.is_game_over():
                break
            bMove = bPlayer.calculate_move(board)
            print("black", bMove)
            board.push_san(bMove)
            print(board)
            print()
            move += 1
        print("GAME OVER")
        print(board.outcome())
        print()

    def agent_move(self):
        pass

    def play_agent_new(self):
        white_player = Agent(True)
        black_player = Agent(False)
        board = self.board
        move = 0

        while not self.board.is_game_over():
            white_move = white_player.calculate_move_attack(board)
            print("white", white_move)
            board.push_san(white_move)
            print(board)
            print()
            if board.is_game_over():
                break
            black_move = black_player.calculate_move(board)
            print("black", black_move)
            board.push_san(black_move)
            print(board)
            print()
            move += 1
        print("GAME OVER")
        print(board.outcome())
        print()
