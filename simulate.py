import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random
import constants as c
from simulation import SIMULATION

simulation = SIMULATION()
simulation.Run()



# # scaled_targetAngles = (targetAngles +1) * (numpy.pi / 4)
# # scaled_targetAngles -= numpy.pi / 4
# # targetAngles = scaled_targetAngles
