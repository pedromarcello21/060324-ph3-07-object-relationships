# Class Inheritance, Methods, and Attributes

## Learning Goals

- Inheritance

- The super method

- Class attributes

- Class methods

## Exercises

### Inheritance

1. Make the `Dog` class inherit from `Mammal` (be sure to import!)

2. Amend the `__init__` method for Dog so it properly utilizes the `super` method.

3. Amend the `__repr__` method so it makes sense with the new attributes from `Mammal`.

4. Change the behavior for the `make_sound` method in `Dog` so it returns something that makes more sense. You will not need to use `super`.

5. Change the `sleep` and `run_around` methods for `Dog` so that they use the `super` keyword. Add additional dog-centric behavior to the methods (for example print or return something new that gives us an idea of what the `Dog` instance is doing).

### Class Methods / Attributes

1. Give the `Fish` a class attribute `all_fish` which starts as an empty list.

2. When a new `Fish` is created, append it to `Fish.all_fish`.

3. Create a new class method `num_fish` which returns the length of `Fish.all_fish`.

4. Create a class method `all_fish_names` which returns a list of all the names for `Fish` instances. *HINT: You can use list comprehension for this!*

5. Create a class method `average_length` which returns the average length in inches for all `Fish` instances. *HINT: The average is the sum of lengths / number of fish. There are several ways of getting the average in Python...*
