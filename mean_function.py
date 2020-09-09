# Week 3 Assignment 1
# Given a function f and a closed interval [a,b]. copmute the mean value of the function on the interval using two alterative approaches:
# 1. compute the mean over n equispaced points in the interval
# 2. compute the mean over n random points in the interval
#
# Authors: Oliviero Andreussi, Student
# 
# Variables: 
#   f: arbitrary function (in the assignment this is set to be the numpy.sin() function)
#   a/b: left/right border of the interval
#   n: number of points used in the calculation
#   fmean_structured: mean from n equispaced points
#   fmean_random: mean from n random points
#
# Expected Outcome: 
#   for the given function and interval, the result should approach 2/pi as n becomes large
#
import numpy as np
f=np.sin
a=0.0
b=np.pi

fmean_structured = 0.0
fmean_random = 0.0

# The following statements are meant to check the error of the numerical calculations with respect to the analytic result
# The analytic result implemented only applies to the given function and interval
error_structured = fmean_structured*np.pi - 2.0
error_random = fmean_random*np.pi - 2.0
print("The error of the first approach is  = {:.3e}".format(error_structured))
print("The error of the second approach is = {:.3e}".format(error_random))
