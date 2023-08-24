class Bird:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Bird(name={name})"

    def tweet(self):
        return f"{self.name} is posting all their tweets"
