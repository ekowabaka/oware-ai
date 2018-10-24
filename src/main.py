from oware import Game
from agents import RandomAgent

game = Game(agents=(RandomAgent(), RandomAgent()))
game.run()
