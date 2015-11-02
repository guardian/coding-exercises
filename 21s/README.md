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
* add a new player (called Alex) to the game
* Sam and Alex must play their hand against the Dealer
* Alex plays the same rules as Sam when drawing cards
* the dealer must draw cards from the deck after Sam and Alex
* radomise who gets to pick cards first between Sam and Alex


[1] Numbered cards are their point value. Jack, Queen and King count as 10. Ace counts as 1 or 11 and can be changed to make the most preferable hand.

[More info on the rules] (http://www.pagat.com/banking/blackjack.html)