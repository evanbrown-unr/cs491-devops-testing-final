
# class to reresent dealer/player hand
class Hand:
	def __init__(self, dealer=False):
		self.dealer = dealer
		self.cards = []
		self.total_value = 0

	def add_to_hand(self, card):
		self.cards.append(card)

	def calculate_hand(self):
		accumulator = 0
		contains_ace = False
		for card in self.cards:
			if card.value.isnumeric():
				accumulator += int(card.value)
			else:
				if card.value == "A":
					contains_ace = True
					accumulator += 11
				else:
					accumulator += 10

		if contains_ace and accumulator > 21:
			accumulator -= 10

		self.total_value = accumulator

	def get_total_value(self):
		self.calculate_hand()
		return self.total_value

	def show_hand(self):
		if self.dealer:
			print("hidden")
			i = 1
			while i < len(self.cards):
				print(self.cards[i])
				i += 1
		else:
			for card in self.cards:
				print(card)
			print("Sitting at:", self.get_total_value())
		print()
	