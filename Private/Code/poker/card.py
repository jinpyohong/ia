import random
from abc import ABCMeta, abstractmethod

# Constants
suits = 'CDHS'
ranks = '23456789TJQKA'

class Card(metaclass=ABCMeta):
    """Abstact class for playing cards
    """
    def __init__(self, rank_suit):
        if rank_suit[0] not in ranks or rank_suit[1] not in suits:
            raise ValueError(f'{rank_suit}: illegal card')
        self.card = rank_suit
        
    def __repr__(self):
        return self.card
    
    @abstractmethod
    def value(self):
        """Subclasses should implement this method
        """
        raise NotImplementedError("value method not implemented")

    # card comparison operators
    def __gt__(self, other): return self.value() > other.value()
    def __ge__(self, other): return self.value() >= other.value()
    def __lt__(self, other): return self.value() < other.value()
    def __le__(self, other): return self.value() <= other.value()
    def __eq__(self, other): return self.value() == other.value()
    def __ne__(self, other): return self.value() != other.value()


class PKCard(Card):
    """Card for Poker game
    """
    VALUES = dict(zip(ranks, range(2, 2+len(ranks))))
    
    def value(self):
        return PKCard.VALUES[self.card[0]]

    @property
    def rank(self):
        return self.card[0]

    @property
    def suit(self):
        return self.card[1]

    # Altenatives 
    #
    # def __getattr__(self, attr):
    #     if attr == 'rank':
    #         return self.card[0]
    #     elif attr == 'suit':
    #         return self.card[1]
    #     else:
    #         raise AttributeError(f'{attr}')

class Deck:
    def __init__(self, cls):
        """Create a deck of 'cls' card class
        """
        self.cards = [cls(r + s) for r in ranks for s in suits]
        
    def pop(self):
        return self.cards.pop()
    
    def shuffle(self):
        random.shuffle(self.cards)
        
    def __str__(self):
        return str(self.cards)
    
    def __getitem__(self, index):
        return self.cards[index]
    
    def __len__(self):
        return len(self.cards)

if __name__ == '__main__':
    # Card object instantiation alternatives
    c1 = PKCard('9C')
    c2 = PKCard('TH')
    c3 = PKCard('9H')
    print(c1, c2, c3)
    print(c1, c1.rank, c1.suit)
    # Comparison
    if c1 < c2: print(c1, '<', c2)
    if c1 == c3: print(c1, '==', c3)
    if c1 == c3 < c2: print(c1, '==', c3, '<', c2)
    # testing repr()
    print(str(c1))
    print(repr(c1))
    # list of Cards
    deck = Deck(PKCard)
    deck.shuffle()
    print(deck)
    print(sorted(deck))     # sort list of Cards
    print([c1, c3] == [c3, c1])
