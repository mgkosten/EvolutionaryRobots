import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import constants as c
from world import WORLD
from robot import ROBOT
from motor import MOTOR

class SIMULATION:

    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)

        self.world = WORLD()
        self.robot = ROBOT()

        pyrosim.Prepare_To_Simulate(self.robot.robotId)
        self.robot.Prepare_To_Sense()
    
    def Run(self):
        for i in range(c.loop_iterations):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Act
            # backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
            # frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
        
            # pyrosim.Set_Motor_For_Joint(
            #     bodyIndex = robotId, 
            #     jointName = b'Torso_BackLeg', 
            #     controlMode = p.POSITION_CONTROL, 
            #     targetPosition = targetAngles_BackLeg[i], 
            #     maxForce = 15)
        
            # pyrosim.Set_Motor_For_Joint(
            #     bodyIndex = robotId, 
            #     jointName = b'Torso_FrontLeg', 
            #     controlMode = p.POSITION_CONTROL, 
            #     targetPosition = targetAngles_FrontLeg[i], 
            #     maxForce = 15)

            time.sleep(1/240)  # 4 spaces indentation
            print(i)  # 4 spaces indentation

    def __del__(self):

        p.disconnect()