

class Territory:
    def __init__(self, coords, A, z):
        self.coords = coords
        self.A = A
        self.z = z

    def point_position_relative_to_line(self, point, y):
        y_on_line = -1 * self.A * pow(point[0], 2 / 3) + y
        if point[1] == 0:
            return "Below"
        elif point[1] < y_on_line:
            return "Below"
        elif point[1] > y_on_line:
            return "Above"
        else:
            return "On"

    def below_or_above(self, coord, y2):
        x = coord[0]
        y = coord[1]
        z = coord[2]
        calc = self.point_position_relative_to_line([x, y], y2)
        if calc == "Below" or calc == "On":
            return [x, y, z * -1, "orange"]
        else:
            return [x, y, z * -1, "blue"]

    def generate_inside_coordinates(self, coordinates, y, z=10):
        z_coord = z * -1
        c1 = coordinates[1]
        c2 = coordinates[2]
        coords = []
        inc_dec = 1
        z = 0
        while z >= z_coord:
            i = 0
            while i < c1[0]:
                j = 0
                while j < c2[1]:
                    coords.append(self.below_or_above([i, j, z], y))
                    j += inc_dec
                i += inc_dec
            z -= inc_dec
        return coords

    def get_territory_matris(self):
        return self.generate_inside_coordinates(self.coords, self.coords[2][1], self.z)
