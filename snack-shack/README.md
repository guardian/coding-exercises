# Snack shack

Hello, the competitive world of software engineering has gotten to me and I have decided to enter the world of fast food!

I am making quick snacks but I would like a program to help organise people's orders and what I should be doing.

## Sandwiches

I can make a sandwich in one minute and then I need 30 seconds to serve the sandwich and take money from the customer.

Can you write a program that takes orders from customers and sequences what I should be doing?

So if I have four sandwich orders the schedule should be:

0:00 4 sandwich orders placed, start making sandwich 1
0:60 serve sandwich 1
1:30 make sandwich 2
2:30 serve sandwich 2
3:00 make sandwich 3
4:00 serve sandwich 3
4:30 make sandwich 4
5:30 serve sandwich 4
6:00 take a well earned break!

## Estimates

With the schedule in place I should be able to predict when people will get their order when they place it.

Modify your program so that when an order is placed it returns an estimate of how long the customer will have to wait from the order being placed to getting their food, based on the current order.

## Fast food, short tempers

People expect to be able to get their sandwich quickly. If they have to wait more than five minutes they will refuse to pay for it. So in the example above sandwich 4 would have been too late.

Modify the order placement so that it rejects orders that cannot be served in time.

## Jacket potatoes

Sandwiches are great but people really want the option of hot food too. I've decided to offer jacket potatoes. Jacket potatoes are pre-baked but need to be heated in my single microwave for 2 and half minutes. I then need 30 seconds to top them and 30 seconds to serve them.

Jacket potatoes go cold again if they are not served within two minutes of being heated.

The good news is that people will wait seven minutes to get a jacket potato.

Please modify the order system to include jacket potatoes.

So if there are orders for two sandwiches and a jacket potato the schedule should be:

0:00 Put jacket potato in microwave
0:01 Make sandwich 1
1:01 Serve sandwich 2
1:31 Make sandwich 2
2:31 Serve sandwich 2
3:01 take jacket potato out of microwave
3:31 top jacket potato
4:01 serve jacket potato
4:31 take a break!

## Inventory

I only have limited ingredients in the shack: I can make 45 sandwiches and 30 jacket potatoes. Orders for something that is sold out should not be accepted and it reflect to the user whether there is an alternative available or whether everything is sold out.

## So popular!

People actually like my sandwiches and potatoes! Some are willing to wait longer to get their order.

Please modify the order system to allow the customer to optionally say how long they are willing to wait for their food. Only reject the order if the current schedule makes it impossible to serve it in the time requested.

## Many microwaves

I have been silly, while there is only one me I can have many microwaves in the shack. Modify the schedule to reflect the fact that I can now microwave two potatoes at a time.

## Advance orders

Some people would like to place an order for collection at a specific time. They will pay in advance so I won't need to serve their order but just have it ready in time.

Change the order placement to allow a preferred time to specified (wait time is irrelevant in this case) if the order can be served within five minutes of the desired time then accept the order and return the actual ready time. 