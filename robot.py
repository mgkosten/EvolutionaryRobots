import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT:

    def __init__(self):
        self.robotId = p.loadURDF("body.urdf")
        self.nn = NEURAL_NETWORK("brain.nndf")
        # self.motors = MOTORS()
    
    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
    
    def Sense(self, t):
        # self.values.append(pyrosim.Get_Touch_Sensor_Value_For_Link(self.sensor.linkName))
        for sensor, instance in self.sensors.items():
           instance.Get_Value(t)

    def Prepare_To_Act(self):
        self.joints = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.joints[jointName] = MOTOR(jointName)
    
    def Act(self, t):
        for joint, instance in self.joints.items():
            instance.Set_Value(self, t)
    
    def Think(self):
        self.nn.Update()
        self.nn.Print()
