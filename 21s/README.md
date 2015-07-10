Can you beat the dealer at 21
======================================


Potential tasks for the pairing test:
--------------------------------------

#### Setup the game
* create a shoe (n decks of cards, randomly mixed together)
* create n number of players
* create 1 dealer
* deal two cards from the top of the shoe to each player and the dealer

#### Rules to implement
* each player plays their hand against the dealer only
* determine score of a hand[1]
* before picking cards see if player or dealers hand is blackjack (total score 21) and wins.
* for any plays where the above is not true then each player in turn picks cards from the top of the shoe
* there is no limit to cap to the cards drawn
* the player should aim to get a higher score than the dealer
* if the player has a higher score than the dealer but not reached 21 then choice to draw or stick is 50:50.
* totals above 21 are bust and the player is out of the game
* after all the players have picked the dealer can pick cards from the top of the shoe
* the dealer score must be above 17 and cannot pick futher cards once this limit has been reached.
* if the dealer scores over 21 they have bust and have lost the hand
* decide if the player or the dealer wins.

#### Things to consider
* shoe that becomes empty (it needs refilling)
* ensure order of play is correct

[1] Numbered cards are their point value. Jack, Queen and King count as 10. Ace counts as 1 or 11 and can be changed to make the most preferable hand.

What tech skills could the game help look for?
-----------------------------------------------

* Working with structures (for deck of cards, number of players)
* Edge cases for the rules (TDD)
* Can test OO and functional depending on how to implement each player


[More info on the rules] (http://www.pagat.com/banking/blackjack.html)