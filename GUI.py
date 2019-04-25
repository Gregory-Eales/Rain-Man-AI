import sys, pygame, time, random

class PokerScreen(object):

    def __init__(self, graphics=True):
        pygame.init()
        pygame.font.init()
        self.card_images = {}
        self.load_card_images()
        self.background_image = pygame.image.load("Images/PokerTable.jpg")
        self.background_size = [1400, 800]
        self.screen = pygame.display.set_mode(self.background_size)
        self.screen.blit(self.background_image, [0, 0])
        self.load_card_images()
        self.card_positions = self.get_card_positions()
        self.white = (255, 255, 255)
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)
        self.text_locations = self.get_player_text_locations()
        if graphics:
            pygame.display.flip()

    def load_card_images(self):
        ranks1 = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        suits1 = ["Diamonds", "Clubs", "Hearts", "Spades"]
        ranks2 = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        suits2 = ["D", "C", "H", "S"]
        size = [32, 22]
        for suit in range(len(suits1)):
            for rank in range(len(ranks1)):
                self.card_images[ranks1[rank] + " of " + suits1[suit]] = \
                    pygame.image.load("Images/PNG/" + ranks2[rank] + suits2[suit] + ".png")
        self.card_images["Back of Card"] = pygame.image.load("Images/PNG/gray_back.png")

    def show_random_cards(self):
        ranks1 = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        suits1 = ["Diamonds", "Clubs", "Hearts", "Spades"]
        for i in range(1):
            self.screen.blit(pygame.transform.scale(self.card_images[ranks1[random.randint(0, len(ranks1) - 1)]
                                                           + " of " + suits1[random.randint(0, len(suits1) - 1)]],
                                               [140, 200]), [250, 320])
            self.screen.blit(pygame.transform.scale(self.card_images[ranks1[random.randint(0, len(ranks1) - 1)]
                                                           + " of " + suits1[random.randint(0, len(suits1) - 1)]],
                                               [140, 200]), [550, 320])
            self.screen.blit(pygame.transform.scale(self.card_images[ranks1[random.randint(0, len(ranks1) - 1)]
                                                           + " of " + suits1[random.randint(0, len(suits1) - 1)]],
                                               [140, 200]), [850, 320])
            self.screen.blit(pygame.transform.scale(self.card_images[ranks1[random.randint(0, len(ranks1) - 1)]
                                                           + " of " + suits1[random.randint(0, len(suits1) - 1)]],
                                               [140, 200]), [1150, 320])
            pygame.display.flip()
            time.sleep(1)

    def card_position_tester(self):
        x = 40
        width, height = int(56 * 1.3), int(80 * 1.3)
        positions = [[710 - width - 10, 400 - 0.5 * height-x], [710, 400 - 0.5 * height-x],
                     [710 - width * 2 - 20, 400 - 0.5 * height-x], [710 + width + 10, 400 - 0.5 * height-x]]
        for pos in positions:
            self.display_card("Ace of Spades", pos)

        positions = [[700-3*width, 0.5 * height - x], [700-4*width-10, 0.5 * height - x], [700+2*width, 0.5 * height - x], [700 + 3*width + 10, 0.5 * height - x]]
        for pos in positions:
            self.display_card("Ace of Spades", pos)

        positions = [[700 - 3 * width, 800 - 1.5 * height - x], [700 - 4 * width - 10, 800 - 1.5 * height - x], [700 + 2*width, 800 - 1.5 * height - x],
                     [700 + 3 * width + 10, 800 - 1.5 * height - x], [width, 400 - 0.5 * height - x], [2*width + 10, 400 - 0.5 * height - x], [1400-2*width, 400 - 0.5 * height - x], [1400-3*width - 10, 400 - 0.5 * height - x]]
        for pos in positions:
            self.display_card("Ace of Spades", pos)
        pygame.display.flip()

    def draw_stat_borders(self):
        width, height, x = int(56 * 1.3), int(80 * 1.3), 40
        w, h = width * 2 + 10, 40
        pygame.draw.rect(self.screen, (0, 0, 0), [700-4*width - 10, 800 - 1.5 * height - x + height + 10, w, h])
        pygame.draw.rect(self.screen, (0, 0, 0), [700 + 2*width, 800 - 1.5 * height - x + height + 10, w, h])
        pygame.draw.rect(self.screen, (0, 0, 0), [1400 - 3 * width - 10, 400 - 0.5 * height - x + height + 10, w, h])
        pygame.draw.rect(self.screen, (0, 0, 0), [700 + 2 * width, 0.5 * height - 40 + height + 10, w, h])
        pygame.draw.rect(self.screen, (0, 0, 0), [700 - 4 * width - 10, 0.5 * height - 40 + 10 + height, w, h])
        pygame.draw.rect(self.screen, (0, 0, 0), [width, 400 - 0.5 * height - x + height + 10, w, h])
        pygame.draw.rect(self.screen, (0, 0, 0), [710 - width - 10, 400 - 0.5 * height - 40 + 10 + height, w, h])

    def display_card(self, card_name, location):
        size = [int(56*1.3), int(80*1.3)]
        self.screen.blit(pygame.transform.scale(self.card_images[card_name], size), location)

    def get_card_positions(self):
        Card_Positions = {}
        x = 40
        width, height = int(56 * 1.3), int(80 * 1.3)
        board_cards = [[700 + 1.5 * width + 20, 400 - 0.5 * height - 40], [700 + 0.5 * width + 10, 400 - 0.5 * height - 40], [700 - 2.5* width - 20, 400 - 0.5 * height - 40], [700 - 1.5*width - 10, 400 - 0.5 * height - 40], [700 - 0.5 * width, 400 - 0.5 * height - 40]]
        Player5_Pos = [[700 - 3 * width, 0.5 * height - 40], [700 - 4 * width - 10, 0.5 * height - 40]]
        Player0_Pos = [[700 + 2 * width, 0.5 * height - 40], [700 + 3 * width + 10, 0.5 * height - 40]]
        Player3_Pos = [[700 - 3 * width, 800 - 1.5 * height - x], [700 - 4 * width - 10, 800 - 1.5 * height - x]]
        Player2_Pos = [[700 + 2 * width, 800 - 1.5 * height - x], [700 + 3 * width + 10, 800 - 1.5 * height - x]]
        Player4_Pos = [[width, 400 - 0.5 * height - x], [2 * width + 10, 400 - 0.5 * height - x]]
        Player1_Pos = [[1400 - 2 * width, 400 - 0.5 * height - x], [1400 - 3 * width - 10, 400 - 0.5 * height - x]]
        Player_Pos = [Player0_Pos, Player1_Pos, Player2_Pos, Player3_Pos, Player4_Pos, Player5_Pos]
        for i in range(6):
            Card_Positions["Player" + str(i)] = Player_Pos[i]
        Card_Positions["Board"] = board_cards
        return Card_Positions

    def update_player_cards(self, cards, player):
        if len(cards)==2:
            for j in range(2):
                self.display_card(cards[j],self.card_positions[player][j])
        if len(cards) != 2:
            for j in range(2):
                self.display_card("Back of Card", self.card_positions[player][j])

    def update_board_cards(self, board, player):
        print(len(self.card_positions[player]))
        print(len(board))
        for j in range(len(board)):
            self.display_card(board[j], self.card_positions[player][j])


    def write_text(self, text, location):
        width, height, x = int(56 * 1.3), int(80 * 1.3), 40
        w, h = width * 2 + 10, 40
        text_surface = self.myfont.render(text, False, self.white)
        self.screen.blit(text_surface, location)

    def get_player_text_locations(self):
        width, height, x = int(56 * 1.3), int(80 * 1.3), 40
        text_locations = {}
        text_locations["Player0"] = [700 + 2 * width, 1.5 * height - 40 + 22]
        text_locations["Player1"] = [1400 - 3 * width - 10, 400 + 0.5 * height - x + 22]
        text_locations["Player2"] = [700 + 2 * width, 800 - 0.5 * height - x + 22]
        text_locations["Player3"] = [700 - 4 * width - 5, 800 - 1.5 * height - x + height + 22]
        text_locations["Player4"] = [width, 400 + 0.5 * height - x + 22]
        text_locations["Player5"] = [700 - 4 * width - 10, 1.5 * height - 40 + 22]
        text_locations["Board"] = [710 - width - 10, 400 + 0.5 * height - 40 + 22]
        return text_locations

    def update_player_scores(self, scores, pot_amount, num_players):
        for i in range(num_players):
            self.write_text(" Player"+str(i)+": " + str(scores[i]), self.text_locations["Player"+str(i)])
        self.write_text(" Pot: "+ str(pot_amount), self.text_locations["Board"])







