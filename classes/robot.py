class Robot:

    # this method gets called EVERY TIME we make a new instance
    def __init__(self, name, buttons, year_built):
        self.name = name
        self._buttons = buttons
        self.year_built = year_built

    # this is our getter
    def get_buttons(self):
        return f"{self._buttons} beep boop"

    # this is our setter which keeps buttons from being anything other than a positive integer
    def set_buttons(self, number_of_new_buttons):
        if isinstance(number_of_new_buttons, int) and number_of_new_buttons >= 0:
            self._buttons = number_of_new_buttons
        else:
            print("NOPE")

    # this property overrides robot1.buttons and robot1.buttons = ?
    # it instead runs get_buttons and set_buttons
    buttons = property(get_buttons, set_buttons)

    # when we get an instance like robot1 this will get displayed for our users
    def __repr__(self):
        # the triple " is a heredoc --> it allows us to make a multiline string
        return f"""Robot
        name is {self.name}
        buttons is {self.buttons}
        year_built is {self.year_built}"""
