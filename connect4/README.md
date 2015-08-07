# Connect4

Connect4 is a grid-based game, where players take it in turns to add
tokens. The winner is whoever manages to line up 4 pieces, in any
direction, first. Diagonals are allowed.

https://en.wikipedia.org/wiki/Connect_Four

## Tasks

The aim is to develop an interactive version of the game which the
candidate and interviewer can play together.

A simple, text-based, representation of the grid is encouraged to
start with. For example, you might use '.' for empty slots, and 'x'
and 'o' for pieces of the two players. Players can input their turns
via the REPL.

A minimal version of the game should support:

- a 6 x 7 grid
- players play pieces sequentially
- the game identifies winning turns and ends at that point

## Bonus rounds

### Pop Out

In addition to the existing rules, players may 'pop' one of the pieces
out from the bottom of the board for their turn. All the pieces above
shift downwards. Victory conditions remain the same as before.

### 5-in-a-row

Instead of four pieces in a row for victory, 5 are now required! Adapt
the grid to be 6 x 9 to accommodate this.

### Power up

In addition to the usual pieces, players also receive specially marked
'Power Checkers' pieces. This can be played once per game. One example
of a 'Power Checker' is an Anvil - this removes all pieces below it
when played, leaving the Anvil at the bottom row of the board.

Implement the Anvil.

Invent your own 'Power Checker' and add it to the game!
