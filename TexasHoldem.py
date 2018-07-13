from random import shuffle
import random


class Deck(object):

    def __init__(self):
        self.rank = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.suit = ["Diamonds", "Clubs", "Hearts", "Spades"]
        self.deck_values = self.create_values()
        self.deck_order = self.reset_deck_order()

    # Creates values for each card
    def create_values(self):
        deck = {}
        for i in range(14):
            for j in range(4):
                deck[self.rank[i] + " of " + self.suit[j]] = [i, j]
        return deck

    # Initiates the deck order
    def reset_deck_order(self):
        deck_order = []
        for i in range(14):
            for j in range(4):
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

    def __init__(self, num_players, starting_chips):
        # Number of players
        self.num_players = num_players
        # Creates player objects
        self.players = self.add_players()
        # Creates deck object
        self.deck = Deck()
        # Created Board
        self.board = []
        # Number of chips each player starts with
        self.starting_chips = starting_chips
        # Number of chips in the pot
        self.pot = 0
        # Keeps track of whos in the current round
        self.in_game = []
        # Amount player must give to check
        self.big_blind = 0
        # Card ranking dictionary
        self.card_ranks = {"Royal Flush":10, "Straight Flush":9, "Four of a Kind":8, "Full House":7, "Flush":6, "Straight":5, "Three of a Kind":4, "Two Pair":3, "Pair":2, "High Card":1 }


    # Runs the game in a closed loop
    def play(self):
        playing = True
        while playing:
            self.in_game = []
            for i in range(self.num_players):
                in_game.append("Player"+str(i))
            self.draw_flop()
            self.deal_cards()
            for i in range(len(self.in_game)):
                decision_made = True
                while decision_made:
                    print("Board: ", self.board)
                    decision = input(self.in_game[i]+", Would you like to, 'bet', 'fold','check': ")
                    if decision == "check":
                        self.check()
                        decision_made = False
                    elif decision == 'fold':
                        self.fold(self.in_game[i])
                        decision_made = False
                    elif decision == 'bet':
                        self.bet(self.in_game[i])
                        decision_made = False
                    else:
                        print("Sorry that is not an option")
                        pass
            self.deck.reset_deck_order()

    # Creates a Player() object for each player
    def add_players(self):
        self.in_game = []
        players = {}
        for i in range(self.num_players):
            players["Player" + str(i)] = Player()
            self.in_game.append("Player"+str(i))
        return players

    # Gives each player two hole cards from the deck
    def deal_cards(self):
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
    def check(self):
        self.players[player].chips = self.players[player].chips - self.big_blind
        self.pot = self.pot + self.big_blind

    # Removes player from the game
    def remove_player(self):
        pass

    # Resets the game
    def reset_game(self, starting_chips, num_players ):
        # Number of players
        self.num_players = num_players
        # Creates player objects
        self.players = self.add_players()
        # Creates deck object
        self.deck = Deck()
        # Created Board
        self.board = []
        # Number of chips each player starts with
        self.starting_chips = starting_chips
        # Number of chips in the pot
        self.pot = 0

    def decide_winner(self):
        highest_player = "Player0"
        for player in self.in_game:
            pass

    # Checks the highest set of cards a player has
    def highest_card_score(self, player):
        pairs = []
        hand = self.players[player].hand
        total_cards = hand+self.board
        # checks for pairs or two pairs
        pairs = check_pairs(total_cards)
        # checks for

    # Checks for the number of pairs
    def check_pairs(self, cards):
        pairs = 0
        cards = []
        for card in cards:
            amount = cards.count(card)
            if amount == 2:
                pairs.append()
                cards.remove(card)
                cards.remove(card)
            if amount == 3:
                for

        result = len(pairs)
        return result














