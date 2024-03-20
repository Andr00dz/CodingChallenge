from math import sqrt
from math import log

def fib(x):
    # Only valid for large x
    return 1 / sqrt(5) * (((1 + sqrt(5)) / 2) ** x)

def fibDeriv(x):
    return 1 / sqrt(5) * (log(((1 + sqrt(5)) / 2)) * ((1 + sqrt(5)) / 2) ** x)

def fibNewton():
    num = 8.889533109425357e+94  # My favourite Fibonacci number
    sol = 450  # Good initial guess
    for i in range(22):
        sol = sol - (fib(sol) - num) / fibDeriv(sol)
        print(sol)
    return int(sol)

n = fibNewton()