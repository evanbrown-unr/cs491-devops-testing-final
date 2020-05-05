from card import Card
import random

# class for deck data structure
class Deck:
	def __init__(self):
		SUITS = ["Spades", "Hearts", "Diamonds", "Clubs"]
		VALUES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
		self.cards = [Card(suit, value) for suit in SUITS for value in VALUES]

	def shuffle(self):
		if len(self.cards) > 1:
			random.shuffle(self.cards)

	def deal(self):
		if len(self.cards) >= 1:
			return self.cards.pop(0)