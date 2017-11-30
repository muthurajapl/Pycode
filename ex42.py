## Animal is- a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## ??
class Dog(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

## ??
class Cat(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

## ??
class Person(object):

    def __init__(self, name, pet = None):
        ## ??
        self.name = name
        ## Person has- a pet of some kind
        self.pet = None

## ??
class Employee(Person):

    def __init__(self, name, salary, pet = None):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name, pet = None)
        ## ??
        self.salary = salary

## ??
class Fish(object):
    pass

## ??
class Salmon(Fish):
    pass

## ??
class Halibut(Fish):
    pass


## rover is- a Dog
rover = Dog("Rover")

## ??
satan = Cat("Satan")

## ??
mary = Person("Mary",satan)
print (mary.name, mary.pet)
## ??
mary.pet = satan
print (mary.name, mary.pet)

## ??
frank = Employee("Frank", 120000, rover)
print (frank.name, frank.salary, frank.pet)

## ??
#frank.pet = rover

## ??
flipper = Fish()

## ??
crouse = Salmon()

## ??
harry = Halibut()