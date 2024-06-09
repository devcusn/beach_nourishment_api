import sympy as sp


class Volume:
    def __init__(self, A, length_of_beach, total_length, closure_depth_x, revetment_position):
        self.init = True
        self.length_of_beach = length_of_beach
        self.total_length = total_length
        self.A = A
        self.closure_depth_x = closure_depth_x
        self.revetment_position = revetment_position

    def integrate(self, start, end, A):
        y = sp.Symbol('y')
        f = A * y**(2/3)
        integral = sp.integrate(f, (y, start, end))
        res = integral.evalf()
        return res

    def getVolume(self):
        c1 = self.integrate(0, self.revetment_position +
                            self.length_of_beach, self.A)-self.integrate(0, self.revetment_position, self.A)

        c1_c2 = self.integrate(0, self.closure_depth_x,  self.A) - \
            self.integrate(0, self.closure_depth_x -
                           self.length_of_beach, self.A)
        c1_c2_c3 = self.integrate(0, self.closure_depth_x + self.length_of_beach, self.A) - \
            self.integrate(0,  self.closure_depth_x, self.A)
        c2 = c1_c2 - c1
        c3 = c1_c2_c3 - c1_c2
        c4 = self.length_of_beach
        total = (c1_c2_c3 + c4) * self.total_length
        return {"volume": float(total), "detail": {
            "c1": float(c1),
            "c2":  float(c2),
            "c3":  float(c3),
            "c4":  float(c4)
        }}
