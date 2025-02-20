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
        self.robot.Prepare_To_Act()
    
    def Run(self):
        for i in range(c.loop_iterations):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Act(i)

            time.sleep(1/40) 
            # print(i)
        for sensor_name, sensor_instance in self.robot.sensors.items():
            sensor_instance.Save_Values(sensor_name)

        for joint_name, motor_instance in self.robot.joints.items():
            motor_instance.Save_Values(joint_name)

    def __del__(self):

        p.disconnect()