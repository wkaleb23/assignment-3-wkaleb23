import sys
from a3 import *


def create_deck_test():
    deck = create_deck()
    print_deck(deck)
    print("Create deck test passed")


def create_card_node_test():
    card_node = create_card_node("my_payload")
    ## Because this is a unit test for "create_card_node()",
    ##  I'm willing to "break the abstraction" to make sure
    ##  it's correct
    if (card_node['payload'] != 'my_payload'):
        print("Test failed-- wrong payload")
    if card_node['prev'] is not None:
        print("Test failed-- wrong prev node")
    if card_node['next'] is not None:
        print("Test failed-- wrong next node")

    print("Create card_node test passed")


def card_node_next_test():
    print("Create card_node_next test by-passed")

def create_hand_test():
    hand = create_hand()
    assert hand['first_card'] is None, "First card is not None when it should be"
    assert hand['num_cards_in_hand'] == 0, "num_cards_in_hand is not 0 when it should be"
    print("create_hand_test passed")

def add_1card_to_hand_test():
    ## Set up
    hand = create_hand()
    card = ("jack", "hearts", 10)

    ## Execute the thing to test
    add_card_to_hand(hand, card)

    ## Evaluate the result for correctness
    assert hand['num_cards_in_hand'] == 1, "num_cards_in_hand should be 1"
    assert get_card_from_node(
        hand['first_card']) is card, 'The first card is not the right one'
    print("add_card_to_hand_test passed")

def add_2cards_to_hand_test():
    ## Set up
    hand = create_hand()
    card = ("jack", "hearts", 11)
    card2 = ("queen", "hearts", 12)

    ## Execute the thing to test
    add_card_to_hand(hand, card)
    add_card_to_hand(hand, card2)

    ## Evaluate the result for correctness
    assert hand['num_cards_in_hand'] == 2, "num_cards_in_hand should be 2"
    assert is_card_in_hand(hand, card), "Card 1 is not in hand but should be"
    assert is_card_in_hand(hand, card2), "Card 2 is not in hand but should be"
    assert get_card_from_node(hand['first_card']) is card2, "Card2 is not the first card in the hand, but should be"
    print("add_2card_to_hand_test passed")

def remove_first_card_from_hand_test():
    ## Set up
    hand = create_hand()
    card = ("jack", "hearts", 11)
    card2 = ("queen", "hearts", 12)
    add_card_to_hand(hand, card)
    add_card_to_hand(hand, card2)

    ## Execute the thing to test
    removed_card = remove_card_from_hand(hand, card)

    ## Evaluate the result for correctness
    assert hand['num_cards_in_hand'] == 1, "num_cards_in_hand should be 1"
    assert not is_card_in_hand(hand, card), "Card 1 is in hand but should not be"
    assert is_card_in_hand(hand, card2), "Card 2 is not in hand but should be"
    assert removed_card is card, "Card was not returned but should be"
    assert get_card_from_node(hand['first_card']) is card2, "Card 2 is not the first element but should be"

    print("remove_first_card_from_hand_test passed")

def main():
    create_deck_test()
    create_card_node_test()
    card_node_next_test()
    create_hand_test()
    add_1card_to_hand_test()
    add_2cards_to_hand_test()
    remove_first_card_from_hand_test()

if __name__ == '__main__':
    sys.exit(main())
