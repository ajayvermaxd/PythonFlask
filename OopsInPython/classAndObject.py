# define a class name Car with the attributes make, model, year
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    #create a method start_engine that prints the msg car has stated
    def start_engine(self):
        print("The engine has started")

#create an object my_car from the Car class with the attributes make, model, year
my_car = Car(make ="Toyota", model = "Camry", year="2022")
print("Brand: ", my_car.make) #output Toyota
print("Model: " , my_car.model)  #output Carmy
print("Year: ", my_car.year)    #output 2022