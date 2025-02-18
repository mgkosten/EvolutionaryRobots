import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random
import constants as c
from simulation import SIMULATION

pass
# amplitude_BackLeg = c.amp_BackLeg
# frequency_BackLeg = c.freq_BackLeg
# phaseOffset_BackLeg = c.offset_BackLeg

# amplitude_FrontLeg = c.amp_FrontLeg
# frequency_FrontLeg = c.freq_FrontLeg
# phaseOffset_FrontLeg = c.offset_FrontLeg

# physicsClient = p.connect(p.GUI)
# p.setAdditionalSearchPath(pybullet_data.getDataPath())
# p.setGravity(0,0,-9.8)
# planeId = p.loadURDF("plane.urdf")
# robotId = p.loadURDF("body.urdf")
# p.loadSDF("world.sdf")

# pyrosim.Prepare_To_Simulate(robotId)

# angles = numpy.linspace(0, 2 * numpy.pi, 1000)
# targetAngles_BackLeg = amplitude_BackLeg * numpy.sin(frequency_BackLeg * angles + phaseOffset_BackLeg)
# targetAngles_FrontLeg = amplitude_FrontLeg * numpy.sin(frequency_FrontLeg * angles + phaseOffset_FrontLeg)

# # scaled_targetAngles = (targetAngles +1) * (numpy.pi / 4)
# # scaled_targetAngles -= numpy.pi / 4
# # targetAngles = scaled_targetAngles
# # numpy.save('data/anglesBackLeg.npy', targetAngles_BackLeg, allow_pickle=False)
# # numpy.save('data/anglesFrontLeg.npy', targetAngles_FrontLeg, allow_pickle=False)
# # exit()

# backLegSensorValues = numpy.zeros(1000)
# frontLegSensorValues = numpy.zeros(1000)
# for i in range(1000):
# 	p.stepSimulation()
# 	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
# 	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
# 	pyrosim.Set_Motor_For_Joint( 
# 		bodyIndex = robotId, 
# 		jointName = b'Torso_BackLeg', 
# 		controlMode = p.POSITION_CONTROL, 
# 		targetPosition = targetAngles_BackLeg[i], 
# 		maxForce = 15)
	
# 	pyrosim.Set_Motor_For_Joint( 
# 		bodyIndex = robotId, 
# 		jointName = b'Torso_FrontLeg', 
# 		controlMode = p.POSITION_CONTROL, 
# 		targetPosition = targetAngles_FrontLeg[i], 
# 		maxForce = 15)

# 	time.sleep(1/240)
# 	# print(i)
# p.disconnect()

# numpy.save('data/backLegSensorValues.npy', backLegSensorValues, allow_pickle=False)
# numpy.save('data/frontLegSensorValues.npy', frontLegSensorValues, allow_pickle=False)

# # print(frontLegSensorValues)
