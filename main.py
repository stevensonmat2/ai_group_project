import argparse
from game import Game

parser = argparse.ArgumentParser()

parser.add_argument('--game', dest='game_type', type=str, default="a1vsa1",)

args = parser.parse_args()

game = Game()
game.run_simulation(args.game_type)
# game.playAgentVsAgent()
# game.playHumanVsAgent()
# game.play_agent_new()
