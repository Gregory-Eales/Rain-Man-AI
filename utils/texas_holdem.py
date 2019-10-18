import time

import torch
import numpy

class Card(object):

    def __init__(self):
        pass

class Deck(object):

    def __init__(self):
        pass

    def reset(self):
        pass

class TexasHoldem(object):

    def __init__(self, num_players=2, starting_chips=1000):

        self.community_cards = []
        self.pot = 0
        self.num_players = num_players
        self.starting_chips = starting_chips
        self.suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
        self.kinds = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack",
         "Queen", "King", "Ace"]

    def step(self, action):
        # actions: bet, raise, fold
        pass

    def reset(self, action):
        pass
