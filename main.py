import random
import pygame


W_SIZE = [800, 600]
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


pygame.init()
screen = pygame.display.set_mode(W_SIZE)
pygame.display.set_caption("Black Jack in PyGame")
clock = pygame.time.Clock()


def resize(coordinates, size=1):
    new = []
    for item in coordinates:
        new.append(tuple(list(i * size for i in item)))
    return tuple(new)


def place(coordinates, x=0, y=0):
    new = []
    for item in coordinates:
        new.append(tuple((item[0] + x, item[1] + y)))
    return tuple(new)


def coor_to_draw(card, x=0, y=0):
    return place(resize(suit_shape[card]), x, y)


def card_draw(card, x, y):
    global screen
    pygame.draw.polygon(screen, suit_color[card[1]], coor_to_draw(card[1], x, y))


card_ranks = {str(i): i for i in range(2, 11)}
for i in ('J', 'Q', 'K'):
    card_ranks[i] = 10
card_ranks['A'] = 11
card_ranks['a'] = 1
card_suits = ['clubs', 'diamonds', 'hearts', 'spades']

suit_shape = {
    'clubs': (
        (30, 0), (20, 10), (30, 30), (10, 20), (0, 30), (10, 40), (30, 30),
        (20, 70), (40, 70), (30, 30), (50, 40), (60, 30), (50, 20), (30, 30), (40, 10)),
    'diamonds': ((30, 0), (0, 35), (30, 70), (60, 35)),
    'hearts': ((30, 10), (20, 0), (10, 0), (0, 10), (0, 30), (10, 50),
               (30, 70), (50, 50), (60, 30), (60, 10), (50, 0), (40, 0)),
    'spades': ((30, 0), (0, 40), (0, 50), (10, 60), (20, 60), (30, 50),
               (20, 70), (40, 70), (30, 50), (40, 60), (50, 60), (60, 50), (60, 40))
}

suit_color = {
    'clubs': BLACK,
    'diamonds': RED,
    'hearts': RED,
    'spades': BLACK
}

deck = [(i, j) for j in card_suits for i in card_ranks if i != 'a']

new_deck = deck.copy()
random.shuffle(new_deck)


finish = False


while not finish:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True

    screen.fill(WHITE)

    for i in range(len(new_deck)):
        card_draw(new_deck[i], random.randint(0, W_SIZE[0]), random.randint(0, W_SIZE[1]))


    # refresh rate
    pygame.time.Clock().tick(60)
    pygame.display.flip()






