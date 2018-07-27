import matplotlib.pyplot as plt
plt.style.use('miles')
import numpy as np
import os

numlines = 7 # number of curves to show in parametric plot
t = np.arange(0,2,0.1)
interval = 2*np.pi/numlines

# Parametric plot
fig, ax = plt.subplots()

for i in range(numlines):
	x = np.cos(i*interval) - np.cos(t+i*interval)
	y = -1*np.sin(i*interval) + np.sin(t+i*interval)
	ax.plot(x, y)
ax.set(xlabel = '$x_n$', ylabel = '$y_n$')
ax.grid()


filename = "coriolis parametric"
fig.savefig(filename + ".pdf")
os.system("open '" + filename + "'.pdf")


# Separate time plots
plt.cla()

t = np.arange(0,5,0.1)
B = np.pi/2
x = np.cos(B) - np.cos(t+B)
y = -1*np.sin(B) + np.sin(t+B)

line_x = ax.plot(t, x, label='$x_n(t_n)$')
line_y = ax.plot(t, y, label='$y_n(t_n)$')
ax.set(xlabel = '$t_n$')
ax.grid()
ax.legend()

filename = "coriolis time"
fig.savefig(filename + ".pdf")
os.system("open '" + filename + "'.pdf")