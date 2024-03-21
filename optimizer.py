import numpy as np

class optimizer:
    def __init__(self, f, max_it = 100, hooks = None, post_processing=None):
        self.f = f
        self.max_it = max_it
        self.hooks = [] if hooks is None else hooks
        self.post_processing = (lambda x:x)\
            if post_processing is None else post_processing

    
    def step(self,):
        raise NotImplementedError('The class ' + __class__.name + 
                                  ' does not have a step method')
        
    def optimize(self, verbosity=1, **kwargs):
        self.init_run(**kwargs)
 
        while not self.terminate():
            self.pre()
            self.step()
            if verbosity > 0:
                self.print_step()
            self.post()
        return self.x
      
    def hook_eval(self,):
        for hook in self.hooks:
            hook(self) 
    
    def pre(self,):
        self.x_old = self.x.copy()
        self.hook_eval()
    
    def post(self,):
        self.it[self.active_idx] += 1
        self.post_processing(self)
            
    def print_step(self,):
        print(self.it)
    
    def terminate(self,):
        return True
    
    def init_run(self,):
        self.it = 0

class newton_1D(optimizer):
    def __init__(self, f, **kwargs):
        super().__init__(f, **kwargs)
        self.terms = [
            lambda opt: opt.it > opt.max_it,
            lambda opt: np.abs(opt.x - opt.x_old) < 1e-5]
        
    def step(self,):
        # newton update
        xx = self.x[self.active_idx]
        self.x[self.active_idx] += (
            -self.f(xx)/self.f.grad(xx)
        )
        
    def init_run(self, **kwargs):
        self.x = kwargs.get('x0', np.zeros(1,))
        if isinstance(self.x, (int,float)):
            self.x = self.x * np.ones(1,)
        self.x_old = self.x.copy()+1e10 # this is hacky, can do better
        self.it = np.zeros((self.x.shape[0]))
        
    def terminate(self,):
        self.select_active_idx()
        return (self.active_idx.shape[0] == 0)
        
    def select_active_idx(self,):
        t = np.zeros((self.x.shape[0]), dtype=bool)
        for term in self.terms:
            t = np.logical_or(t, term(self))

        self.active_idx = np.where(~t)[0]
        
    def print_step(self,):
        print(20*'-')
        print('Iteration: ' + str(self.it))
        print('Solution: ' +str(self.x))
        