class Dog:

    def __init__(self, name, is_good=True):
        self.name = name
        self.is_good = is_good

    def __repr__(self):
        return f"Dog(name={self.name}, is_good={self.is_good})"
