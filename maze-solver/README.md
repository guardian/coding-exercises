# Maze Solving Test

Given a 10x10 ASCII maze, create an algorithm which will solve the maze.

The maze might look as follows:
```
+--+--+--+--+--+--+--+--+--+--+
   |                       |  |
+  +  +--+  +--+--+--+--+  +  +
|  |  |  |     |           |  |
+  +  +  +--+  +--+  +  +--+  +
|     |        |     |     |  |
+--+  +--+--+--+  +--+--+  +  +
|     |     |        |     |  |
+--+--+  +--+  +--+--+  +--+  +
|     |        |     |  |     |
+  +  +--+--+--+  +  +  +  +--+
|  |  |           |     |     |
+  +  +  +  +--+--+--+--+--+  +
|  |     |     |           |  |
+  +--+--+--+  +  +--+--+--+  +
|  |     |     |     |     |  |
+  +  +  +  +--+  +--+  +  +  +
|     |  |        |     |  |  |
+--+--+  +--+--+--+  +--+  +  +
|                    |
+--+--+--+--+--+--+--+--+--+--+

```
It will be loaded for you already and will be stored in a
2-dimensional array.

A `+` and a `-` indicate walls that cannot be passed through. A blank
space means that can move through it.

As the maze is solved, you should store what steps you've taken to get
through the maze in the form of a grid reference.

e.g [(0,1), (0,3), (1,1)]

Here each tuple in an index in the array that can be
accessed. Following the generated path should lead to the end of the
maze. Do not worry about backtracking. There is no need to remove any
backtracks taken.

## A possible solution

The simplest way to solve a maze is to use a
[Wall Following Algorithm](https://en.wikipedia.org/wiki/Maze_solving_algorithm#Wall_follower).

You simply enter the maze and turn left at every wall or right at
every wall. Doing this you are guaranteed to reach either another exit
or will return to the beginning. Your algorithm can assume that
reaching the entrance before finding an exit means the maze cannot be
solved.
