import unittest

from card import Card
from deck import Deck
from hand import Hand
from blackjack import Blackjack


### UNIT TESTS ####

# This is full test coverage for Card because the only
# functionality that it provides is overloading the 
# __repr__() and __str__() methods
class CardUnitTests(unittest.TestCase):
	def setup(self):
		self.card = Card("Spades", "A")

	def cleanup(self):
		self.card = None

	# tests the string representation of a card
	# tests direct mismatches and case sensitivity
	def test_str_repr(self):
		self.setup()
		self.assertEqual("A of Spades", str(self.card))
		self.assertNotEqual("Q of Clubs", str(self.card))
		self.assertNotEqual("2 of Spades", str(self.card))
		self.assertNotEqual("A of spades", str(self.card))
		self.cleanup()

########################################################################

# These test all of the functions in the Deck unit
class DeckUnitTests(unittest.TestCase):
	def setup(self):
		self.deck = Deck() # unshuffled deck

	def cleanup(self):
		self.deck = None

	# tests that cars are in order of suit and value when unshuffled
	# tests that those cards are not in deck anymore
	def test_before_shuffle(self):
		self.setup()
		test_card = self.deck.cards.pop(0) # take first card
		self.assertEqual("A of Spades", str(test_card))
		test_card_2 = self.deck.cards.pop(0)
		self.assertEqual("2 of Spades", str(test_card_2))
		self.cleanup()

	# tests that random card is not at top of deck
	# may sometimes be A of Spades, so can not assume otherwise
	# tests that card is properly removed from deck
	def test_after_shuffle(self):
		self.setup()
		self.deck.shuffle()
		test_card = self.deck.cards.pop()
		self.assertNotIn(test_card, self.deck.cards)
		self.cleanup()

	# tests that one round of dealing removes those two
	# cards from the main deck
	def test_deal(self):
		self.setup()
		test_card = self.deck.deal()
		test_card_2 = self.deck.deal()
		self.assertNotIn(test_card, self.deck.cards)
		self.assertNotIn(test_card, self.deck.cards)
		self.cleanup()

#####################################################################

# Tests all code coverage for the Hand
# Since hand requires the use of card, they are used
# without having them being drawn from the deck to reduce
# testing dependencies
class HandUnitTests(unittest.TestCase):
	def setup(self):
		self.hand = Hand()

	def cleanup(self):
		self.hand = None

	# tests that proper card gets added to hand
	def test_add_to_hand(self):
		self.setup()
		a_spade = Card("Spades", "A")
		q_hearts = Card("Hearts", "Q")
		self.hand.add_to_hand(a_spade)
		self.hand.add_to_hand(q_hearts)
		self.assertIn(a_spade, self.hand.cards)
		self.assertIn(q_hearts, self.hand.cards)
		self.cleanup()

	# tests if hand value is properly calculated
	def test_calculate_hand(self):
		self.setup()
		a_spade = Card("Spades", "A")
		q_hearts = Card("Hearts", "Q")
		self.hand.add_to_hand(a_spade)
		self.hand.add_to_hand(q_hearts)
		self.hand.calculate_hand()
		total = self.hand.get_total_value()
		self.assertEqual(21, total)
		self.cleanup()


### INTEGRATION TESTS ###

# The Blackjack integrations requires that the player and hand object
# be instantiated 
class BlackjackIntegreationTests(unittest.TestCase):
	def setup(self):
		self.blackjack = Blackjack()
		self.blackjack.player = Hand()
		self.blackjack.dealer = Hand()

	def cleanup(self):
		self.blackjack = None

	# tests if bust logic works for player hand
	# if the player busts, then the game is over and the dealer wins
	def test_player_busted(self):
		self.setup()
		self.blackjack.player.add_to_hand(Card("Spades", "A"))
		self.blackjack.player.add_to_hand(Card("Hearts", "A"))
		self.assertFalse(self.blackjack.player_busted())
		self.blackjack.player.add_to_hand(Card("Hearts", "K"))
		self.blackjack.player.add_to_hand(Card("Hearts", "Q"))
		self.assertTrue(self.blackjack.player_busted())
		self.cleanup()

	# tests if bust logic works for dealer hand
	# if the dealer busts, then the game is over and the player wins
	def test_dealer_busted(self):
		self.setup()
		self.blackjack.dealer.add_to_hand(Card("Spades", "A"))
		self.blackjack.dealer.add_to_hand(Card("Hearts", "A"))
		self.assertFalse(self.blackjack.dealer_busted())
		self.blackjack.dealer.add_to_hand(Card("Hearts", "K"))
		self.blackjack.dealer.add_to_hand(Card("Hearts", "Q"))
		self.assertTrue(self.blackjack.dealer_busted())
		self.cleanup()

	# tests if check blackjack method properly functions
	# starts by having player test their hand, first when
	# it is not a blackjack and then when it is
	def test_check_blackjack_player(self):
		self.setup()
		self.blackjack.player.add_to_hand(Card("Spades", "A"))
		self.assertEqual((False, False), self.blackjack.check_blackjack())
		self.blackjack.player.add_to_hand(Card("Hearts", "Q"))
		self.assertEqual((True, False), self.blackjack.check_blackjack())
		self.cleanup()

	# same test except for the dealer rather than the player
	def test_check_blackjack_dealer(self):
		self.setup()
		self.blackjack.dealer.add_to_hand(Card("Clubs", "A"))
		self.assertEqual((False, False), self.blackjack.check_blackjack())
		self.blackjack.dealer.add_to_hand(Card("Diamonds", "Q"))
		self.assertEqual((False, True), self.blackjack.check_blackjack())
		self.cleanup()


if __name__ == "__main__":
	unittest.main()