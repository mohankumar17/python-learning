from abc import ABC, abstractmethod
class Department(ABC):
    @abstractmethod
    def process(self):
        pass

class Employee(Department):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def getEmpId(self):
        return self.id

    def getEmpName(self):
        return self.name

    def process(self):
        print("Abstract method implementation.")

#dept = Department() #throws error as Departement is abstract class
#print(dept.getId(),dept.getName())
emp = Employee(1, "Paul")
print(emp.getEmpId(), emp.getEmpName())
emp.process()