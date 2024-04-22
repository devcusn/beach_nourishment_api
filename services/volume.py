import sympy as sp


class Volume:
    def __init__(self, A, length_of_beach, total_length):
        self.init = True
        self.length_of_beach = length_of_beach
        self.total_length = total_length
        self.A = 0.09

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
        c1_c2_c3 = self.integrate(0, 502.2, self.A) - \
            self.integrate(0, 414.8, self.A)
        c4 = self.length_of_beach
        total = (c1_c2_c3 + c4) * self.total_length
        return int(total)
