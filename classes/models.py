# CAR - GARAGE RELATIONSHIP ### ONE TO MANY RELATIONSHIP

# GARAGE ### HAS MANY CARS
class Garage:

    all_garages = []
    
    def __init__(self, address:str):
        self.address = address
        Garage.all_garages.append(self)

    def __repr__(self):
        return f"Garage(address={self.address})"
    

# CAR ### BELONGS TO A GARAGE
class Car:

    # holds all the cars we've made
    all_cars = []

    def __init__(self, make:str, model:str, license_plate:str):
        self.make = make
        self.model = model
        self.license_plate = license_plate
        Car.all_cars.append(self)

    def __repr__(self):
        return f"Car(make={self.make}, model={self.model}, license_plate={self.license_plate})"




##############################
##############################
##############################
    



# DOCTOR - PATIENT RELATIONSHIP ###

# DOCTOR ###
class Doctor:

    all_doctors = []

    def __init__(self, name:str, specialty:str):
        self.name = name
        self.specialty = specialty
        Doctor.all_doctors.append(self)

    def __repr__(self):
        return f"Doctor(name={self.name}, specialty={self.specialty})"
    

# PATIENT ###
class Patient:

    all_patients = []

    def __init__(self, first_name:str, last_name:str):
        self.first_name = first_name
        self.last_name = last_name
        Patient.all_patients.append(self)

    def __repr__(self):
        return f"Patient(first_name={self.first_name}, last_name={self.last_name})"


# APPT ###
class Appointment:

    all_appts = []

    def __init__(self):
        Appointment.all_appts.append(self)

    def __repr__(self):
        return f"Appointment(patient={self.patient.first_name}, doctor={self.doctor.name})"
    
    


##############################
##############################
##############################




# STUDENT - ENROLLMENT - COURSE RELATIONSHIP ###

# STUDENT ###
class Student:

    all_students = []

    def __init__(self, name):
        self.name = name
        Student.all_students.append(self)

    def __repr__(self):
        return f"Student(name={self.name})"
    
# COURSE ###
class Course:

    all_courses = []

    def __init__(self, subject):
        self.subject = subject
        Course.all_courses.append(self)

    def __repr__(self):
        return f"Course(subject={self.subject})"
    
# ENROLLMENT ###
class Enrollment:

    all_enrollments = []

    def __init__(self, start_date:str):
        self.start_date = start_date
        Enrollment.all_enrollments.append(self)

    def __repr__(self):
        return f"Enrollment(start_date={self.start_date})"