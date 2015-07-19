# Cycling manager

Imagine we are the manager of a cycling team that is in a multiple stage race. We want to write a program that will help us understand what our team tactics should be.

## Assumptions

For this problem assume that cyclists can accelerate instanteously to whatever speed they want and they can sustain any speed indefinitely without tiring. Our race is happening on a flat road with no curves so we do not have to worry about velocity (or alternatively we can use the terms velocity and speed interchangeably).

For units of distance use meters, for time use seconds.

Distance travelled can be calculated by multiplying speed by time: d = v * t.

*Note*: all the speeds in the examples are quite slow because they are around the value of one. Feel free to multiple them by 5 or 10 if you want.

## Race order

The first thing we would like to have is the ability to say given the current race order what will the race order be in the future?

We can model the cyclist as having a name (a single lowercase letter); a current speed; a current position in the race.

We would like to have a program that takes the current state of the race and a number of minutes in the future and generates a report on what the predicted state of the race. The prediction should list the new race order from first to last with the id of the cyclist and the change in their race position.

## Example

We have three cyclists a, b and c. The current race order is b, a, c. b is going 1.5m a second, a is 1.9 m/s and c is 2 m/s. Each cyclist is exactly 20 meters apart.

After 1 minute the race order should be: b, a, c

After 5 minutes the race order should be: c, a, b.

If each cyclist is 100 meters apart though:

After 3 minutes the race order is: b, a, c

After 5 minutes the race order is: a, b, c

After 7 minutes the race order is: a, c, b

After 20 minutes the race order is: c, a, b

## Race to the finish

Being able to predict the future order is great but it would be more useful to understand what tactics we should send to the team for the finish. When the lead rider reaches the 20km mark we need to send instructions to our team.

Update the model so that: each rider belongs to a team designated by a single uppercase letter, each rider has a distance from the end of the race, imagine we know the top speed of each rider in the race can achieve and add that to the model as well.

The time taken to travel a distance is the distance divided by speed or:
t = d / v

### Goals

Each rider would like to finish first, if they cannot finish first they would like to try to finish within five minutes of the first rider. If they cannot do either of those they should just remain at their current speed.

We should assume that all the teams will send the "right" orders to their teams at exactly the same time.

Write a program that tells each member of the team the minimum speed they need to go to achieve their goal.

It should also generate a prediction of the final race order and the difference in times between the finishers.

### Examples

As a trivial example if all riders have the same maximum speed and they are all travelling at 1m/s if the first rider is 20000 meters ahead of the second rider then no-one should change their speed.

Now imagine we have riders a, b, c and d. Team A consists of a and b. Team B of c and d.

All of the riders are current 50m apart, the race order is c, a, d, b. All are current travelling at 1 m/s.

a has a maximum speed of 1.5 m/s, b 1.8 m/s, c 2.4 m/s and d 2.5/ms.

The instructions should be for c and d to travel at their maximum speed and for a and b to maintain their current speed.

The final race order will be d, c, b, a.

The time differences will be ~ 4 minutes 48 seconds between d and c.

~34 minutes 30 seconds between d and b

~46 minutes 45 seconds between d and a

## Bonus question

In the example above d and c ended up racing one another to the finish despite being in the same team. Can you modify your problem so that it can calculate the minimum speed required for c to beat b and a and hence for all of team B to finish before team A?




