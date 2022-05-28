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
        self.state_value = self.get_state_value()
        self.successor_states = []
        self.legal_moves = []

    # calculates value of board configuration for given color player
    def calculate_state_value(self,color):
        state = self.board
        sum = 0
        sum += len(self.board.pieces(chess.KING,color)) * 4 
        sum += len(state.pieces(chess.QUEEN,color)) * 9
        sum += len(state.pieces(chess.BISHOP,color)) * 3
        sum += len(state.pieces(chess.ROOK,color)) * 5
        sum += len(state.pieces(chess.KNIGHT,color)) * 3
        sum += len(state.pieces(chess.PAWN,color))
    
        return sum

    # Value function returns the difference in of board values between players
    def get_state_value(self):
        if(self.is_white):
            return self.calculate_state_value(chess.WHITE) - self.calculate_state_value(chess.BLACK)
        return self.calculate_state_value(chess.BLACK) - self.calculate_state_value(chess.WHITE)
    
    def calculate_successor_states(self):
        pass

    # uses chess libray to calculate legal moves 
    # returns str list of legal moves
    def calculate_legal_moves(self):
        moveStr = []
        for x in list(self.board.legal_moves):
            if(self.board.is_legal(x)):
                moveStr.append(str(x))
        return moveStr  
    def get_child(self,action: str):
        childBoard = self.get_board()
        childBoard.push_san(action)         # 
        return StateNode(childBoard, self.is_white)
        
    def get_board(self):
        return self.board.copy()

    def terminal_state(self)->bool:
        over = self.board.is_game_over()
        return over


