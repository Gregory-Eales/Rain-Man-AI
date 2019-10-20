import time
from random import shuffle

import torch
import numpy

class Card(object):

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return "{} of {}".format(self.rank, self.suit)

class Deck(object):

    def __init__(self):
        self.suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
        self.ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack",
         "Queen", "King", "Ace"]

        self.cards = []
        self.populate_deck()
        self.shuffle()

    def populate_deck(self):
        for suit in self.suits:
            for rank in self.ranks:
                self.cards.append(Card(suit, rank))

    def reset(self):
        self.cards = []
        self.populate_deck

    def shuffle(self):
        shuffle(self.cards)


    def draw_card(self):
        card = self.cards[0]
        self.cards.remove(card)
        return card

class Player(object):

    def __init__(self):

        self.chips = 0
        self.cards = []

    def add_cards(self, card1, card2):
        self.cards.append(card1)
        self.cards.append(card2)

    def reset_cards(self):
        self.cards = []

    def __str__(self):
        card1 = self.cards[0].__str__()
        card2 = self.cards[1].__str__()
        return "Chips:{}, Cards: {}, {}".format(self.chips, card1, card2)

class TexasHoldem(object):

    def __init__(self, num_players=2):

        self.num_players = num_players
        self.players = {}
        self.community_cards = []
        self.pot = 0
        self.deck = Deck()


        # game logic
        self.is_betting = True
        self.dealer = "P1"

        self.initialize_players()


    def step(self, action):
        """
         actions: bet:-1, fold:-2, raise:[0, 1]
         raise: between 0 and 1, represent percentage of chips to be raised

        """
        # return possible actions [bet, fold, raise]
        # returns next player_id, cards, community cards, all player chips, pot
        pass

    def initialize_players(self):

        for player in range(self.num_players):
            self.players["P"+str(player)] = Player()

    def draw_card(self):
        return self.deck.draw_card()

    def reset_deck(self):
        self.deck.reset()

    def remove_player_cards(self):

        for i in range(self.num_players):
            self.players["P"+str(i)].reset_cards

    def reset_players(self):
        self.players = {}
        for player in range(self.num_players):
            self.players["P"+str(player)] = Player()

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

def main():
    a = Deck()
    card = a.draw_card()


if __name__ == "__main__":
    main()
