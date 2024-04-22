

class Territory:
    def __init__(self, coords, A, z, lob):
        self.coords = coords
        self.A = A
        self.z = z
        self.length_of_beach = lob

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

    def below_or_above(self, coord, y2, beach_length):
        x = coord[0]
        y = coord[1]
        z = coord[2]
        calc = self.point_position_relative_to_line([x-beach_length, y], y2)
        if calc == "Below" or calc == "On":
            return [x, y, z * -1, "orange"]
        else:
            return [x, y, z * -1, "blue"]

    def generate_inside_coordinates(self, coordinates, y, z=10, beach_length=20):
        z_coord = z * -1
        c1 = coordinates[1]
        c2 = coordinates[2]
        coords = []
        inc_dec = 1
        z = 0

        while z >= z_coord:
            i = 0
            while i < c1[0] + beach_length:
                j = 0
                while j < c2[1]:
                    if (i < beach_length):
                        coords.append([i, j, z*-1, 'orange'])
                    else:
                        coords.append(self.below_or_above(
                            [i, j, z], y, beach_length))
                    j += inc_dec
                i += inc_dec
            z -= inc_dec
        return coords

    def generate_inside_coordinates_3d(self, coordinates, y, z=10):

        coords = []
        last_z = 0
        last_x = 0
        inc_or_dec = 'inc'
        for i in range(len(coordinates)):
            if (i + 1 < len(coordinates)):
                coord_1 = coordinates[i]
                coord_2 = coordinates[i+1]
                x_difference = abs(coord_1[0][0] - coord_2[0][0])
                z_difference = abs(coord_1[0][2] - coord_2[0][2])
                x_inc_init = 0
                x_inc = abs(x_difference / z_difference)
                closure_depth = coord_1[2][1]
                for z in range(last_z, last_z + z_difference):
                    for x in range(last_x, last_x + int(coord_1[1][0])):
                        for y in range(int(coord_1[2][1])):
                            coords.append(self.below_or_above(
                                [x + x_inc_init, y, z], closure_depth))
                    x_inc_init += x_inc
            last_z = z_difference
            last_x = x_difference
        return coords

    def get_territory_matris(self):
        return self.generate_inside_coordinates(self.coords[0], self.coords[0][2][1], self.z, self.length_of_beach)

    def get_territory_matris_3d(self):
        return self.generate_inside_coordinates_3d(self.coords, self.coords[0][2][1], self.z)
