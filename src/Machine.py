

class Machine():
    def __init__(self , name, oc ,cpu ,memory ):
        self.machine_name = name
        self.oc = oc
        self.cpu = cpu
        self.memory = memory


    def to_dict(self):
        # Returns the dictionary representation of the Machine object 
        return {
            "name": self.machine_name,
            "OC": self.oc,
            "CPU": self.cpu , 
            "Memory": self.memory , 
        }
    


    # def print_machine(self):
    #     print(f"Name: {self.machine_name} , OC: {self.oc} , CPU: {self.cpu} , RAM: {self.memory}")



