from solution import SOLUTION
import constants as c
import copy

def dominates(solution1, solution2):
    """
    Checks if solution1 dominates solution2.
    """
    better_in_at_least_one = False
    worse_in_any = False
    for i in range(len(solution1.objectives)):
        if solution1.objectives[i] > solution2.objectives[i]:
            better_in_at_least_one = True
        elif solution1.objectives[i] < solution2.objectives[i]:
            worse_in_any = True
            break  # cannot dominate if worse
    return better_in_at_least_one and not worse_in_any

class HILL_CLIMBER:
    def __init__(self):
        self.parent = SOLUTION()

    def Evolve(self):
        self.parent.Evaluate("GUI", generation=0)
        self.parent.Evaluate("DIRECT")
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation(currentGeneration)
    
    def Evolve_For_One_Generation(self, generation):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT", generation=generation)
        self.Print()
        self.Select(generation)

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()

    def Select(self, generation):
        if self.parent.objectives is None or self.child.objectives is None:
            # Handle the case where evaluation might have failed
            if self.child.objectives is not None:
                self.parent = self.child
            return

        if dominates(self.child, self.parent):
            print("Child dominates parent. Keeping Child.")
            self.parent = self.child
        elif dominates(self.parent, self.child):
            print("Parent dominates child. Keeping parent.")
        else:
            print("Neither dominates the other. Keeping parent.")

        # write fitness of parent after selection
        total_fitness = self.parent.objectives[0] + self.parent.objectives[1]
        if generation is not None:
            with open("fitnessTracking.txt", "a") as track_file:
                track_file.write(f"{generation}, {total_fitness}\n")
    
    def Show_Best(self):
        self.parent.Evaluate("GUI")

    def Print(self):
        print(self.parent.objectives, self.child.objectives)