# CAR - GARAGE RELATIONSHIP ###

# CAR ###
class Car:
    
    def __init__(self, make, model, license_plate):
        self.make = make
        self.model = model
        self.license_plate = license_plate

    def __repr__(self):
        return f"Car(make={self.make}, model={self.model}, license_plate={self.license_plate})"

# GARAGE ###
class Garage:
    
    def __init__(self, address):
        self.address = address

    def __repr__(self):
        return f"Garage(address={self.address})"
    
##############################



# DOCTOR - PATIENT RELATIONSHIP ###

# DOCTOR ###
class Doctor:

    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty

    def __repr__(self):
        return f"Doctor(name={self.name}, specialty={self.specialty})"

# PATIENT ###
class Patient:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f"Patient(first_name={self.first_name}, last_name={self.last_name})"
    
##############################
    


# STUDENT - INSTRUCTOR - COURSE - ASSIGNMENT - SCHOOL RELATIONSHIP ###

# STUDENT ###
class Student:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Student(name={self.name})"
    
# INSTRUCTOR ###
class Instructor:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Instructor(name={self.name})"
    
# COURSE ###
class Course:

    def __init__(self, subject, start_date):
        self.subject = subject

    def __repr__(self):
        return f"Course(subject={self.subject})"

# ASSIGNMENT ###
class Assignment:

    def __init__(self, title, grade):
        self.title = title
        self.grade = grade

    def __repr__(self):
        return f"Assignment(title={self.title}, grade={self.grade})"

# SCHOOL ###
class School:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"School(name={self.name})"
    
##############################