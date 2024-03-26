import numpy as np
from optimizer import newton_1D

class fib:
    """ Fibonacci objective function """
    def __init__(self, num):
        self.num = num
        self.idx = Ellipsis
        
    def __call__(self, x):
        # Only valid for large x
        return self.fibo(x) - self.num[self.idx]

    @classmethod
    def fibo(self, x):
        return 1 / np.sqrt(5) * (((1 + np.sqrt(5)) / 2) ** x)

    @classmethod
    def grad(cls,x):
        return 1 / np.sqrt(5) * (np.log(((1 + np.sqrt(5)) / 2)) * ((1 + np.sqrt(5)) / 2) ** x)

    def idx_hook(self, opt):
        self.idx = opt.active_idx

def post(opt):
    opt.x = np.rint(opt.x)


sol = np.random.randint(200,500, (7,))
sol[0] = 456

num = fib.fibo(sol)
x0 = 500 * np.ones(num.shape[0])
f = fib(num)   
opt = newton_1D(f, hooks=[f.idx_hook], 
                post_processing=post,
                max_it=1e4)
sol_newton = opt.optimize(x0=x0, verbosity = 0)

print(30*'=')
print('Finished after: ' + str(opt.it) + ' Iterations.')
print('Newton Solution: ' +str(sol_newton))
print('True Solution: ' + str(sol))
print('Error: ' + str(np.abs(sol_newton - sol).max()))