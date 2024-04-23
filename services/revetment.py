class Revetment:
    def __init__(self, revetment_depth, A):
        self.revetment_depth = revetment_depth
        self.A = A

    def get_position_of_revetment(self):
        return pow(self.revetment_depth / self.A, 3/2)
