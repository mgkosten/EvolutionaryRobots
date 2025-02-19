import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
class ROBOT:

    def __init__(self):
        self.robotId = p.loadURDF("body.urdf")
        # self.motors = MOTORS()
    
    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
    
    def Sense(self, t):
        # self.values.append(pyrosim.Get_Touch_Sensor_Value_For_Link(self.sensor.linkName))
        for sensor, instance in self.sensors.items():
           instance.Get_Value(t) 
