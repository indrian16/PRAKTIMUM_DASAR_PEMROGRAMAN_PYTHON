# Class Worker
# Merepentasikan Object Perkerja
class Worker:

    # Total Object
    totalWorkerCount = 0

    # Constuctor
    # Inititiallize Object
    # @param name mendefisikan nama perkerja
    # @param salaray mendefisikan gajih gajih
    def __init__(self, name, salary):

        self.name = name
        self.salary = salary
        Worker.totalWorkerCount += 1
    
    # Removed totalWorkerCount 1, after call del function
    def __del__(self):

        Worker.totalWorkerCount -= 1

    # Print Worker Object Count
    def printTotalWorker(self):

        print("Total worker: %d" % Worker.totalWorkerCount)

    # Print Detail Worker, name salary
    def printPekerja(self):
        
        print("Name: ", self.name, ", Salary: $", self.salary)

    printTotalWorker = classmethod(printTotalWorker)

budi = Worker("Budi Setiawan", 1000)
alanSuryajana = Worker("Alan Suryajana", 1000)

budi.printPekerja()
alanSuryajana.printPekerja()
Worker.printTotalWorker()

print("Remove one object")
del budi
Worker.printTotalWorker()