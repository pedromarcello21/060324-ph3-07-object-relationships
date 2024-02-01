# CAR - GARAGE RELATIONSHIP ### ONE TO MANY RELATIONSHIP

# CAR ### BELONGS TO A GARAGE
class Car:

    # holds all the cars we've made
    all_cars = []

    def __init__(self, make, model, license_plate, garage):
        self.make = make
        self.model = model
        self.license_plate = license_plate
        self.garage = garage
        Car.all_cars.append(self)

    def __repr__(self):
        return f"Car(make={self.make}, model={self.model}, license_plate={self.license_plate})"

    @property
    def garage(self):
        return self._garage
    
    @garage.setter
    def garage(self, new_garage):
        # if type(new_garage) is Garage:
        if isinstance(new_garage, Garage):
            self._garage = new_garage
        else:
            raise TypeError("cars belong in garages, garage must of type Garage")



# GARAGE ### HAS MANY CARS
class Garage:
    
    def __init__(self, address):
        self.address = address

    def __repr__(self):
        return f"Garage(address={self.address})"
    
    def cars(self):
        # give me all the cars that belong to this garage
        # self == the garage that called this method
        return [ car for car in Car.all_cars if car.garage == self ]

        # JS #
        # all_cars.filter((car) => {
        #     return car.garage === self
        # })

##############################
    

# DOCTOR - PATIENT RELATIONSHIP ###

# DOCTOR ###
class Doctor:

    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty

    def __repr__(self):
        return f"Doctor(name={self.name}, specialty={self.specialty})"
    
    def appointments(self):
        return [ appt for appt in Appointment.all_appts if appt.doctor == self ]
    
    def patients(self):
        return [ appt.patient for appt in Appointment.all_appts if appt.doctor == self ]

# PATIENT ###
class Patient:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f"Patient(first_name={self.first_name}, last_name={self.last_name})"
    
    def appointments(self):
        return [ appt for appt in Appointment.all_appts if appt.patient == self ]
    
    def doctors(self):
        return [ appt.doctor for appt in Appointment.all_appts if appt.patient is self ]
    

# APPT ###
class Appointment:

    all_appts = []

    def __init__(self, doctor, patient):
        self.doctor = doctor
        self.patient = patient
        Appointment.all_appts.append(self)

    def __repr__(self):
        return f"Appointment(patient={self.patient.first_name}, doctor={self.doctor.name})"
    
    
##############################
    


# STUDENT - ASSIGNMENT - COURSE - INSTRUCTOR ###

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


##############################