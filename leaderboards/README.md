# Leaderboards

We want to try and ride the gamification wave and produce "leaderboards as a service".

Create a simple leaderboard model and add some scores to it. The leaderboard should be sorted by score, highest to lowest.

If a player adds a new score only their highest score should be recorded.

You can either implement this a service or try and implement a UI to demonstrate the functionality. The choice is yours.

## Dealing with ties

If multiple players share the same score we should order the entries according to who recorded the score first. Players with the same score should share the same position on the leaderboard though.

Position numbering after a tie should reflect the number of people who have scored higher than the score. As a simple example if A has scored 5; B, C and D have scored 4 and E has scored 2 then the positions should be 1, 2, 2, 2, 5.

## Leagues

We now want to be able to model "leagues". These are groups of players who can access a leaderboard that is limited just to the players who are members of the same league.

A player may be a member of many leagues.

Create a model for leagues and use it to create a league leaderboard without duplicating the global score data.

