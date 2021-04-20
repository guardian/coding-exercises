# Game of Life

## Background 

The Game of Life is a cellular automaton. 

It is discussed in detail on [Wikipedia](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).

## Rules

The game of life is played on a two dimensional grid.

At each turn, the state of a cell may either be "alive" or "dead"; determined by the following rules:

1. A cell with fewer than two live neighbours dies of under-population
2. A cell with 2 or 3 live neighbours lives on to the next generation
3. A cell with more than 3 live neighbours dies of overcrowding
4. An empty cell with exactly 3 live neighbours "comes to life"

## Tasks

1. Implement a grid for the game to take place on.
2. Carefully consider what happens at the edges.
3. Implement the game of life for a single iteration.
4. Display the results for a single iteration.
5. Animate the game so that it is played in real time.

## Extension

There are many features which may exist in the game of life, an interesting class of them is the spaceship.
Seed a grid with the [heavyweight spaceship](https://conwaylife.com/wiki/Heavyweight_spaceship) a [pattern file](https://www.conwaylife.com/patterns/hwss.cells) should be used. 
