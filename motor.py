import constants as c
import pyrosim.pyrosim as pyrosim
import numpy
class MOTOR:

    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act
    
    def Prepare_To_Act(self):
        self.amplitude = c.amp_BackLeg
        self.frequency = c.freq_BackLeg
        self.offset = c.offset_BackLeg

        self.motorValues = {}
        # for motor in pyrosim.linkNamesToIndices:
        #     self.sensors[linkName] = SENSOR(linkName)

        # angles = numpy.linspace(0, 2 * numpy.pi, c.loop_iterations)
        # motorValues = self.amplitude * numpy.sin(self.frequency * angles + self.offset)

    def Set_Value(self):
        pyrosim.Set_Motor_For_Joint(
                bodyIndex = robotId, 
                jointName = b'Torso_BackLeg', 
                controlMode = p.POSITION_CONTROL, 
                targetPosition = targetAngles_BackLeg[i], 
                maxForce = 15)