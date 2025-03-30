import pybullet as p
import pyrosim.pyrosim as pyrosim
import constants as c
import numpy as np
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
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.sinVals = np.linspace(0, (2 * np.pi), 1000)
            self.motors[jointName] = MOTOR(jointName)
        # print(self.joints)
    
    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                # print(neuronName)
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName).encode('utf-8')
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                # print(f"Motor {jointName} desired angle: {desiredAngle}")

                self.motors[jointName].Set_Value(self, desiredAngle * c.motorJointRange)
                # motor_to_set = self.motors.get(jointName)
                # motor_to_set.Set_Value(self, desiredAngle)
                # self.motors[jointName].Set_Value(self, 1.0)
    
    def Think(self):
        self.nn.Update()
        self.nn.Print()

    def Get_Fitness(self):
        # basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
        # basePosition = basePositionAndOrientation[0]
        # xPosition = basePosition[0]
        
        # # write to file 
        # with open("fitness.txt", "w") as file:
        #     file.write(str(xPosition))
        # Get the robot's final X position (you might still want this)
        pass