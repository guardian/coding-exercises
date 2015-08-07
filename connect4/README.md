# Connect4

Connect4 is a grid-based game, where players take it in turns to add
tokens. The winner is whoever manages to line up 4 pieces, in any
direction, first. Diagonals are allowed.

https://en.wikipedia.org/wiki/Connect_Four

## Tasks

1. Model a 6 x 7 grid (should be visualised)
2. Players should be able to play pieces sequentially
3. The game should identify winning turns and end at that point

While not, required, candidates and interviewers are encouraged to
play via the REPL. A basic text-based representation of the board and
pieces is suggested.

Interviewers should be able to help with IO methods - reading input,
and printing output.

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
