#3D
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = plt.axes(projection='3d')
#Randomwalk
import random
import matplotlib.pyplot as plt
import numpy as np
pos_x = 0
pos_y = 0
pos_z = 0
walk = [[pos_x],[pos_y],[pos_z]]
for i in range(10000):
    """Randomize x, y, z"""
    step = random.randint(-1,1)
    pos_x += step
    step = random.randint(-1,1)
    pos_y += step
    step = random.randint(-1,1)
    pos_z += step
    
    """Append to walk"""
    walk[0].append(pos_x)
    walk[1].append(pos_y)
    walk[2].append(pos_z)
px = walk[0]
py = walk[1]
pz = walk[2]
    
ax.plot3D(px, py, pz, 'red')
ax.scatter3D(px, py, pz, c='#00FF0010', marker='.')
