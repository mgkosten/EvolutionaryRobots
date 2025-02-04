import numpy
import matplotlib.pyplot as plt

backLegSensorValues = numpy.load('data/backLegSensorValues.npy')
frontLegSensorValues = numpy.load('data/frontLegSensorValues.npy')

plt.plot(backLegSensorValues)

plt.plot(frontLegSensorValues)

# print(backLegSensorValues)

plt.show()