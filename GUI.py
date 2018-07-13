import sys, pygame, time, random

pygame.init()


def load_card_images(screen):
    ranks1 = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]
    suits1 = ["diamonds", "clubs", "hearts", "spades"]
    ranks2 = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suits2 = ["D", "C", "H", "S"]
    size = [32, 22]
    card_images = {}
    for suit in range(len(suits1)):
        for rank in range(len(ranks1)):
            card_images[ranks1[rank] + " of " + suits1[suit]] = \
                pygame.image.load("Images/PNG/"+ ranks2[rank]+suits2[suit] + ".png")

    while True:

        screen.blit(pygame.transform.scale(card_images[ranks1[random.randint(0,len(ranks1)-1)] + " of " + suits1[random.randint(0,len(suits1)-1)]], [140, 200]), [250, 320])
        screen.blit(pygame.transform.scale(card_images[ranks1[random.randint(0,len(ranks1)-1)] + " of " + suits1[random.randint(0,len(suits1)-1)]], [140, 200]), [550, 320])
        screen.blit(pygame.transform.scale(card_images[ranks1[random.randint(0,len(ranks1)-1)] + " of " + suits1[random.randint(0,len(suits1)-1)]], [140, 200]), [850, 320])
        screen.blit(pygame.transform.scale(card_images[ranks1[random.randint(0,len(ranks1)-1)] + " of " + suits1[random.randint(0,len(suits1)-1)]], [140, 200]), [1150, 320])
        pygame.display.flip()
        time.sleep(1)


def create_background():
    size = [1500, 800]
    image = pygame.image.load("Images/PokerTable.jpg")
    screen = pygame.display.set_mode(size)
    screen.blit(image, [0, 0])
    pygame.display.flip()
    return screen


screen = create_background()
load_card_images(screen)

x = input("Done?")


