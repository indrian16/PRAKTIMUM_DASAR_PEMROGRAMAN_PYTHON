# Class Worker
# Merepentasikan Object Perkerja
class Worker:

    # Constuctor
    # Inititiallize Object
    # name mendefisikan nama perkerja
    # salaray mendefisikan gajih gajih
    def __init__(self, name, salary):

        self.name = name
        self.salary = salary

    # Print Detail Worker, name salary
    def printPekerja(self):
        
        print("Name: ", self.name, ", Salary: $", self.salary)