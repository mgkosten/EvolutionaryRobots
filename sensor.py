import numpy 
import constants as c
class SENSOR:

    def __init__(self, linkName):
        self.linkName = linkName
        self.value = numpy.zeros(c.loop_iterations)