import os
import numpy
import pyrosim.pyrosim as pyrosim
import random
import constants as c

class SOLUTION:
    def __init__(self):
        self.weights = numpy.random.rand(c.numSensorNeurons, c.numMotorNeurons) *2 - 1
        print(self.weights)

    def Evaluate(self, directOrGUI):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        os.system(f"py simulate.py {directOrGUI}")

        f = open("fitness.txt", "r")
        self.fitness = float(f.read().strip())
        f.close()

    def Mutate(self):
        randRow = random.randint(0, c.numSensorNeurons - 1)
        randCol = random.randint(0, c.numMotorNeurons - 1)
        self.weights[randRow][randCol] = random.random() * 2 - 1

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="SoccerBall", pos=[-1, 0, 0.5], size=[0.5, 0.5, 0.5])
        pyrosim.End()

    def Generate_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0,0,3.7] , size=[1,1,1.5])
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0,-0.5,2.95], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0,0,-0.5] , size=[0.3,0.3,1], mass=2)
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0,0.5,2.95], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0,0,-0.5] , size=[0.3,0.3,1], mass=2)
        # pyrosim.Send_Joint( name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", position = [-0.5,0,1], jointAxis = "0 1 0")
        # pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5,0,0] , size=[1,0.2,0.2])
        # pyrosim.Send_Joint( name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = "revolute", position = [0.5,0,1], jointAxis = "0 1 0")
        # pyrosim.Send_Cube(name="RightLeg", pos=[0.5,0,0] , size=[1,0.2,0.2])
        pyrosim.Send_Joint( name = "FrontLeg_FrontLowerLeg" , parent= "FrontLeg" , child = "FrontLowerLeg" , type = "revolute", position = [0,0,-1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0,0,-0.5] , size=[0.3,0.3,1], mass=3)
        pyrosim.Send_Joint( name = "BackLeg_BackLowerLeg" , parent= "BackLeg" , child = "BackLowerLeg" , type = "revolute", position = [0,0,-1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="BackLowerLeg", pos=[0,0,-0.5] , size=[0.3,0.3,1], mass=3)
        pyrosim.Send_Joint( name = "FrontLowerLeg_FrontFoot" , parent= "FrontLowerLeg" , child = "FrontFoot" , type = "revolute", position = [0,0,-1], jointAxis = "0 0 1")
        pyrosim.Send_Cube(name="FrontFoot", pos=[0,0,-0.1] , size=[1,0.3,0.2], mass=5)
        pyrosim.Send_Joint( name = "BackLowerLeg_BackFoot" , parent= "BackLowerLeg" , child = "BackFoot" , type = "revolute", position = [0,0,-1], jointAxis = "0 0 1")
        pyrosim.Send_Cube(name="BackFoot", pos=[0,0,-0.1] , size=[1,0.3,0.2], mass=4)
        pyrosim.End()

    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork("brain.nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "BackLegLower")
        pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "FrontLegLower")
        pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "BackFoot")
        pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "FrontFoot")
        # pyrosim.Send_Sensor_Neuron(name = 7 , linkName = "LeftLowerLeg")
        # pyrosim.Send_Sensor_Neuron(name = 8 , linkName = "RightLowerLeg")
        sensor_neurons = list(range(c.numSensorNeurons))
        pyrosim.Send_Motor_Neuron( name = 0 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 1 , jointName = "Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 2 , jointName = "FrontLeg_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "BackLeg_BackLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "FrontLowerLeg_FrontFoot")
        pyrosim.Send_Motor_Neuron( name = 5 , jointName = "BackLowerLeg_BackFoot")
        # pyrosim.Send_Motor_Neuron( name = 9 , jointName = "LeftLeg_LeftLowerLeg")
        # pyrosim.Send_Motor_Neuron( name = 10 , jointName = "RightLeg_RightLowerLeg")
        motor_neurons = list(range(c.numMotorNeurons))
        # pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3 , weight = -0.5 )
        # pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 3 , weight = 1.0 )
        # pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 4 , weight = 1.5 )
        # pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 4 , weight = 0.5)
        for currentRow in sensor_neurons:
            for currentColumn in motor_neurons:
                weight = self.weights[currentRow][currentColumn]
                pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn, weight = weight)
        pyrosim.End()
        