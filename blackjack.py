from deck import Deck
from hand import Hand

# class to encapsulate gameplay functionality of blackjack
class Blackjack:
	def __init__(self):
		pass

	def play(self):
		playing = True

		while playing:
			self.player = Hand()
			self.dealer = Hand(dealer=True)
			self.deck = Deck()
			self.deck.shuffle()

			for i in range(2):
				self.player.add_to_hand(self.deck.deal())
				self.dealer.add_to_hand(self.deck.deal())

			self.show_table()

			game_over = False

			while not game_over:
				player_win, dealer_win = self.check_blackjack()
				if player_win or dealer_win:
					game_over = True
					self.show_results(player_win, dealer_win)
					continue

				choice = input("Hit or stick (h/s)?").lower()
				while choice not in ["hit", "stick", "h", "s"]:
					choice = input("Invalid input. Enter Hit or Stick or (h/s)").lower()

				if choice in ["hit", "h"]:
					self.player.add_to_hand(self.deck.deal())
					if self.dealer.get_total_value() <= 17:
						self.dealer.add_to_hand(self.deck.deal())
					self.show_table()
					if self.player_busted():
						print("Player busted!")
						game_over = True
					if self.dealer_busted():
						print("Dealer busted!")
						game_over = True
				else:
					player_value = self.player.get_total_value()
					dealer_value = self.dealer.get_total_value()

					print("\nFINAL RESULTS:")
					print("Player score:", player_value)
					print("Dealer score:", dealer_value)
					print()

					if player_value > dealer_value:
						player_win = True
					elif player_value < dealer_value:
						dealer_win = True
					else:
						player_win = dealer_win = True

					game_over = True
					self.show_results(player_win, dealer_win)

			play_again = input("Test your luck again? (y/n)").lower()
			if play_again in ["no", "n"]:
				playing = False
			else:
				game_over = False

	def player_busted(self):
		return self.player.get_total_value() > 21

	def dealer_busted(self):
		return self.dealer.get_total_value() > 21

	def check_blackjack(self):
		player_win = False
		dealer_win = False

		if self.player.get_total_value() == 21:
			player_win = True
		if self.dealer.get_total_value() == 21:
			dealer_win = True

		return player_win, dealer_win

	def show_table(self):
		print("\nDealer's hand:")
		self.dealer.show_hand()
		print("Player's hand:")
		self.player.show_hand()

	def show_results(self, player_win, dealer_win):
		if player_win and dealer_win:
			print("Draw!")
		elif player_win:
			print("Player has won. Congratulations!")
		elif dealer_win:
			print("House has won. Better luck next time!")



if __name__ == "__main__":
	blackjack = Blackjack()
	blackjack.play()