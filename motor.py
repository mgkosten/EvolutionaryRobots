import constants as c
import pyrosim.pyrosim as pyrosim
import pybullet as p
import numpy
class MOTOR:

    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()
    
    def Prepare_To_Act(self):
        self.amplitude = c.amplitude
        # self.frequency = c.frequency
        self.offset = c.offset

        self.motorValues = {}

        if self.jointName == b"Torso_BackLeg":
            self.frequency = c.frequency / 2.0
            print(f"Joint {self.jointName}: Frequency = {self.frequency}")
        else:
            self.frequency = c.frequency
            print(f"Joint {self.jointName}: Frequency = {self.frequency}")

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
        
    def Save_Values(self, sensor_filename):
        filename = f"data/angles{sensor_filename}.npy"
        motor_value_array = numpy.array(list(self.motorValues.values()))
        numpy.save(filename, motor_value_array, allow_pickle=False)