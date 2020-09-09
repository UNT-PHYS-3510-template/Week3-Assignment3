# Week 3 Assignment 2

Given a set of function f defined on a close interval \[a,b\], we want to compute its mean value in the interval. We can imagine two alternative algorithms:

1. We divide the interval into a regular set of n equispaced points. We compute the value of the function at these points and take its mean.

2. We randomly select n points within the interval. We compute the value of the function at these points and take its mean.

Which of the two approaches gives the most accurate results?

TASK: Use two loops to compute the average of a function in an interval. In the first loop, the function should be evaluated on equispaced points. In the second loop, the function should be evaluated on random points, generated using the numpy.random.uniform(a,b) function. The specific function (sine) and interval (0 to pi) are coded in the assignment file.

EXPECTED OUTCOME: For the given function and interval, the two means should approach the value of 2/pi as the number of points n becomes large. Why is this the result? 
