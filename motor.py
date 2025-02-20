import constants as c
import pyrosim.pyrosim as pyrosim
import pybullet as p
import numpy
class MOTOR:

    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()
    
    def Prepare_To_Act(self):
        self.amplitude = c.amp_BackLeg
        self.frequency = c.freq_BackLeg
        self.offset = c.offset_BackLeg

        self.motorValues = {}

        # angles = numpy.linspace(0, 2 * numpy.pi, c.loop_iterations)
        # motorValues = self.amplitude * numpy.sin(self.frequency * angles + self.offset)

    def Set_Value(self, robot, t):
        angles = numpy.linspace(0, 2 * numpy.pi, c.loop_iterations)
        motorValue = self.amplitude * numpy.sin(self.frequency * angles[t] + self.offset)
        self.motorValues[t] = motorValue
        pyrosim.Set_Motor_For_Joint(
                bodyIndex = robot.robotId, 
                jointName = self.jointName, 
                controlMode = p.POSITION_CONTROL, 
                targetPosition = self.motorValues[t], 
                maxForce = 15)