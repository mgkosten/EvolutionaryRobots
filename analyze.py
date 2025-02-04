import numpy
import matplotlib.pyplot as plt

backLegSensorValues = numpy.load('data/sensorValues.npy')

plt.plot(backLegSensorValues)

print(backLegSensorValues)

plt.show()