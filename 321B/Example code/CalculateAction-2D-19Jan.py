import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt



def action(ax, ay):
    mass = 1
    t1 = 0
    t2 = 3
    x1 = 0
    y1 = 1
    x2 = 10
    y2 = 0
    vx = (x2-x1)/(t2-t1) - 1/2.*ax*(t2-t1)
    vy = (y2-y1)/(t2-t1) - 1/2.*ay*(t2-t1)
    postime = np.linspace(0, t2-t1, 1000)
    
    xpos = x1 + vx*postime + 1/2*ax*postime**2
    vxpos = vx + ax*postime
    
    ypos = y1 + vy*postime + 1/2*ay*postime**2
    vypos = vy + ay*postime
    
    Lagrangian = 1/2*mass*( vxpos**2 + vypos**2) - mass*9.8*ypos
    return Lagrangian.sum()*(t2-t1)/1000

action_vectorized = np.vectorize(action)

Ax = np.linspace(-10,10,100)
Ay = np.linspace(-20, 0, 100)

X, Y = np.meshgrid(Ax, Ay)
Z = action_vectorized(X, Y)

plt.contourf(X,Y,Z)

plt.show()
    




