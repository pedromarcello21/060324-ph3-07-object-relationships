from classes.mammal import Mammal

class Dog(Mammal):

    def __init__(self, name, is_good=True):
        super().__init__(rested=False, name=name)
        self.is_good = is_good

    def __repr__(self):
        return f"Dog(name={self.name}, is_good={self.is_good}, rested={self.rested})"

    def make_sound(self):
        return "BOWOWOWOWOWOWOWOWOWOWOWOWOWOW (into infinity)"
    
    def sleep(self):
        super().sleep()
        return "ZZzzzZZZzzzZZZZzzzz"

    def run_around(self):
        super().run_around()
        print(f"{self.name} is running around!")