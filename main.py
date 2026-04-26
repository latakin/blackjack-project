
from blackjack.deck import Deck,ranks,suits
from blackjack.chips import Chips
from blackjack.hand import Hand, values


test_deck = Deck()
test_deck.shuffle()
test_player = Hand()
test_player.add_card(test_deck.deal())
test_player.add_card(test_deck.deal())
print(test_player.value)










