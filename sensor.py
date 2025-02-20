import numpy 
import pyrosim.pyrosim as pyrosim
import constants as c
class SENSOR:

    def __init__(self, linkName):
        self.linkName = linkName
        self.value = numpy.zeros(c.loop_iterations)

    def Get_Value(self, t):
        self.value[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        # if t == c.loop_iterations - 1:
        #     print(self.value)
        
    def Save_Values(self, sensor_filename):
        filename = f"data/{sensor_filename}SensorValues.npy"
        numpy.save(filename, self.value, allow_pickle=False)