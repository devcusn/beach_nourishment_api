class ClosureDepth:
    def __init__(self, params):
        self.gravity = 9.81
        self.k = 0.78
        self.params = params
        self.wave_height = params['wave_height']
        self.wave_period = params['wave_period']
        self.D = params['D']
        self.rho = params['rho']
        self.dfifthy = params['dfifthy']

    def getA(self, D, dfifthy, rho):
        return ((24 * D * dfifthy) / (5 * rho * self.gravity**(3/2) * self.k**2))**(2/3)

    def get_closure_depth(self, A, h_s, t_m):
        res = A * h_s - 68.5*((h_s**2)/(self.gravity * (t_m ** 2)))
        return res

    def get_water_depth(self, A, y):
        h = A * y**(2/3)
        return h

    def get_closure_depth_x(self, closure_depth, A):
        return (closure_depth / A)*(3/2)

    def res(self):
        A = self.getA(self.D,
                      self.dfifthy,
                      self.rho)
        closure_depth = self.get_closure_depth(A,
                                               self.wave_height, self.wave_period)
        closure_depth_x = self.get_closure_depth_x(closure_depth, A)

        return {
            "closure_depth": closure_depth,
            "x": closure_depth_x * -1,
            "A": A
        }
