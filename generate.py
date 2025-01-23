import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")
x_start = -2.5
y_start = -2.5
z_start = 0.5
for j in range(5):
    for i in range(5):
        x = x_start + i
        y = y_start + j
        z = z_start
        length = 1
        width = 1
        height = 1
        for k in range(10):
            pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
            z += 1
            length = 0.9*length
            width = 0.9*width
            height = 0.9*height
pyrosim.End()