[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/X8jjJBKR)
# assignment-3
Template repo for Assignment 3, Fall 2023

## OBJECTIVES

* Implementing applied data structures

## SUMMARY/OVERVIEW
In this assignment, you are going to implement some key components to a card game. 
The card game is a version of Euchre (pronounced "U-ker"). Euchre is a 4-player game 
that is modified to be a 2-player for this assignment. 
To get a sense of the game, you can play the traditional version at 
https://cardgames.io/euchre/.

This assignment will focus only on implementing the needed data structures, and a future 
assignment will utilize these implementations to play the game. 


## BACKGROUND

### Basic Rules Of Euchre

I'm providing this for context, but it's not relevant for this week's assignment. 

Euchre is a 2-player game. The player with the most points after 5 rounds wins. 
A player wins a round by "collecting the most tricks". 
A round consists of each player being dealt 5 cards, choosing a trump 
(a suit designated as the highest/most powerful for this round), 
and then each player takes turns playing cards for a "trick". 
A player wins a trick by playing the highest value card. 
There are a couple of rules that must be followed for playing a card: 
the first player can play any card, but the second player must "follow suit": 
if they have a card of the same suit, they must play it (but they can choose 
which card they want to play). Further, a card of the trump suit is higher 
than all other cards in the deck. For example, if Spades is trump, a 9 of Spades is 
higher than an Ace of Diamonds. Within a suit, including trump, the face value of the 
card is highest, with Aces being the highest value card.

In this version of the game, Player 1 (the computer) ALWAYS goes first and 
leads the first card.

The deck used for Euchre is a subset of the traditional 52-card deck. 
It includes the Ace, King, Queen, Jack, 10 & 9 of all four suits (Spades, Diamonds, 
Hearts, and Clubs).

## DETAILS

You'll see that in a3.py, we've begun to define some data structures for you. 
Cards have Suits and Names. A Deck is a Stack of Cards, and a Hand is a 
doubly-linked-list of list nodes called CardNodes.

Suits have both a Name and a Color. Cards have a Name, Suit and Value.

While you are filling out your functions, you can use the `a3_test.py` file to help 
you test and explore your implementations. To do this, in PyCharm, fill out the functions in 
`a3.py`. Then, put code that uses your implementation in `a3_test.py`. In the Terminal 
window, run `python3 a3_test.py`, and your updated code will be run. 
