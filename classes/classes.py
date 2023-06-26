import random

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self) -> str:
        return self.rank + ' of ' + self.suit

class Deck():
    def __init__(self):

        self.deck = []

        for suit in suits:
            for rank in ranks:
                #Creating te card object
                self.deck.append(Card(suit, rank))
                self.deck.append(Card(suit, rank))
                self.deck.append(Card(suit, rank))
                self.deck.append(Card(suit, rank))
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += "\n"+ card.__str__()
        return "The deck has: " + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_one(self):
        return self.deck.pop(0)

class Player():
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.aces = 0
        self.value = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value

        #Tracking aces
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):

        while self.aces and self.value > 21:
            self.value -= 10
            self.aces -= 1


class Chips():
    def __init__(self, total = 100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet