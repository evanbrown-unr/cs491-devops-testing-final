# class for card data structure
class Card:
	def __init__(self, suit, value):
		self.suit = suit
		self.value = value

	# overload print
	def __repr__(self):
		return " of ".join((self.value, self.suit))

	# overload string representation
	def __str__(self):
		return " of ".join((self.value, self.suit))