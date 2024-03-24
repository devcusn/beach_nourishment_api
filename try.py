import numpy as np
from itertools import product
z_coord = 40
inc_dec = 1

coords = []
z = 0
while z < z_coord:
    i = 0
    while i < 10:
        j = 0
        while j <= 300:
            coords.append([i, j, z, "orange"])
            j += inc_dec
        i += inc_dec
    z += inc_dec

print(len(coords))


# Assuming coords is the numpy array containing the coordinates

# Save the coords array to a text file
np.savetxt('coords.txt', coords, fmt='%s', delimiter=',')
