class Fish:

    def __init__(self, name, length_in_inches):
        self.name = name
        self.length_in_inches = length_in_inches

    def __repr__(self):
        return f"Fish(name={name})"

    def make_bubbles(self):
        return "bloop bloop"
