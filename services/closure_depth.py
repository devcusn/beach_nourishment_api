class ClosureDepth:
    def __init__(self):
        self.gravity = 9.81

    def getClosureDepth(self, h_s, t_m):
        res = 2.28 * h_s - 68.5*((h_s**2)/(self.gravity * (t_m ** 2)))
        return res

    def get_water_depth(self, A, y):
        h = A * y**(2/3)
        return h
