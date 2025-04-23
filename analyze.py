import numpy
import matplotlib.pyplot as plt

# backLegSensorValues = numpy.load('data/backLegSensorValues.npy')
# frontLegSensorValues = numpy.load('data/frontLegSensorValues.npy')

# plt.plot(backLegSensorValues, label = "BackLeg Sensor", linewidth = 4)

# plt.plot(frontLegSensorValues, label = "FrontLeg Sensor")

# # print(backLegSensorValues)

# plt.legend()
# plt.show()

generations = []
fitness_values = []

with open("fitnessTracking.txt", "r") as file:
    for line in file:
        if line.strip():
            gen_str, fit_str = line.strip().split(',')
            generations.append(int(gen_str))
            fitness_values.append(float(fit_str))

# Plotting
plt.plot(generations, fitness_values, label="Fitness", linewidth=2, marker='o')
plt.title("Fitness Over Generations")
plt.xlabel("Generation")
plt.ylabel("Fitness")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()