import random
import pygame


W_SIZE = [800, 600]
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

card_ranks = {str(i): i for i in range(2, 11)}
for i in ('J', 'Q', 'K'):
    card_ranks[i] = 10
card_ranks['A'] = 11
card_ranks['a'] = 1
card_suits = ['clubs', 'diamonds', 'hearts', 'spades']
x, y = 100, 100
suit_color = {
    "clubs": RED,
    "diamonds": BLACK,
    "hearts": [RED, ((x, y), (x-10, y-15), (x-10, y-5), (x-10, y+5), (x-10, y+15), (x+0, y+15), (x+5, y+15), (x+35, y+50),
                     (x+35, y-50), (x+5, y-15), (x+0, y-15), (x-10, y-15), (x-10, y-5), (x-10, y+5), (x-10, y+15))],
    "spades": BLACK
}

deck = [(i, j) for j in card_suits for i in card_ranks if i != 'a']


print(suit_color["hearts"][1])

class GameObject(object):
    """
    a general class for all objects
    """

    def __init__(self, x=0, y=0):
        self.x, self.y = x, y
        pass

    def draw(self, x, y):
        # pygame.draw.polygon(screen, suit_color[card.id[1]], ((x, y + 100), (x + 100, y + 100), (x + 100, y), (x, y)))
        # will make it later
        pass
    pass


class Deck(GameObject):
    """return a deck of cards"""
    global deck

    def __init__(self):
        super().__init__()
        self.deck = []
        self.create_new_deck(deck)
        pass

    def create_new_deck(self, card_list):
        self.deck = []
        for card in card_list:
            self.deck.append(Card(card))
        random.shuffle(self.deck)
        pass

    pass


class Card(GameObject):
    """
    want to make an object Card
    13 ranks in four suits: clubs (♧), diamonds (♢), hearts (♥) and spades (♤)
    """

    def __init__(self, id):
        super().__init__()
        self.id = id
        pass

    pass


new_deck = Deck().deck

for i in new_deck:
    print(i.id)

pygame.init()

screen = pygame.display.set_mode(W_SIZE)

pygame.display.set_caption("Black Jack in PyGame")

clock = pygame.time.Clock()

finish = False

# shit... now i figured out I need to put coordinates and not vectors ))))
heart = ((x, y),
         (x-10, y-15), (x-10, y-5), (x-10, y+5), (x-10, y+15), (x+0, y+15), (x+5, y+15), (x+35, y+50),
         (x+35, y-50), (x+5, y-15), (x+0, y-15), (x-10, y-15), (x-10, y-5), (x-10, y+5), (x-10, y+15))


x = 0
y = 0
s = 1
nit = ((x, y), (x-10*s, y-10*s), (x-20*s, y-10*s), 
(x-30*s, y), (x-30*s, y+20*s), (x-20*s, y+40*s), 
(x, y+60*s), (x+20*s, y+40*s), (x+30*s, y+20*s), 
(x+30*s, y), (x+20*s, y-10*s), (x+10*s, y-10*s), 
(x, y))


while not finish:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True



    screen.fill(WHITE)
    pygame.draw.polygon(screen, suit_color["hearts"][0], nit)


    # refresh rate
    pygame.time.Clock().tick(60)
    pygame.display.flip()






