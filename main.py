import random
import pygame


W_SIZE = [800, 600]
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


ranks = {str(i): i for i in range(2, 11)}
for i in ('J', 'Q', 'K'):
    ranks[i] = 10
ranks['A'] = 11
ranks['a'] = 1

suits = ['clubs', 'diamonds', 'hearts', 'spades']

shapes = {
    'clubs': [30, 0, 20, 10, 30, 30, 10, 20, 0, 30, 10, 40, 30, 30,
              20, 70, 40, 70, 30, 30, 50, 40, 60, 30, 50, 20, 30, 30, 40, 10],
    'diamonds': [30, 0, 0, 35, 30, 70, 60, 35],
    'hearts': [30, 10, 20, 0, 10, 0, 0, 10, 0, 30, 10, 50,
               30, 70, 50, 50, 60, 30, 60, 10, 50, 0, 40, 0],
    'spades': [30, 0, 0, 40, 0, 50, 10, 60, 20, 60, 30, 50,
               20, 70, 40, 70, 30, 50, 40, 60, 50, 60, 60, 50, 60, 40],
    'A': [14, 0, 0, 50, 10, 50, 12.5, 42, 27.75, 42,
          25, 32, 15, 32, 20, 14, 30, 50, 40, 50, 26, 0],
    'K': [0, 0, 0, 50, 10, 50, 10, 30, 15, 25, 28, 50,
          40, 50, 23, 17, 40, 0, 27, 0, 10, 17, 10, 0],
    'Q': [0, 10, 0, 40, 10, 50, 40, 50, 20, 30, 10, 30, 20, 40,
          15, 40, 10, 35, 10, 15, 15, 10, 25, 10, 30, 15, 30, 35,
          27.5, 37.5, 35, 45, 40, 40, 40, 10, 30, 0, 10, 0],
    'J': [0, 0, 0, 10, 30, 10, 30, 35, 25, 40, 15, 40,
          10, 35, 10, 30, 0, 30, 0, 40, 10, 50, 30, 50,
          40, 40, 40, 0],
    '10': ([0, 10, 0, 17, 6, 17, 6, 50, 14, 50, 14, 0, 6, 0],
           [28, 0, 22, 0, 16, 10, 16, 40, 22, 50, 34, 50, 40, 40, 40, 10,
           34, 0, 28, 0, 28, 8, 32, 14, 32, 36, 28, 42, 24, 36, 24, 14, 28, 8]),
    '9': [30, 30, 10, 30, 0, 20, 0, 10, 10, 0, 30, 0, 40, 10,
          40, 40, 30, 50, 10, 50, 0, 40, 27, 40, 30, 37, 30, 13,
          27, 10, 13, 10, 10, 13, 10, 17, 13, 20, 30, 20],
    '8': [20, 0, 10, 0, 2, 8, 2, 18, 6, 22, 0, 28, 0, 40, 10, 50,
          30, 50, 40, 40, 40, 28, 34, 22, 38, 18, 38, 8, 30, 0, 20, 0,
          20, 8, 27, 8, 30, 11, 30, 15, 27, 18, 20, 18, 20, 28, 27, 28,
          30, 31, 30, 37, 27, 40, 13, 40, 10, 37, 10, 31, 13, 28, 20, 28,
          20, 18, 13, 18, 10, 15, 10, 11, 13, 8, 20, 8],
    '7': [0, 0, 0, 10, 28, 10, 8, 50, 20, 50, 40, 10, 40, 0],
    '6': [40, 13, 40, 10, 30, 0, 10, 0, 0, 10, 0, 40, 10, 50, 30, 50, 40, 40,
          40, 28, 30, 18, 13, 18, 10, 21, 10, 31, 13, 28, 27, 28, 30, 31, 30, 37,
          27, 40, 13, 40, 10, 37, 10, 13, 13, 10, 27, 10, 30, 13],
    '5': [40, 0, 0, 0, 0, 26, 27, 26, 30, 29, 30, 37, 27, 40, 13, 40,
          10, 37, 0, 37, 0, 40, 10, 50, 30, 50, 40, 40, 40, 26, 30, 16,
          10, 16, 10, 10, 40, 10],
    '4': [24, 0, 0, 30, 0, 40, 24, 40, 24, 30, 12, 30, 24, 14,
          24, 50, 34, 50, 34, 40, 40, 40, 40, 30, 34, 30, 34, 0],
    '3': [0, 0, 0, 10, 26, 10, 14, 18, 10, 18, 10, 28, 27, 28, 30, 31,
          30, 37, 27, 40, 13, 40, 10, 37, 0, 37, 0, 40, 10, 50, 30, 50,
          40, 40, 40, 28, 30, 18, 28, 18, 40, 10, 40, 0],
    '2': [10, 0, 0, 10, 0, 13, 10, 13, 13, 10, 27, 10, 30, 13, 30, 15,
          0, 40, 0, 50, 40, 50, 40, 40, 14, 40, 40, 18, 40, 10, 30, 0],
}

suit_color = {
    'clubs': BLACK,
    'diamonds': RED,
    'hearts': RED,
    'spades': BLACK
}


class GameObject:
    def __init__(self):
        self.data = {}
        pass

    def draw_obj(self, size=1, xy=(0, 0)):
        pass


class Card(GameObject):
    def __init__(self, suit, rank):
        super().__init__()
        self.suit = suit
        self.rank = rank
        pass


pygame.init()
screen = pygame.display.set_mode(W_SIZE)
pygame.display.set_caption("Black Jack in PyGame")
clock = pygame.time.Clock()


def draws(color: tuple, _shape: list, size=1, xy=(0, 0)):
    if type(_shape[0]) == int:
        pygame.draw.polygon(screen, color,
                            tuple((_shape[i] * size + xy[0], _shape[i + 1] * size + xy[1])
                                  for i in range(0, len(_shape), 2)))
    else:
        for shape in _shape:
            pygame.draw.polygon(screen, color,
                                tuple((shape[i] * size + xy[0], shape[i + 1] * size + xy[1])
                                      for i in range(0, len(shape), 2)))


deck = [(i, j) for j in suits for i in ranks if i != 'a']

new_deck = deck.copy()
random.shuffle(new_deck)

finish = False

while not finish:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True

    screen.fill(WHITE)


    draws(BLACK, shapes['spades'], 5, (200, 20))
    draws(BLUE, shapes['10'], 5, (400, 20))




    # refresh rate
    pygame.time.Clock().tick(60)
    # refresh screen
    pygame.display.flip()


