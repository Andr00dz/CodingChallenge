from math import sqrt
from math import log

# My favourite Fibonacci number is fib(n)=8.889533109425357e+94.
# Unfortunately, I forgot what n is.
# Maybe you can help me find the correct value of n.
# Only a true mathematician is able to solve this without brute-force.
# Apply Newton's method for this problem.

def fib(x):
    return 1 / sqrt(5) * (((1 + sqrt(5)) / 2) ** x)     # Only valid for large x

def fibDeriv(x):
    # Compute derivative of fib
    return

def fibNewton():
    num = 8.889533109425357e+94  # My favourite Fibonacci number
    sol = 450  # Good initial guess. I tested n<450 by hand and couldn't find the correct one.
    for i in range(23):  # Do exactly 23 iterations and hope for convergence
        # Compute Newton update with sol
        sol =
        print(sol)
    return int(sol)

n = fibNewton()