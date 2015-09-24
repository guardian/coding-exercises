# Cycling manager

Imagine we are the manager of a cycling team that is in a multiple stage race. We want to write a program that will help us understand what our team tactics should be.

## Assumptions

For this problem assume that cyclists can accelerate instanteously to whatever speed they want and they can sustain any speed indefinitely without tiring. Our race is happening on a flat road with no curves so we do not have to worry about velocity (or alternatively we can use the terms velocity and speed interchangeably).

For units of distance use meters, for time use seconds.

Distance travelled can be calculated by multiplying speed by time: d = v * t.

## Race order

The first thing we would like to have is the ability to say given the current race order what will the race order be in the future?

We can model the cyclist as having a name (a single lowercase letter); a current speed; a current position in the race.

We would like to have a program that takes the current state of the race and a number of seconds in the future and generates a report on what the predicted state of the race. The prediction should list the new race order from first to last with the id of the cyclist and the change in their race position.

### Example

We have three cyclists a, b and c. The current race order is b, c, a. b is going 10m a second, a is 5 m/s and c is 7 m/s.

Each cyclist starts exactly 200 meters apart.

After 1 minute the race order should be: b, c, a

After 5 minutes the race order should be: a, c, b

After 90 seconds the race order should be: c, a, b

## Race to the finish

A race has a number of metres left before the finish line and a rider has a maximum velocity that they are capable of. Add both of these ideas to your model.

Now amend your code so it is possible to select a rider and the program decides whether that rider should change speed to win the race (assuming that no other rider changes their speed).

### Example

Riders a b and c are riding in alphabetical order and are 2000m from the finish line. All of them are travelling at 5m/s. The maximum speeds for the riders are: a 12m/s, b 9m/s and c 7m/s.

If all the riders are 200m apart then c should accelerate to their top speed as they will win the race. b should also accelerate. c should stay at the same speed as they are already winning.

If a is 600m behind b and c is 200m ahead of a. a should not accelerate but b should.


