class Cat:

    def __init__(self, name, lives_remaining=9):
        self.name = name
        self.lives_remaining = lives_remaining

    def __repr__(self):
        return f"Cat(name={self.name}, lives_remaining={lives_remaining})"
