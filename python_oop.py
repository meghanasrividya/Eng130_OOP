from snake import Sk
class Python_oop(Sk):
    def __init__(self):
        super().__init__()
        self.large=True

    def swallow(self):
        return "Python can swallow"

py = Python_oop()

print(py.swallow())# printing same class method
print(py.breathe())# printing greatgrand parent method
print(py.hunt())# printing grand parent method
print(py.use_tongue_to_smell())# using parent class method
