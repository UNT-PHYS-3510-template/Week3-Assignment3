# Week 3 Assignment 3

In the previous assignment we tested two ways to compute the average value of a function within an interval. This can be useful to estimate the definite integral of the function:

<a href="https://www.codecogs.com/eqnedit.php?latex=\int_a^bf(x)dx\approx&space;(b-a)\bar{f}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\int_a^bf(x)dx\approx&space;(b-a)\bar{f}" title="\int_a^bf(x)dx\approx (b-a)\bar{f}" /></a>

However, there are less approximate ways of computing the integral of a function using a numerical algorithm. One of the simplest is the midpoint rule, where the integration domain is split into a set of regular and small intervals, and the area below the function within each interval is estimated from the value of the function in the midpoint (see the following image taken from https://tutorial.math.lamar.edu/classes/calcii/approximatingdefintegrals.aspx)

![midpoint rule](https://tutorial.math.lamar.edu/classes/calcii/ApproximatingDefIntegrals_Files/image001.png)

TASK: In the midpoint.py program you can find the basic loop to perform midpoint integration of a generic function f in a closed interval \[a,b\]. Modify the code to compute the integral of the sine function between 0 and pi. Find a value of the number n of small intervals that is needed to get a result correct up to the 4th decimal digit (i.e. the error is less than 1e-4). 

EXPECTED OUTCOME: For the given function and interval, the two means should approach the value of 2/pi as the number of points n becomes large. Why is this the result? 
