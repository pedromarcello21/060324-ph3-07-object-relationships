class Human:
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self._age = 0

    def __repr__(self):
        return f"Human(first_name={self.first_name}, last_name={self.last_name}, age={self._age})"

    # --- INSTANCE METHODS --- #

    def say_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def happy_birthday(self):
        self._age += 1
        return self._age

    # --- PROPERTIES --- #

    # the @ is a decorator
    @property
    def age(self):
        return f"{self.say_full_name()} is {self._age}"
    
    @age.setter
    def age(self, new_age):
        if type(new_age) == int:
            self._age = new_age
        else:
            print("UNACCEPTABLE")

    # --- HERE IS AN ALTERNATE WAY OF SETTING PROPERTIES --- #

    # def get_age(self):
    #     return self._age
    
    # def set_age(self, new_age):
    #     if type(new_age) == int:
    #         self._age = new_age
    #     else:
    #         print("UNACCEPTABLE")

    # age = property(get_age, set_age)