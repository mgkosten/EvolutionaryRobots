import pybullet as p
import pyrosim.pyrosim as pyrosim
import os
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT:

    def __init__(self, solutionID):
        self.robotId = p.loadURDF("body.urdf")
        self.nn = NEURAL_NETWORK("brain" + str(solutionID) + ".nndf")
        os.system("del brain" + str(solutionID) + ".nndf")
        self.solutionID = solutionID
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
        print(self.joints)
    
    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName).encode('utf-8')
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.joints[jointName].Set_Value(self, desiredAngle)
    
    def Think(self):
        self.nn.Update()
        self.nn.Print()

    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotId, 0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        
        # write to file 
        with open("fitness" + str(self.solutionID) + ".txt", "w") as file:
            file.write(str(xCoordinateOfLinkZero))