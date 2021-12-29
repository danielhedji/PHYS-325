import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

# start with calculate action for ball at y=1 at 0s
# y=0 at 3s
# find action as a function of ay

def action( ay ):
    # write position as a function of time
    # velocity as a function of time, use to build up L
    # know initial and final positions, so needd to find initial vyo
    
    # hard code initial and final times
    t0 = 0
    t1 = 3
    
    #hard code initial and final positions
    y0 = 1
    y1 = 0
    
    #based on final and initial positions I can work out vyo
    vyo = (y1 - y0)/(t1-t0) - 1/2.*ay*(t1-t0)
    
    #make up a set of numbers to be my time
    time = np.linspace(0,t1-t0,1000)
    
    ypos = y0 + vyo*time + 1/2*ay*time**2
    vy = vyo + ay*time
    
    mass = 1
    # this gives me L as a function of time
    L = 1/2*mass*vy**2 - mass*9.8*ypos
    ACT = L.sum()*(time[1]-time[0])
    
    return ACT

action_v = np.vectorize(action)

AY = np.linspace(-15,10,100)

plt.plot(AY,action_v(AY))
plt.show()











