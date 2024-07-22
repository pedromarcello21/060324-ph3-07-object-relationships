# One to Many #
from classes.models import Car, Garage

# Many to Many #
from classes.models import Doctor, Patient, Appointment

# HARD MODE # (You may need to make more models to make this work!)
from classes.models import Student, Enrollment, Course

# SEED DATA GOES BELOW

my_garage = Garage(address="11 Broadway")

tesla = Car(make="Tesla", model="Cybertruck", license_plate="ILUVELON", garage=my_garage)

porsche = Car(make="Porsche", model="Spyder", license_plate="VROOMVROOM", garage=my_garage)


d1 = Doctor(name="Strange", specialty="neurosurgery / magic")
d2 = Doctor(name="Phil", specialty="drama")

p1 = Patient(first_name="Isaiah", last_name="Kantor")
p2 = Patient(first_name="Josh", last_name="Cruz")