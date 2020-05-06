# Inheritance is the ability to define a new class that is a modified version of an existing class
"""
There are several kinds of relationship between classes:

Objects in one class might contain references to objects in another class. For example, each Rectangle contains a reference to a Point, and each Deck contains references to many Cards. This kind of relationship is called HAS-A, as in, “a Rectangle has a Point.”
One class might inherit from another. This relationship is called IS-A, as in, “a Hand is a kind of a Deck.”
One class might depend on another in the sense that objects in one class take objects in the second class as parameters, or use objects in the second class as part of a computation. This kind of relationship is called a dependency.
"""
import random
class Card:
    """
    Represent a standard
    """
    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = ['None', 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    def __str__(self):
        return ' %s of %s' %(Card.rank_names[self.rank],Card.suit_names[self.suit])
    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1<t2

class  Desk:
    def __init__(self):
        self.cards =[]
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    def pop_card(self):
        return self.cards.pop()
    def add_card(self, card):
        self.cards.append(card)
    def shuffle(self):
        random.shuffle(self.cards)
#inheritance
class Hand(Desk):
    """
    Represents a hand of playing cards.
    """
    def __init__(self, label):
        self.cards =[]
        self.label = label
    def __str__(self):
        return 'From:' + str(self.label)+super().__str__()




hand1 = Hand('minh dan')
print(hand1.label)



desk = Desk()
desk.shuffle()
card1 = desk.pop_card()
hand1.add_card(card1)
print('Card by pop form parent class')
print(card1)
print('Card from chill class')
print('that method print form parent')
print(hand1)
# print(hand1.cards)


# card1 = Card(1, 12)
# print(card1)
# print(desk)