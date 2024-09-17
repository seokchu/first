import collections

Card = collections.nametuple('Card', ['rank','suit'])

class FrenchDeck:
    rank = [str(n) for n in range(2,11) + list('JQKA')]
    suit = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                        for rank in self.ranks]
    def __len__(self):
        return len(self._cards)

    def __getitem__(self,position):
        return self.cards[position]
