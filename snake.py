from reptile import Reptile

class Sk(Reptile):

    def __init__(self):
        super().__init__()

    def use_tongue_to_smell(self):
        return " if I can touch itI can smell it as well "
smart_sk = Sk()
# print(smart_sk.hunt())
# print(smart_sk.use_tongue_to_smell())
# print(smart_sk.breathe())

# create a new same .md  file to add this code with your documentation