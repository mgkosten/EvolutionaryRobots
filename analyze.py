import numpy
import matplotlib.pyplot as plt

backLegSensorValues = numpy.load('data/backLegSensorValues.npy')
frontLegSensorValues = numpy.load('data/frontLegSensorValues.npy')

plt.plot(backLegSensorValues, label = "BackLeg Sensor", linewidth = 4)

plt.plot(frontLegSensorValues, label = "FrontLeg Sensor")

# print(backLegSensorValues)

plt.legend()
plt.show()