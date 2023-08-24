class Fish:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Fish(name={name})"

    def make_bubbles(self):
        return "bloop bloop"
