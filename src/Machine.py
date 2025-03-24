

class Machine():
    def __init__(self , machine_name, oc ,cpu ,memory ):
        self.machine_name = machine_name
        self.oc = oc
        self.cpu = cpu
        self.memory = memory


    def to_dict(self):
        # Returns the dictionary representation of the Machine object 
        return {
            "Machine_name": self.machine_name,
            "OC": self.oc,
            "CPU": self.cpu , 
            "Memory": self.memory , 
        }
    




