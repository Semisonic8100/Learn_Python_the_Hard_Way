# Animal is-a object (yes, sort of confusing).  Look at the extra credit.
class Animal(object):
    pass

## Dog is-a Animal.
class Dog(Animal):
    
    def __init__(self, name):
        ## Dog has-a name.
        self.name = name

## Cat is-a Animal
class Cat(Animal):
    
    def __init__(self, name):
        ## Cat has-a- name
        self.name = name
        
## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a name
        self.name = name
        
        ## Person has-a- pet of some kind.
        self.pet = None
        
## Employee is-a person.
class Employee(Person):
    
    def __init__(self, name, salary):
        ## ?? hrmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## Employee has-a salary of some kind.
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass
    
## Halibut is-a Fish
class Halibut(Fish):
    pass

## Rover is-a Dog
rover = Dog("Rover")

## Satan is a Cat
satan = Cat("Satan")

## Mary is a Person
mary = Person("Mary")

## From Mary get pet attribute and set it equal to satan.
mary.pet = satan

## Set frank to an instance of class Employee with parameters "Frank" and 120000.
## So frank is-a Employee
frank = Employee("Frank", 120000)

## Frank has-a pet named rover.
frank.pet = rover

## Flipper is-a Fish.
flipper = Fish()

## crous is-a salmon
crous = Salmon()

## harry is-a halibut
harry = Halibut()
