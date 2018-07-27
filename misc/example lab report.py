import matplotlib.pyplot as plt
plt.style.use('miles')
import numpy as np
import os

t = [0.4240, 0.4060, 0.3530, 0.3374, 0.3040, 0.2809, 0.2410, 0.2121]
y = [0.8800, 0.8100, 0.6100, 0.5535, 0.4450, 0.3900, 0.2900, 0.2200]

y_th = np.arange(0.2,0.9,0.01)
t_th = np.sqrt(2/9.81*y_th)

fig, ax = plt.subplots()
line_x = ax.plot(y, t, 'o', label = 'observed')
line_th = ax.plot(y_th, t_th, label = 'theoretical')

ax.set(xlabel = '$y_0$', ylabel = r'$t_\mathdefault{avg}$')
ax.grid()
ax.legend()

filename = "example lab report plot"
fig.savefig(filename + ".pdf")
os.system("open '" + filename + "'.pdf")