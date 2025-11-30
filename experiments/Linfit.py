import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

targetValue     = [1.0,     4.0,    6.0,    10.0]
measuredValues  = [1.2345,  4.545,  6.6788, 10.5467]

regression = linregress(targetValue,measuredValues)

plottingLineX = np.linspace (min(min(targetValue,measuredValues)),max(max(targetValue,measuredValues)),1000)
plottingLineY = regression.slope * plottingLineX + regression.intercept

print(f"Regression slope: {regression.slope} intercept {regression.intercept}")

plt.plot(plottingLineX,plottingLineY)
plt.plot(targetValue,measuredValues,'ro')
plt.show()