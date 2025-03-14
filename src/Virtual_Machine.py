

class Virtual_Machine():
    def __init__(self , name, oc ,cpu ,memory ):
        self.machine_name = name
        self.oc = oc
        self.cpu = cpu
        self.memory = memory
    

    def print_machine(self):
        print(f"Name: {self.machine_name} , OC: {self.oc} , CPU: {self.cpu} , RAM: {self.memory}")



