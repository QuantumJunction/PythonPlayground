import matplotlib.pyplot as plt
import numpy as np

amplitude = 10
phase = 90/360 * 2 * np.pi
frequency = 5
t = np.linspace(0,4*np.pi, 1000)
y = amplitude * np.sin(frequency * t + phase)

plt.plot(t,y)
plt.show()