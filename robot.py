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
