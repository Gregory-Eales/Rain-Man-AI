from TexasHoldem import *

Game = TexasHold(5, 100)

Game.draw_flop()
Game.add_middle()
Game.add_river()

print(Game.check_pairs(["two", "two", "Three", "Three", "Three"]))