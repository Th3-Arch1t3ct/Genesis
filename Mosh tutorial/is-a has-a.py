## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a animal
class Dog(Animal):

    def __init__(self, name):
        ##??
        self.name = name

## Cat is-a animal
class Cat(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ##??
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary

## Fish has-a object
class Fish(object):
    pass

## Salmon is-a fish
class Salmon(Fish):
    pass

## Salmon is-a fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a cat
satan = Cat("Satan")

## mary is-a person
mary = Person("Mary")

## mary has-a pet
mary.pet = satan

## frank is-a employee
frank = Employee("Frank", 120000)

## frank has-a pet rover
frank.pet = rover

## flipper is-a fish
flipper = Fish()

## crouse is-a salmon
crouse = Salmon()

## harry has-a fish
harry = Halibut()

print()