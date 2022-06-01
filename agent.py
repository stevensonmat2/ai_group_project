from cmath import inf
from re import S
from state_node import StateNode
import chess


class Agent:
    # creates agent with bool value. True for white, False for black
    def __init__(self, white: bool) -> None:
        self.is_white = white

    # wrapper to call miniMax. Returnsstyle="width:100%" border-top="1"p  > best action
    def calculate_move(self, board: chess.Board) -> str:
        max = True
        alpha = -inf
        beta = inf
        max_depth = 3
        action_value = []
        state_node = StateNode(board, self.is_white)
        action_value = self.miniMax(
            state_node, max, alpha, beta, max_depth, StateNode.get_state_value
        )
        return action_value[1]

    def calculate_move_attack(self, board: chess.Board):
        max = True
        alpha = -inf
        beta = inf
        max_depth = 3
        action_value = []
        state_node = StateNode(board, self.is_white)
        action_value = self.miniMax(
            state_node,
            max,
            alpha,
            beta,
            max_depth,
            StateNode.calculate_attack_state_value,
        )
        return action_value[1]

    # recursive call to miniMax
    # state: StateNode object
    # max: bool type. True for maximizing, False for minimizing
    # alpha: initialized as -inf
    # beta: initialized as +inf
    # depth: starts at max depth. Decreases every call until 0 is reached
    def miniMax(
        self, state: StateNode, max: bool, alpha, beta, depth, state_value
    ) -> list:
        action = None
        maxVal = None
        # base case. Returns current state value if max depth or terminal state is reached
        if depth <= 0 or state.terminal_state():
            return [state.state_value, action]
        # maximizing
        if max:
            maxVal = -inf
            for act in state.calculate_legal_moves():
                child = state.get_child(act)
                value = self.miniMax(child, False, alpha, beta, depth - 1, state_value)
                if value[0] >= maxVal:
                    maxVal = value[0]
                    action = act
                if value[0] >= beta:
                    return [maxVal, act]
                if value[0] > alpha:
                    alpha = value[0]
        # minimizing
        else:
            maxVal = inf
            for act in state.calculate_legal_moves():
                child = state.get_child(act)
                value = self.miniMax(child, True, alpha, beta, depth - 1, state_value)
                if value[0] <= maxVal:
                    maxVal = value[0]
                    action = act
                if value[0] <= alpha:
                    return [maxVal, action]
                if value[0] < beta:
                    beta = value[0]
        return [maxVal, action]
