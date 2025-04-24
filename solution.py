import os
import numpy
import pyrosim.pyrosim as pyrosim
import random
import constants as c

class SOLUTION:
    def __init__(self):
        self.weights = numpy.random.rand(c.numSensorNeurons, c.numMotorNeurons) *2 - 1
        # print(self.weights)
        self.fitness = None
        self.objectives = None

    def Evaluate(self, directOrGUI, generation=None):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        os.system(f"py simulate.py {directOrGUI}")

        # Read from fitness.txt
        with open("fitness.txt", "r") as file:
            contents = file.read()
            values = contents.strip().split(",")
            if len(values) == 2:
                try:
                    distance_to_target = float(values[0])
                    stability = float(values[1])
                    self.objectives = [-distance_to_target, stability]
                except:
                    self.objectives = [0.0, 0.0]  # fallback
            else:
                self.objectives = [0.0, 0.0]

        # # fitnessTrackign.txt
        # if generation is not None:
        #     with open("fitnessTracking.txt", "a") as track_file:
        #         track_file.write(f"{generation}, {distance_to_target + stability}\n")
        # f = open("fitness.txt", "r")
        # fitness_data = f.readline().strip().split(',')
        # self.objectives = [float(x) for x in fitness_data]
        # self.fitness = tuple(self.objectives)
        # # self.fitness = float(f.read().strip())
        # f.close()

    def Mutate(self):
        randRow = random.randint(0, c.numSensorNeurons - 1)
        randCol = random.randint(0, c.numMotorNeurons - 1)
        self.weights[randRow][randCol] = random.random() * 2 - 1

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="SoccerBall", pos=[-0.5, 0, 0.5], size=[0.5, 0.5, 0.5])
        pyrosim.Send_Cube(name="Target", pos=[-6, 0, 2], size = [2, 2, 2])
        pyrosim.End()

    def Generate_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0,0,3.7] , size=[1,1,1.5], mass = 0.5)
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0,-0.5,2.95], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0,0,-0.5] , size=[0.3,0.3,1], mass=2.5)
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0,0.5,2.95], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0,0,-0.5] , size=[0.3,0.3,1], mass=2.5)
        pyrosim.Send_Joint( name = "Torso_RightArm" , parent= "Torso" , child = "RightArm" , type = "revolute", position = [0,0.5,4.2], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="RightArm", pos=[0,0.25,0] , size=[0.2,0.5,0.2], mass=0.005)
        pyrosim.Send_Joint( name = "RightArm_RightLowerArm" , parent= "RightArm" , child = "RightLowerArm" , type = "revolute", position = [0,0.4,-0.1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RightLowerArm", pos=[0,0,-0.25] , size=[0.2,0.2,0.5], mass=0.005)
        pyrosim.Send_Joint( name = "Torso_LeftArm" , parent= "Torso" , child = "LeftArm" , type = "revolute", position = [0,-0.5,4.2], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="LeftArm", pos=[0,-0.25,0] , size=[0.2,0.5,0.2], mass=0.005)
        pyrosim.Send_Joint( name = "LeftArm_LeftLowerArm" , parent= "LeftArm" , child = "LeftLowerArm" , type = "revolute", position = [0,-0.4,-0.1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LeftLowerArm", pos=[0,0,-0.25] , size=[0.2,0.2,0.5], mass=0.005)
        pyrosim.Send_Joint( name = "FrontLeg_FrontLowerLeg" , parent= "FrontLeg" , child = "FrontLowerLeg" , type = "revolute", position = [0,0,-1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0,0,-0.5] , size=[0.3,0.3,1], mass=4)
        pyrosim.Send_Joint( name = "BackLeg_BackLowerLeg" , parent= "BackLeg" , child = "BackLowerLeg" , type = "revolute", position = [0,0,-1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="BackLowerLeg", pos=[0,0,-0.5] , size=[0.3,0.3,1], mass=4)
        pyrosim.Send_Joint( name = "FrontLowerLeg_FrontFoot" , parent= "FrontLowerLeg" , child = "FrontFoot" , type = "revolute", position = [0,0,-1], jointAxis = "0 0 1")
        pyrosim.Send_Cube(name="FrontFoot", pos=[0,0,-0.1] , size=[1,0.3,0.2], mass=7)
        pyrosim.Send_Joint( name = "BackLowerLeg_BackFoot" , parent= "BackLowerLeg" , child = "BackFoot" , type = "revolute", position = [0,0,-1], jointAxis = "0 0 1")
        pyrosim.Send_Cube(name="BackFoot", pos=[0,0,-0.1] , size=[1,0.3,0.2], mass=7)
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
        pyrosim.Send_Sensor_Neuron(name = 7 , linkName = "RightArm")
        pyrosim.Send_Sensor_Neuron(name = 8 , linkName = "LeftArm")
        pyrosim.Send_Sensor_Neuron(name = 9 , linkName = "RightLowerArm")
        pyrosim.Send_Sensor_Neuron(name = 10 , linkName = "LeftLowerArm")
        sensor_neurons = list(range(c.numSensorNeurons))
        pyrosim.Send_Motor_Neuron( name = 0 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 1 , jointName = "Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 2 , jointName = "FrontLeg_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "BackLeg_BackLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "FrontLowerLeg_FrontFoot")
        pyrosim.Send_Motor_Neuron( name = 5 , jointName = "BackLowerLeg_BackFoot")
        pyrosim.Send_Motor_Neuron( name = 6 , jointName = "Torso_RightArm")
        pyrosim.Send_Motor_Neuron( name = 7 , jointName = "Torso_LeftArm")
        pyrosim.Send_Motor_Neuron( name = 8 , jointName = "RightArm_RightLowerArm")
        pyrosim.Send_Motor_Neuron( name = 9 , jointName = "LeftArm_LeftLowerArm")
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
        