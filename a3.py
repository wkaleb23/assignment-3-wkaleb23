## These constants have been defined as a starting point.
## You may find yourself wanting to define things a little differently for your
##  implementation. That's fine.
NUM_CARDS_IN_HAND = 5
NUM_CARDS_IN_DECK = 24

SUITS = ["Clubs", "Spades", "Hearts", "Diamonds"]
FACES = ["Jack", "Queen", "King", "Ace"]
NUMBERED = [9, 10]
COLOR_BLACK = "Black"
COLOR_RED = "Red"

## card is a tuple of (name, suit, color, value)

## deck is a list structured as a stack

## card_node is a dict of {next_card, prev_card, payload}

## hand is a linked list, represented by a dict of {first_card, num_cards_in_hand}

# ----------------------------------------
#  Deck functions
# ---------------------------------------
#  Assume that the value of cards are:
#  Nine=9; Ten=10; Jack=11; and so on, up to Ace=14.

# Creates the deck, initializing any fields necessary.
# Returns a deck.
def create_deck():
	pass

# Adds a card to the top of the deck.
# Returns a pointer to the deck.
def push_card_to_deck(deck, card):
	pass

# Shows the top card, but does not remove it from the stack.
# Returns a pointer to the top card.
def peek_card(deck):
	pass

# Removes the top card from the deck and returns it.
# Returns a pointer to the top card in the deck.
def pop_card(deck):
	pass

# Determines if the deck is empty.
# Returns 0 if the Deck has any cards; 1 otherwise.
def is_deck_empty(deck):
	pass

## Prints the provided deck
def print_deck(deck):
	pass

#----------------------------------------
# Hand functions
#----------------------------------------

## A Hand is a linked list, so we define Card_Nodes before
## defining the Hand

def create_card_node(card):
	pass

def get_next_card_node(card_node):
	pass

def get_prev_card_node(card_node):
	pass

def get_card_from_node(card_node):
	pass


# Creates a Hand and initializes any necessary fields.
# Returns a new empty hand
def create_hand():
	pass

# Adds a card to the hand.
def add_card_to_hand(hand, card):
	pass

# Removes a card from the hand via card value
# Returns the card (not a card_node) that was removed from the hand
# Returns None if the specified card is not in the hand
def remove_card_from_hand(hand, card):
	pass

# Removes a card from the hand via index
# Returns the card, not a card_node
# Returns None if index is < 0 or greater than the length of the hand/list.
def get_card_from_hand(hand, index):
	pass

# Determines if there are any cards in the hand.
# Return 0 if the hand is empty; 1 otherwise.
def is_hand_empty(hand):
	pass

# Prints a single card
def print_card(card):
	pass

# Prints an entire hand
def print_hand(hand):
	pass

