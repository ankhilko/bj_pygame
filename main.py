import random
import pygame

card_ranks = {str(i): i for i in range(2, 11)}
for i in ('J', 'Q', 'K'):
    card_ranks[i] = 10
card_ranks['A'] = 11
card_ranks['a'] = 1
card_suits = ['clubs', 'diamonds', 'hearts', 'spades']

deck = [(i, j) for j in card_suits for i in card_ranks if i != 'a']


class GameObject(object):
    """
    a general class for all objects
    """

    def __init__(self, x=0, y=0):
        self.x, self.y = x, y
        pass

    def draw(self, x, y):
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



