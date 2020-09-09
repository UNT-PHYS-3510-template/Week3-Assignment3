# Week 3 Assignment 1
# Given a function f and a closed interval [a,b]. copmute the mean value of the function on the interval using two alterative approaches:
# 1. compute the mean over n equispaced points in the interval
# 2. compute the mean over n random points in the interval
#
# Authors: Oliviero Andreussi, Student
# 
# Variables: 
#   f: arbitrary function
#   a/b: left/right border of the interval
#   n: number of intervals used in the calculation
#   exact_result: analytic result of the definite integral
#   numerical_integral: numerical result of the definite integral using midpoint rule
#
import numpy as np
f=
a=
b=
n= 
exact_result= # this should be the exact analytic result of the integration

dx=(b-a)/n
numerical_integral=0.0
for j in range(n):
    numerical_integral+=f(a+(j+0.5)*dx)*dx

print("With n = {:10n} points the error of midpoint integration is equal to {: .3e}".format(n,numerical_integral-exact_result))

