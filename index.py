# One to Many #
from classes.models import Car, Garage

# Many to Many #
from classes.models import Doctor, Patient, Appointment

# HARD MODE # (You may need to make more models to make this work!)
from classes.models import Student, Instructor, Course

g1 = Garage("11 Broadway")
g2 = Garage("123 Sesame Street")

c1 = Car(make="BMW", model="M3", license_plate="EWTESLA", garage=g1)
c2 = Car(make="Tesla", model="Roadster", license_plate="EWGAS", garage=g1)
c3 = Car(make="Ferrari", model="F2004", license_plate="RACING", garage=g1)

c4 = Car(make="Porsche", model="GT3RS", license_plate="ELMO ON THE STREET", garage=g2)

d1 = Doctor(name="Dr Doolittle", specialty="veterinarian")
d2 = Doctor(name="Dr Strange", specialty="magic? but also surgery I guess")

p1 = Patient(first_name="Mohammad", last_name="Hossain")
p2 = Patient(first_name="Chett", last_name="Tiller")

a1 = Appointment(doctor=d1, patient=p1)
a2 = Appointment(doctor=d1, patient=p2)
a3 = Appointment(doctor=d2, patient=p1)