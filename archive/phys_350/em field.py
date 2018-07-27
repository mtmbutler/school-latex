import matplotlib.pyplot as plt
plt.style.use('miles')
import numpy as np
import os

# Figure 1: x_n and y_n vs t_n
t = np.arange(0.0, 4*np.pi, 0.01)
x = t - np.sin(t)
y = 1 - np.cos(t)

fig, ax = plt.subplots()
line_x = ax.plot(t, x, label='$x_n$')
line_y = ax.plot(t, y, label='$y_n$')

ax.set(xlabel = '$t_n$')
ax.grid()
ax.legend()

filename = "em field fig1"
fig.savefig(filename + ".pdf")
os.system("open '" + filename + "'.pdf")


# Figure 2: y_n vs x_n
plt.cla()
ax.plot(x, y)
plt.ylim((0,2.25))

ax.set(xlabel = '$x_n$', ylabel = '$y_n$')
ax.grid()

filename = "em field fig2"
fig.savefig(filename + ".pdf")
os.system("open '" + filename + "'.pdf")


# Figure 3: x/tau vs t_n for different alpha
plt.cla()
for i in [5.0, 2.0, 1.0, 0.5, 0.1]:
	x = i*(t-np.sin(t))
	ax.plot(t, x, label=r'$\alpha = {}$'.format(i))

ax.set(xlabel = '$t_n$', ylabel = r'$x/\tau$')
ax.grid()
ax.legend()

filename = "em field fig3"
fig.savefig(filename + ".pdf")
os.system("open '" + filename + "'.pdf")


# Figure 4: y/tau vs t_n for different alpha
plt.cla()
for i in [5.0, 2.0, 1.0, 0.5, 0.1]:
	y = i*(1-np.cos(t))
	ax.plot(t, y, label=r'$\alpha = {}$'.format(i))

plt.ylim((0,12))
ax.set(xlabel = '$t_n$', ylabel = r'$y/\tau$')
ax.grid()
ax.legend()

filename = "em field fig4"
fig.savefig(filename + ".pdf")
os.system("open '" + filename + "'.pdf")

# Figure 5: y/tau vs x/tau for different alpha
plt.cla()
for i in [5.0, 2.0, 1.0, 0.5, 0.1]:
	y = i*(1-np.cos(t))
	x = i*(t-np.sin(t))
	ax.plot(x, y, label=r'$\alpha = {}$'.format(i))

plt.ylim((0,12))
ax.set(xlabel = r'$x/\tau$', ylabel = r'$y/\tau$')
ax.grid()
ax.legend()

filename = "em field fig5"
fig.savefig(filename + ".pdf")
os.system("open '" + filename + "'.pdf")