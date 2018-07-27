import matplotlib.pyplot as plt
plt.style.use('miles')
import numpy as np
import os

t = np.arange(0.0, 0.9, 0.01)

fig, ax = plt.subplots()

# Variable beta
for B in [0.01, 0.1, 0.5, 0.9]:
	v = -np.log(1-t) - B*t
	ax.plot(t, v, label=r'$\beta = {}$'.format(B))

ax.set(xlabel = '$t_n$', ylabel = '$v_n$')
ax.grid()
ax.legend()

filename = "rocket fig1"
fig.savefig(filename + ".pdf")
os.system("open '" + filename + "'.pdf")


# Big beta
plt.cla()

B = 2
v = -np.log(1-t) - B*t
ax.plot(t, v)

ax.set(xlabel = '$t_n$', ylabel = '$v_n$')
ax.grid()

filename = "rocket fig2"
fig.savefig(filename + ".pdf")
os.system("open '" + filename + "'.pdf")