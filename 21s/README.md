Can you beat the dealer at 21
======================================

#### Setup the game
* create a single deck of playing cards
* two players (called Sam and the Dealer) who will play against each other
* each player is given two cards from the top of a shuffled deck of cards

#### Rules to implement
* determine score of a hand[1]
* check if either player has blackjack (21) with their initial hand and wins the game
* if neither player has blackjack then Sam can start drawing cards from the top of the deck
* Sam should stop drawing cards from the deck if their total reaches 17 or higher
* Sam has lost the game if their total is higher than 21 
* when Sam has stopped drawing cards the Dealer can start drawing cards from the top of the deck
* the Dealer should stop drawing cards when their total is higher than Sam.
* the Dealer has lost the game if their total is higher than 21 
* determine which player wins the game

Additions
* ace can be valued at 1 or 11, implement this change into the scoring of a hand.
* add another deck of playing cards that can be shuffled into the original shuffled deck
* add a new player (called Alex) to the game
* Sam and Alex must play their hand against the Dealer
* Alex plays the same rules as Sam when drawing cards
* the dealer must draw cards from the deck after Sam and Alex
* randomise who gets to draw cards first between Sam and Alex

[1] Numbered cards are their point value. Jack, Queen and King count as 10 and Ace counts as 11.

[More info on the rules] (http://www.pagat.com/banking/blackjack.html)