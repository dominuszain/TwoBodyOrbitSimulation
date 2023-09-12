import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

x1 = np.loadtxt('x1.csv')
y1 = np.loadtxt('y1.csv')
x2 = np.loadtxt('x2.csv')
y2 = np.loadtxt('y2.csv')

def animate(i):
    #ln1.set_data([0, x1[i], x2[i]], [0, y1[i], y2[i]])
    point2.set_data(x1[i],y1[i])
    point3.set_data(x2[i],y2[i])
    
fig, ax = plt.subplots(1,1, figsize=(8,8))
ax.set_facecolor('k')
ax.get_xaxis().set_ticks([])    # enable this to hide x axis ticks
ax.get_yaxis().set_ticks([])    # enable this to hide y axis ticks
#ln1, = plt.plot([], [], 'ro--', lw=3, markersize=8)
point2, = ax.plot(0,0, marker="o")
point3, = ax.plot(0,0, marker="o")
ax.set_ylim(-50,200)
ax.set_xlim(-50,400)
ani = animation.FuncAnimation(fig, animate, frames=10000, interval=50)
ani.save('output.gif',writer='pillow',fps=50)
