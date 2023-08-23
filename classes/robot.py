class Robot:
    
    def __init__(self, name, model_num, battery_type="AAA"):
        # self == instance of the robot
        self.name = name
        self.age = 0
        self.model_num = model_num
        self.battery_type = battery_type

    def shoot_lasers(self):
        return "PEW PEW PEW"
    
    def recite_poetry(self):
        return f"Hello my designation is {self.name} and I am here to recite Shakespeare"