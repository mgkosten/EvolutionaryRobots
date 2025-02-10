import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = numpy.zeros(500)
frontLegSensorValues = numpy.zeros(500)
for i in range(500):
	p.stepSimulation()
	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
	pyrosim.Set_Motor_For_Joint( 
		bodyIndex = robotId, 
		jointName = b'Torso_BackLeg', 
		controlMode = p.POSITION_CONTROL, 
		targetPosition = 0.0, 
		maxForce = 500)

	time.sleep(1/60)
	# print(i)
p.disconnect()

numpy.save('data/backLegSensorValues.npy', backLegSensorValues, allow_pickle=False)
numpy.save('data/frontLegSensorValues.npy', frontLegSensorValues, allow_pickle=False)

# print(frontLegSensorValues)
