import matplotlib.pyplot as plt
plt.style.use('miles')
import numpy as np
import os

t = np.arange(0,1.1,0.1)
y = [1.67203, \
     1.79792, \
     2.37791, \
     2.66408, \
     2.11245, \
     2.43969, \
     1.88843, \
     1.59447, \
     1.79340, \
     1.07810, \
     0.21066]

fig, ax = plt.subplots()
ax.plot(t, y, 'o')

t = np.arange(0,1.02,0.02)
y = -5.20174*t**2 + 3.90148*t + 1.654338
ax.plot(t, y)

ax.set(xlabel = '$t$', ylabel = '$y$')
ax.grid()

filename = "project1 fig1"
fig.savefig(filename + ".pdf")
os.system("open '" + filename + "'.pdf")