from oware.game import Game
from oware.agents import RandomAgent

game = Game(agents=(RandomAgent(), RandomAgent()))
game.run()
