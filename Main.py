from TexasHoldem import *
import time
import treys


Game = TexasHold(2, 100, graphics=False)
Game.add_players_to_game()
Game.deal_cards()
Game.draw_flop()
Game.add_river()
Game.add_middle()
Game.give_initial_chips()

Game.update_game_screen()
x = input("Done?")



