import numpy as np
import matplotlib.pyplot as plt


def dms2degrees(dms):
    return dms[0] + dms[1]/60 + dms[2]/3600


lat1 = dms2degrees([41, 14, 42.84])
lon1 = dms2degrees([29, 5, 35.11])
lat2 = dms2degrees([41, 14, 37.93])
lon2 = dms2degrees([29, 5, 47.17])

zoomlat1 = dms2degrees([41, 14, 22.47])
zoomlat2 = dms2degrees([41, 14, 23.13])

latAnchorage = 41.2
lonAnchorage = 29.3

plt.figure(1)

# Plotting the main map
map_ax = plt.subplot(2, 2, 1)
print(lat1, lat2, lon1, lon2)
map_ax.plot([lat1, lat2], [lon1, lon2], 'black', linewidth=1)
map_ax.plot([lat1, latAnchorage], [lon1, lonAnchorage], '-*')
map_ax.set_xlabel('Latitude')
map_ax.set_ylabel('Longitude')
map_ax.set_title('Map')
map_ax.grid(True)
map_ax.set_aspect('equal', adjustable='box')

# Plotting transect AA
A = 0.1
dx = 0.1
xmax = 300
x = np.arange(0, xmax + dx, dx)
heq1 = -A * np.power(x, 2/3)

transect_aa_ax = plt.subplot(2, 2, 2)
transect_aa_ax.plot(x, heq1, 'black', linewidth=2)
transect_aa_ax.set_xlabel('x (m)')
transect_aa_ax.set_ylabel('h (m)')
transect_aa_ax.set_title('Transect AA')
transect_aa_ax.grid(True)

# Plotting transect BB
heq2 = -A * np.power(x, 2/3)
transect_bb_ax = plt.subplot(2, 2, 3)
transect_bb_ax.plot(x, heq2, 'black', linewidth=2)
transect_bb_ax.set_xlabel('x (m)')
transect_bb_ax.set_ylabel('h (m)')
transect_bb_ax.set_title('Transect BB')
transect_bb_ax.grid(True)

# Plotting transect CC
heq3 = -A * np.power(x, 2/3)
transect_cc_ax = plt.subplot(2, 2, 4)
transect_cc_ax.plot(x, heq3, 'black', linewidth=2)
transect_cc_ax.set_xlabel('x (m)')
transect_cc_ax.set_ylabel('h (m)')
transect_cc_ax.set_title('Transect CC')
transect_cc_ax.grid(True)

plt.tight_layout()
plt.show()
