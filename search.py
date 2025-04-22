import os
from hillclimber import HILL_CLIMBER

hc = HILL_CLIMBER()
if os.path.exists("fitnessTracking.txt"):
    os.remove("fitnessTracking.txt")

hc.Evolve()
hc.Show_Best()