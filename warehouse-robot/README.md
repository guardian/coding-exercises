# Robot Warehouse

We have installed a robot in our warehouse and now we need to be able to send it commands to control it. We need you to implement the control mechanism.

For convenience the robot moves along a grid in the roof of the warehouse and we have made sure that all of our warehouses are built so that the dimensions of the grid are 10 by 10. We've also made sure that all our warehouses are aligned along north-south and east-west axes.

All of the commands to the robot consist of a single capital letter and different commands are dilineated by whitespace.

## Part One

The robot should accept the following commands:

* N move north
* W move west
* E move east
* S move south

### Example command sequences

The command sequence: "N E S W" will move the robot in a full square, returning it to where it started.

If the robot starts in the south-west corner of the warehouse then the following commands will move it to the middle of the warehouse.

"N E N E N E N E"

### Requirements

* Create a way to send a series of commands to the robot
* Make sure that the robot doesn't try to move outside the warehouse

## Part two

The robot is equipped with a lifting claw which can be used to move crates around the warehouse. We track the locations of all the crates in the warehouse.

Model the presence of crates in the warehouse. Initially one is in the centre and one in the north-east corner.

Extend the robot's commands to include the following:

* G grab a crate and lift it
* D drop a crate gently to the ground

There are some rules about moving crates:

* The robot should not try and lift a crate if it already lifting one
* The robot should not lift a crate if there is not one present
* The robot should not drop a crate on another crate!

## Part three

We have expanded the robot's grid system to include diagonal tracks. Modify the robot's movement so that it can take advantage of the new diagonals. We don't want to change all the movement programmes though so don't change the syntax of the commands we send.

So for example if the robot starts in the south-west corner of the warehouse then issuing the command "E N" should move the robot to the same place as if it moved east once and north once but it should only move once.

