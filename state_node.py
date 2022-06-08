from cmath import pi
from re import A
import chess

# StateNode class represents states of a give chess board and
# the value of that state for the player.
# The chess library is used to:
#   create a chess board configuration
#   generate a list of legal moves for the current configuration
#   make a move with a given action and update board configuration
#   detect stalemate, checkmates and other game ending configurations


class StateNode:
    def __init__(self, board: chess.Board, white: bool) -> None:
        self.board = board
        self.is_white = white
        self.color = chess.WHITE if self.is_white else chess.BLACK
        self.opp_color = chess.BLACK if self.is_white else chess.WHITE
        # self.state_value = self.get_state_value()
        # self.state_value_attacks = self.calculate_attack_state_value()
        self.successor_states = []
        self.legal_moves = []

    # calculates value of board configuration for given color player
    def calculate_state_value(self, color):
        state = self.board
        sum = 0
        sum += len(self.board.pieces(chess.KING, color)) * 4
        sum += len(state.pieces(chess.QUEEN, color)) * 9
        sum += len(state.pieces(chess.BISHOP, color)) * 3
        sum += len(state.pieces(chess.ROOK, color)) * 5
        sum += len(state.pieces(chess.KNIGHT, color)) * 3
        sum += len(state.pieces(chess.PAWN, color))

        return sum

    # Value function returns the difference in of board values between players
    def get_state_value(self):
        agent_color = chess.WHITE if self.is_white else chess.BLACK
        opponent_color = chess.BLACK if self.is_white else chess.WHITE
        return self.calculate_state_value(agent_color) - self.calculate_state_value(
            opponent_color
        )

    def calculate_successor_states(self):
        pass

    def calculate_attack_state_value(self):
        moves = self.board.legal_moves
        # pieces = self.board.pieces(color=chess.WHITE if self.is_white else chess.BLACK)
        # print(pieces)
        # state_value = self.state_value
        state_value = self.get_state_value()
        # for square in self.board.checkers():
        #     piece = self.board.piece_at(square)
        #     if piece and piece.color == self.color:
        #         state_value += 50

        king = self.board.pieces(chess.KING, self.color)
        king_square = chess.E1 if self.is_white else chess.E8
        if king != self.board.piece_at(king_square):
            state_value -= 100
        if self.board.is_checkmate():
            state_value += 1000

        if self.board.is_seventyfive_moves():
            state_value -= 1000

        if self.board.is_fivefold_repetition():
            state_value -= 1000
        # state_value += len(self.board.checkers())
        # state_value -= 20 if self.board.is_check() else 0
        # print(state_value)
        # center_squares = [chess.E4, chess.E5, chess.D4, chess.D5]
        # for square in center_squares:
        #     piece = self.board.piece_at(square)
        #     if piece and piece.color == self.color:
        #         state_value += 4

            # if self.board.is_attacked_by(self.opp_color, square):
            #     state_value -= 4
        # for move in moves:
        #     state_value += 4 if self.board.gives_check(move) else 0
        #     state_value += 2 if self.board.is_capture(move) else 0
            # state_value += 1 if move.to_square in center_squares else 0

        return state_value

    # uses chess libray to calculate legal moves
    # returns str list of legal moves
    def calculate_legal_moves(self):
        moveStr = []
        for x in list(self.board.legal_moves):
            if self.board.is_legal(x):
                moveStr.append(str(x))
        return moveStr

    def get_child(self, action: str):
        childBoard = self.get_board()
        childBoard.push_san(action)  #
        return StateNode(childBoard, self.is_white)

    def get_board(self):
        return self.board.copy()

    def terminal_state(self) -> bool:
        over = self.board.is_game_over()
        return over
