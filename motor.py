import constants as c
import pyrosim.pyrosim as pyrosim
import pybullet as p
import numpy
class MOTOR:

    def __init__(self, jointName):
        self.jointName = jointName

    def Set_Value(self, robot, desiredAngle):
        angles = numpy.linspace(0, 2 * numpy.pi, c.loop_iterations)
        #motorValue = self.amplitude * numpy.sin(self.frequency * desiredAngle + self.offset)
        # desiredAngle = motorValue
        pyrosim.Set_Motor_For_Joint(
                bodyIndex = robot.robotId, 
                jointName = self.jointName, 
                controlMode = p.POSITION_CONTROL, 
                targetPosition = desiredAngle, 
                maxForce = c.motorForce)