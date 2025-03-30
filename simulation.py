import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import constants as c
from world import WORLD
from robot import ROBOT
from motor import MOTOR

class SIMULATION:

    def __init__(self, directOrGUI):
        self.directOrGUI = directOrGUI
        if directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)

        self.world = WORLD()
        self.robot = ROBOT()

        pyrosim.Prepare_To_Simulate(self.robot.robotId)
        self.robot.Prepare_To_Sense()
        self.robot.Prepare_To_Act()

        # Find the soccer ball ID
        self.soccerBallId = self.get_body_id_by_name("SoccerBall")
        # if self.soccerBallId == -1:
        #     print("Error: SoccerBall not found in the simulation.")

        # Store the initial Y position of the soccer ball
        if self.soccerBallId != -1:
            initialBallPosition = p.getBasePositionAndOrientation(self.soccerBallId)[0]
            self.initialBallYPosition = initialBallPosition[1]
        else:
            self.initialBallYPosition = 0.0

    def get_body_id_by_name(self, body_name):
        """
        Retrieves the body ID of an object in PyBullet given its name.
        """
        for bodyId in range(p.getNumBodies()):
            info = p.getBodyInfo(bodyId)
            name = info[0].decode('utf-8')
            if name == body_name:
                return bodyId
        return -1
    
    def Run(self):
        for i in range(c.loop_iterations):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
            if self.directOrGUI == "GUI":
                time.sleep(1/120) 
            # print(i)
        for sensor_name, sensor_instance in self.robot.sensors.items():
            sensor_instance.Save_Values(sensor_name)

    def Get_Fitness(self):
        # self.robot.Get_Fitness()
        if self.soccerBallId != -1:
            ballPositionAndOrientation = p.getBasePositionAndOrientation(self.soccerBallId)
            ballYPosition = ballPositionAndOrientation[0][1]

            # Assuming the soccer ball starts at x=1
            ballTravelDistance = ballYPosition - self.initialBallYPosition

            # Write the ball's travel distance to the fitness file
            with open("fitness.txt", "w") as file:
                file.write(str(ballTravelDistance))
        # else:
        #     # Handle the case where the soccer ball is not found
        #     print("Error: SoccerBall not found in the simulation. Fitness set to 0.")
        #     with open("fitness.txt", "w") as file:
        #         file.write(str(0.0))
        #     return 0.0

    def __del__(self):

        p.disconnect()