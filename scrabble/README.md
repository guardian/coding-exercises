Word Game (Scrabble)
--------------------
![scrabble](https://www.word-grabber.com/3/m/2012/02/scrabble-rack-with-tiles.jpg)

This is a game where players attempt to create words from a set of letter tiles.  Different letters have different points allocated to them.

* Calculate the score for a word. The score is the sum of the points for the letters that make up a word. For example:

GUARDIAN = 2 + 1 + 1 + 1 + 2 + 1 + 1 + 1 = 10

Use these points for each letter:

```
	- 1 point: E, A, I, O, N, R, T, L, S, U
	- 2 points: D, G
	- 3 points: B, C, M, P
	- 4 points: F, H, V, W, Y
	- 5 points: K
	- 8 points: J, X
	- 10 points: Q, Z
```

* Assign seven tiles chosen randomly from the english alphabet to a player's rack.
* In the real game, tiles are taken at random from a 'bag' containing a fixed number of each tile. Assign seven tiles to a rack using a bag containing this distribution:

```
	- 12 tiles: E
	- 9 tiles: A,I
	- 8 tiles: O
	- 6 tiles: N,R,T
	- 4 tiles: L,S,U,D
	- 3 tiles: G
	- 2 tiles: B,C,M,P,F,H,V,W,Y
	- 1 tiles: K,J,X,Q,Z
```

* Find a valid word formed from the seven tiles. A list of valid words can be found in `twl06.txt`.
* Find the longest valid word that can be formed from the seven tiles.
* Find the highest scoring word that can be formed.
* Find the highest scoring word if any one of the letters can score triple.
* For discussion: how would we adapt our solution for a multiplayer environment?
