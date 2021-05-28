import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
import math

x = [[30, 30, 30, 30, 30, 30, 30, 30, 30, 30],
     [25, 20, 20, 30, 35, 40, 35, 35, 30, 25],
     [ 0,  0, 30, 15, 30,  0,  0, 15,  0, 15]]

fig = plt.figure()

ax = fig.add_subplot(projection='3d')

def draw():
    for i in range(300):
        x[0] = [k - 0.01 for k in x[0]]
        vertices = [list(zip(x[0], x[1], x[2]))]
        poly = Poly3DCollection(vertices, alpha=0.1)
        poly.set_color('k')
        ax.add_collection3d(poly)

def move(delta):
    x[0] = [i + delta for i in x[0]]

def rotate(delta, x):
    matrix = [[1, 0, 0],
              [0, math.cos(delta), -1 * math.sin(delta)],
              [0, math.sin(delta), math.cos(delta)]]
    return np.dot(matrix, np.array(x))

def drawXY():
    for i in range(300):
        x[0] = [k + 0.01 for k in x[0]]
        vertices = [list(zip(x[0], x[1], [0 for i in x[2]]))]
        poly = Poly3DCollection(vertices, alpha=0.1)
        poly.set_color('tab:pink')
        ax.add_collection3d(poly)

def drawXZ():
    for i in range(300):
        x[0] = [k + 0.01 for k in x[0]]
        vertices = [list(zip(x[0], [60 for i in x[2]], x[2]))]
        poly = Poly3DCollection(vertices, alpha=0.1)
        poly.set_color('tab:pink')
        ax.add_collection3d(poly)

def drawYZ():
    for i in range(300):
        x[0] = [k + 0.01 for k in x[0]]
        vertices = [list(zip([0 for i in x[2]], x[1], x[2]))]
        poly = Poly3DCollection(vertices, alpha=0.1)
        poly.set_color('tab:pink')
        ax.add_collection3d(poly)

draw()

move(30)
x = rotate(0.50, x)
draw()

ax.set_xlim(0,100)
ax.set_ylim(0,100)
ax.set_zlim(0,100)

move(30)
drawXY()
drawXZ()
drawYZ()

plt.show()