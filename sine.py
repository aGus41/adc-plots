import numpy as np

import matplotlib.pyplot as plot
import math 

time  = np.arange(0, 0.03, 0.0001);
freq = 2*np.pi*100

vg   = 4*np.cos(time*freq)
vo   = 4/math.sqrt(2)*np.cos(time*freq+np.pi/2)

plot.plot(time, vg)

plot.plot(time, vo)

plot.xlabel('Time (s)')

plot.grid(True, which='both')

plot.legend(['Vg','Vo'])
 

plot.show()
