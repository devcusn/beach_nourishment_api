import sympy as sp


class Volume:
    def __init__(self, A, length_of_beach, total_length, closure_depth_x):
        self.init = True
        self.length_of_beach = length_of_beach
        self.total_length = total_length
        self.A = A
        self.closure_depth_x = closure_depth_x

    def integrate(self, start, end, A):
        y = sp.Symbol('y')
        f = A * y**(2/3)
        integral = sp.integrate(f, (y, start, end))
        res = integral.evalf()
        return res

    def getVolume(self):
        c1 = self.integrate(0, 233.8, self.A)-self.integrate(0, 146.4, self.A)
        c1_c2 = self.integrate(0, 414.8,  self.A) - \
            self.integrate(0, 327.4, self.A)
        c1_c2_c3 = self.integrate(0, self.closure_depth_x + self.length_of_beach, self.A) - \
            self.integrate(0,  self.closure_depth_x, self.A)
        c4 = self.length_of_beach
        print(c1_c2_c3)
        total = (c1_c2_c3 + c4) * self.total_length
        return float(total)
