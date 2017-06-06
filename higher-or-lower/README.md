# Higher or lower?

We want to create a guessing game.

The game consists of ten cards numbered 1 to 10.

The player shuffles the cards and deals them face down in a row.

The player then turns over the first card.

They then play the game by guessing whether the next card in the row is higher or lower than the last card revealed.

If they guess correctly, they guess the next card and the next until all ten cards have been turned face up.

The game should tell the user whether they won or lost and offer to start a new game.

You do not have to create a user interface for the game: it will be fine to play it from the shell or REPL, or you can just simulate the game in a test suite.

## Example

The first card is a 3, the player guesses higher. The next card is a 7 so the player continues.

They guess lower but the next card is an 8 so they lose.

## Version 2

Our game is great but we want to make it a bit harder.

We want to be able to configure how many cards the user must guess to win the game.

We also want to track how many cards the user guessed correctly and whether they won the game or not.

We also want to be able to change how many sets of cards are present in the game. In our first iteration we just had one set but we want the initial shuffle to work across multiple sets so there are multiple copies of the same value card. So if we choose two sets of cards there will be two value 10 cards, two 9 and so on.

Modify your code to take into account these changes.