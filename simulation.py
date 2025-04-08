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
    
        # Store the initial Y position of the soccer ball
        self.initialBallYPosition = p.getBasePositionAndOrientation(self.soccerBallId)[0][1] if self.soccerBallId != -1 else 0.0

        # List to store the Z positions of the torso over time
        self.torso_z_positions = []

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
            # Record torso Z position
            torso_id = self.get_body_id_by_name("Torso")
            if torso_id != -1:
                torso_position = p.getBasePositionAndOrientation(torso_id)[0]
                self.torso_z_positions.append(torso_position[2])

        for sensor_name, sensor_instance in self.robot.sensors.items():
            sensor_instance.Save_Values(sensor_name)

    def Get_Fitness(self):
        ballTravelDistance = 0.0
        robotStability = 0.0

        # self.robot.Get_Fitness()
        if self.soccerBallId != -1:
            ballPositionAndOrientation = p.getBasePositionAndOrientation(self.soccerBallId)
            ballYPosition = ballPositionAndOrientation[0][1]

            # Assuming the soccer ball starts at x=1
            ballTravelDistance = ballYPosition - self.initialBallYPosition

            # Robot Stability
            if self.torso_z_positions:
                # Calculate average torso height as a measure of stability
                robotStability = sum(self.torso_z_positions) / len(self.torso_z_positions)
            
            with open("fitness.txt", "w") as file:
                # file.write(str(fitness))
                file.write(f"{ballTravelDistance},{robotStability}")

    def __del__(self):

        p.disconnect()