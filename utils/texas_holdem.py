import time

import torch
import numpy

class Card(object):

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

class Deck(object):

    def __init__(self):
        self.suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
        self.ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack",
         "Queen", "King", "Ace"]

    def reset(self):
        pass

    def shuffle(self):
        pass

class Player(self):

    def __init__(self):

        self.chips = 0
        self.cards = 0

class TexasHoldem(object):

    def __init__(self, num_players=2):

        self.num_players = num_players

        self.community_cards = []
        self.pot = 0


    def draw_card(self):
        pass

    def reset_deck(self):
        pass

    def step(self, action):
        # actions: bet, raise, fold

        # returns next player_id, cards, community cards, all player chips, pot
        pass

    def reset(self, action):
        pass

    def check_highcard(self):
        pass

    def check_pair(self):
        pass

    def check_two_pair(self):
        pass

    def check_three_kind(self):
        pass

    def check_straight(self):
        pass

    def check_flush(self):
        pass

    def check_full_house(self):
        pass

    def check_four_kind(self):
        pass

    def check_straight_flush(self):
        pass

    def check_royal_flush(self):
        pass
