'''
==========================
3D voxel / volumetric plot
==========================

Demonstrates plotting 3D volumetric objects with ``ax.voxels``
'''

import matplotlib.pyplot as plt
import numpy as np

def ply_to_voxel(file_path):
    txt_file = open(file_path)


# prepare some coordinates
x, y, z = np.indices((10, 10, 10))

# draw cuboids in the top left and bottom right corners, and a link between them
# cube1 = (x < 3) & (y < 3) & (z < 3)
# cube2 = (x >= 5) & (y >= 5) & (z >= 5)
# link = abs(x - y) + abs(y - z) + abs(z - x) <= 2
goal = ply_to_voxel('dog.ply')

# combine the objects into a single boolean array
voxels = goal

# set the colors of each object
colors = np.empty(voxels.shape, dtype=object)
colors[goal] = 'red'

# and plot everything
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.voxels(voxels, facecolors=colors, edgecolor='r')

plt.show()