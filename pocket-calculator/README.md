# Pocket calculator

We are going to create an emulation of an old-fashioned pocket calculator.

The calculator is going to have ten registers, numbered 0-9. We can assume our calculator only has one thread so we don't need to worry about locking.

Add the ability to read and write from the registers.

We will fake input to the calculator by creating an input function that takes a sequence of input (bytes, characters, whatever you chose as the type of the registers) and returns a function that will emit the elements of the sequence one at a time.

## Example of the input function's output

f = input(['2', '+', '3']) => function
f() => '2'
f() => '+'
f() => '3'
f() => language appropriate end of iteration or sequence (nil, None, null, etc.)

## Arthimetic

Now implement adding and substracting. The add and subtract operations should take two registers as parameters, applying the operation to the values stored in the two registers.

Next implement multiplication and division, you can implement these how you like but it is fine to have them use the add and subtract operations and to be recursive.

## Parsing

Add an output function that simply prints the value in a specified register.

Using any input format you like and any precedence rules you choose now link the sequence of commands from the input function to the appropriate functions so that when the user wants to add the two numbers 2 and 3 they receive the answer: 5.

## Bonus question

Implement the operations greater than, less than and equal to; all of which operate on registers.

Add them to your input reading functionality so that if the user asks whether 2 is less than 3 they get the answer true and if the say 2 is greater than 3 they get the answer false.

2 should not be equal to 3 and 2 and 3 should both equal themselves.
