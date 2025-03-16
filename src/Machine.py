

class Machine():
    def __init__(self , name, oc ,cpu ,memory ):
        self.machine_name = name
        self.oc = oc
        self.cpu = cpu
        self.memory = memory
        self.services = {}


    def to_dict(self):
        # Returns the dictionary representation of the Machine object 
        return {
            "name": self.machine_name,
            "OC": self.oc,
            "CPU": self.cpu , 
            "Memory": self.memory , 
            "Services": self.services
        }
    


    # def print_machine(self):
    #     print(f"Name: {self.machine_name} , OC: {self.oc} , CPU: {self.cpu} , RAM: {self.memory}")



