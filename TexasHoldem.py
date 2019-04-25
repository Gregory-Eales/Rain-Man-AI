from random import shuffle
from GUI import PokerScreen
import random
import pygame
import treys

class Deck(object):

    def __init__(self):
        self.rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.suit = ["Diamonds", "Clubs", "Hearts", "Spades"]
        self.deck_values = self.create_values()
        self.deck_order = self.reset_deck_order()

    # Creates values for each card
    def create_values(self):
        deck = {}
        for i in range(len(self.rank)):
            for j in range(len(self.suit)):
                deck[self.rank[i] + " of " + self.suit[j]] = [i, j]
        return deck

    # Initiates the deck order
    def reset_deck_order(self):
        deck_order = []
        for i in range(len(self.rank)):
            for j in range(len(self.suit)):
                deck_order.append(self.rank[i] + " of " + self.suit[j])
        return deck_order

    # Shuffles the deck order
    def shuffle_order(self):
        self.deck_order = shuffle(self.deck_order)


class Player(object):

    def __init__(self):
        self.hand = []
        self.chips = 0


class TexasHold(object):

    def __init__(self, num_players, starting_chips, graphics=True):
        # Number of players
        self.num_players = num_players
        # Creates player objects
        self.players = self.add_players_to_game()
        # Creates deck object
        self.deck = Deck()
        # Created Board
        self.board = []
        # Number of chips each player starts with
        self.starting_chips = starting_chips
        # Number of chips in the pot
        self.pot = 0
        # Keeps track of whos in the game
        self.in_game = []
        # Keeps track of who is in the current round
        self.in_round = []
        # Amount player must give to check
        self.big_blind = 0
        # Card ranking dictionary
        self.card_ranks = {"Royal Flush": 10, "Straight Flush": 9, "Four of a Kind": 8, "Full House": 7,
                           "Flush": 6, "Straight": 5, "Three of a Kind": 4, "Two Pair": 3, "Pair": 2, "High Card": 1}
        # Initiates game ante to zero
        self.ante = 0
        # Initiates Graphics
        self.graphics = PokerScreen()
        self.evaluator = treys.Evaluator()
        self.Card = treys.Card()

    # Runs the game in a closed loop
    def main_play(self, chips):
        playing = True
        self.players = self.add_players_to_game()
        self.give_initial_chips()
        while playing:
            self.add_players_to_round()
            self.deck = Deck()
            self.deal_cards()
            # Start initial betting round
            for i in self.in_round:
                self.player_decision(i)
            playing = False

    def player_decision(self, player):
        print("Your Cards Are: ", str(self.players[player].hand[0]), " ", str(self.players[player].hand[1]))
        print("The pot is:", self.pot)
        print("The field cards are: ", self.board)
        decision = input("What would you like to do: Raise/Call/Fold")

        if decision == "Raise":
            amount_check = True
            while amount_check:
                amount = input("How much would you like to bet:")
                if amount < self.players[player].chips:
                    amount_check = False
                if amount > self.players[player].chips:
                    print("You do not have enough chips to bet that amount, please try again")

            self.bet(player, int(amount))

        if decision == "Call":
            self.check(player)

        if decision == "Fold":
            self.fold(player)

    # Creates a Player() object for each player
    def add_players_to_game(self):
        self.in_game = []
        players = {}
        for i in range(self.num_players):
            players["Player" + str(i)] = Player()
            self.in_game.append("Player" + str(i))
        return players

    def add_players_to_round(self):
        for i in self.in_game:
            self.in_round.append("Player" + str(i))

    # Gives each player two hole cards from the deck
    def deal_cards(self):
        print(self.players)
        for i in range(self.num_players):
            for k in range(2):
                picked_card = random.randint(0, (len(self.deck.deck_order)-1))
                self.players["Player"+str(i)].hand.append(self.deck.deck_order[picked_card])
                self.deck.deck_order.remove(self.deck.deck_order[picked_card])

    # Adds three cards to the board
    def draw_flop(self):
        for i in range(3):
            picked_card = random.randint(0, len(self.deck.deck_order)-1)
            self.board.append(self.deck.deck_order[picked_card])
            self.deck.deck_order.remove(self.deck.deck_order[picked_card])

    # Adds the middle card to the board
    def add_middle(self):
        picked_card = random.randint(0, len(self.deck.deck_order)-1)
        self.board.append(self.deck.deck_order[picked_card])
        self.deck.deck_order.remove(self.deck.deck_order[picked_card])

    # Adds the river card to the board
    def add_river(self):
        picked_card = random.randint(0, len(self.deck.deck_order)-1)
        self.board.append(self.deck.deck_order[picked_card])
        self.deck.deck_order.remove(self.deck.deck_order[picked_card])

    # Player bets/raises
    def bet(self, player, amount=10):
        self.players[player].chips = self.players[player].chips - amount
        self.pot = self.pot + amount
        self.big_blind = amount

    # Player folds
    def fold(self, player):
        self.in_game.remove(player)

    # Player checks
    def check(self, player):
        self.players[player].chips = self.players[player].chips - self.big_blind
        self.pot = self.pot + self.big_blind

    # Removes player from the game
    def remove_player(self, player):
        del self.players[player]

    # Resets the game
    def reset_game(self, starting_chips, num_players ):
        # Number of players
        self.num_players = num_players
        # Creates player objects
        self.in_round = self.add_players_to_round()
        for i in self.in_round:
            self.players[i].hand = []
        # Creates deck object
        self.deck = Deck()
        # Created Board
        self.board = []
        # Number of chips each player starts with
        self.starting_chips = starting_chips
        # Number of chips in the pot
        self.pot = 0

    def decide_winner(self):
        scores_dict = {}
        scores_player = {}
        scores = []
        for player in self.in_game:
            scores_dict[self.highest_card_score(player)] = player
            scores_player[player] = self.highest_card_score(player)
            scores.append(self.highest_card_score(player))
        scores = sorted(scores)
        if scores.count(scores[-1])>1:
            drawers = []
            for player in self.in_game:
                if scores_player[player] == scores[-1]:
                    drawers.append(player)
            winner = self.resolve_draw(drawers)
        if scores.count(scores[-1])==1:
            winner = scores_dict[scores[-1]]

        return winner

    # Checks the highest set of cards a player has
    def highest_card_score(self, player):
        highest_score = 1
        hand = self.players[player].hand
        total_cards = hand+self.board

        # checks for type of pairs
        if highest_score < self.check_pairs(total_cards):
            highest_score = self.check_pairs(total_cards)

        # checks for a straight, flush, or combination
            if highest_score < self.check_straight_flush(total_cards):
                highest_score = self.check_straight_flush(total_cards)

        return highest_score

    # Checks for the number of pairs
    def check_pairs(self, cards):
        pair_type = None
        three_kind = 0
        pairs = []
        for card in cards:
            amount = cards.count(card)

            if amount == 2:
                pairs.append(card)
                for i in range(2):
                    cards.remove(card)

            if amount == 3:
                pair_type = "Three of a Kind"
                three_kind = three_kind + 1
                for i in range(3):
                    cards.remove(card)

            if amount == 4:
                pair_type = "Four of a Kind"

            if len(pairs) == 2:
                pair_type = "Two Pair"

            if len(pairs) == 1:
                pair_type = "Pair"

            if three_kind == 1 and len(pairs) == 1:
                pair_type = "Full House"

        return self.card_ranks[pair_type]

    # Checks for a flush, straight, or combination
    def check_straight_flush(self, cards):
        straight = False
        flush = False
        int_list = []
        value = None
        for j in range(8):
            ints = []
            for i in range(5):
                ints.append(i+j)
            int_list.append(ints)
        card_ranks = []
        for i in cards:
            card_ranks.append(self.deck.deck_values[i][0])
        card_ranks = sorted(card_ranks)

        for i in int_list:
            if i == card_ranks:
                straight = True
                break

        card_suits = []

        for i in cards:
            card_suits.append(self.deck.deck_values[i][1])
        card_suits = sorted(card_suits)

        if card_suits.count(card_suits[0]) == 5:
            flush = True

        if straight:
            value = self.card_ranks["Straight"]

        if flush:
            value = self.card_ranks["Flush"]

        if straight and flush:
            value = self.card_ranks["Straight Flush"]

        if card_ranks == [8, 9, 10, 11, 12] and flush:
            value = self.card_ranks["Royal Flush"]

        return value

    # Decides a Draw
    def resolve_draw(self, players):
        player_highcard = {}
        highest_values = []
        for player in players:
            hand = self.players[player].hand
            total_cards = hand + self.board
            print(total_cards)
            card_rank_values = []
            for card in total_cards:
                card_rank_values.append(self.deck.deck_values[card][0])
            card_rank_values = sorted(card_rank_values)
            highest_values.append(card_rank_values[-1])
            player_highcard[card_rank_values[-1]] = player
        highest_values = sorted(highest_values)
        return player_highcard[highest_values[-1]]

    def initiate_graphics(self):
        pass

    def update_game_screen(self):

        # Delete current graphics options

        # Rewrite board cards

        # Rewrite cards
        for i in range(self.num_players):
            self.graphics.update_player_cards(self.players["Player"+str(i)].hand, "Player"+str(i))
        for i in range(self.num_players, 6):
            self.graphics.update_player_cards(["Back of Card", "Back of Card"], "Player" + str(i))

        print(self.board)
        if self.board != []:
            self.graphics.update_board_cards(self.board, "Board")

        # Rewrite text
        self.graphics.draw_stat_borders()
        player_scores = []
        for i in range(self.num_players):
            player_scores.append(self.players["Player"+str(i)].chips)
        self.graphics.update_player_scores(player_scores, self.pot, self.num_players)
        pygame.display.flip()

    def give_initial_chips(self):
        for i in range(self.num_players):
            self.players["Player"+str(i)].chips = self.starting_chips

    def calculate_odds(self, player):
        board = [self.Card.new('Qs'), self.Card.new('Th')]
        hand = None
        odds = (7642 - self.evaluator.evaluate(board, hand))/7642
        return odds
