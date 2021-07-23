# numbers of cars available
cars = 100

# space available in each car
space_in_a_car = 4

# drivers available
drivers = 30

# passengers available
passengers = 90

# cars that wont be driven
cars_not_driven = cars - drivers

# cars that will be driven
cars_driven = drivers

# capacity to be carpooled
carpool_capacity = cars_driven * space_in_a_car

# amount of passengers in each car
average_passengers_per_car = passengers / cars_driven

# amount of cars available
print("There are", cars, "cars available.")

# amount of drivers available
print("There are only", drivers, "drivers available.")

# number of empty cars
print("There will be", cars_not_driven, "empty cars today.")

# cars that can carpool today
print("We can transport", carpool_capacity, "to carpool today")

# passengers to be carpooled today
print("We have", passengers, "to carpool today")

# number of passengers in each car
print("We need to put about", average_passengers_per_car, "in each car")
