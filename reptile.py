# create a class called Reptile
# how do we make the Animal class a parent class- how could we inherit from the Animal
from animal import Animal # importing everything from Animal class
class Reptile(Animal): # Inherit from Animal class
    def __init__(self):

        self.cold_blooded=True
        self.tetrapods=None
        self.heart_chambers =[3,4]

    def hunt(self):
        return "keep working hard to find food !"
    def use_venom(self):
        return "If I have it I will use it"
smart_reptile = Reptile()
# print(smart_reptile.breathe())
# print(smart_reptile.hunt())