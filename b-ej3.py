import numpy as np

import matplotlib.pyplot as plot
import math 

time  = np.arange(0, 0.03, 0.0001);
R=2000
C=0.000001
RC=R*C
vo=1-np.exp((-1/RC)*time)*(1+time/RC)
plot.plot(time, vo)

plot.xlabel('Time (s)')

plot.grid(True, which='both')

plot.legend(['v_o(t)'])
 
plot.show()
