from random import choice
"""
Cards
"""
from collections import namedtuple

Card = namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    """"""
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamond clubs hearts'.split()


    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, pos):
        return self._cards[pos]

    def __str__(self):
        return f'FrenchDeck has {len(self)} cards.'

    def __repr__(self):
        return f'FrenchDeck {id(self)}'

if __name__ == '__main__':
    deck = FrenchDeck()
    ranks = [2, 3, 4, 5]
    suits = ['diamonds', 'clubs', 'hearts']
    # [('diamonds', 2), ('diamonds', 3)...]
    cards = []
    for s in suits:
        # diamonds, clubs, hearts
        for r in ranks:
            # 2, 3, 4, 5
            cards.append((s, r))

    cards2 = [(s, r) for s in suits for r in ranks]
    print(cards2)

    even = [x for x in range(1, 11) if x % 2 == 0]
    print(even)
    char = 'A'
    some_list = [char + str(y) for y in range(1, 11)]
    print(some_list)

