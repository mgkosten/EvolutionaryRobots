import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random
import constants as c
import sys
from simulation import SIMULATION

directOrGUI = sys.argv[1]
solutionID = sys.argv[2]
simulation = SIMULATION(directOrGUI, solutionID)
simulation.Run()
simulation.Get_Fitness()



# # scaled_targetAngles = (targetAngles +1) * (numpy.pi / 4)
# # scaled_targetAngles -= numpy.pi / 4
# # targetAngles = scaled_targetAngles
