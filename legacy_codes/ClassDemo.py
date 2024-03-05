class Department:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def getId(self):
        return self.id
    def getName(self):
        return self.name

class Employee:
    organizationName = "Abies Pvt.Ltd."

    def __init__(self, empId, department):
        self.empId = empId
        self.empName = None
        self.empSalary = None
        self.department = department

    def getEmpName(self):
        return self.empName

    def setEmpName(self, empName):
        self.empName = empName

    def getId(self):
        return self.empId

    def getEmpSalary(self):
        return self.empSalary

    def setEmpSalary(self, empSalary):
        self.empSalary = empSalary

    @classmethod
    def showOrganizationName(cls):
        print(cls.organizationName)

    @staticmethod
    def showMessage():
        print("Static Method")

    def getAddressDetails(self, addr):
        return {"Country": addr.getCountry(),
                "State": addr.getState()}

    def getDepartmentDetails(self):
        return {"Dept ID": self.department.getId(),
                "Dept Name": self.department.getName()}

    class Address:
        def __init__(self, country, state):
            self.country = country
            self.state = state

        def getCountry(self):
            return self.country

        def getState(self):
            return self.state

dept = Department(301, "IT")
theEmployee1 = Employee(101, dept)
addr1 = theEmployee1.Address("India", "AP")

print(theEmployee1.getId())
theEmployee1.setEmpName("Paul Brandon")
print(theEmployee1.getEmpName())
theEmployee1.setEmpSalary(85000)
print(theEmployee1.getEmpSalary())
print(theEmployee1.getAddressDetails(addr1))
print(theEmployee1.getDepartmentDetails())

dept = Department(302, "HR")
theEmployee2 = Employee(102, dept)
addr2 = theEmployee1.Address("India", "TN")

print(theEmployee2.getId())
theEmployee2.setEmpName("Tina Nailor")
print(theEmployee2.getEmpName())
theEmployee2.setEmpSalary(74000)
print(theEmployee2.getEmpSalary())
print(theEmployee2.getAddressDetails(addr2))
print(theEmployee2.getDepartmentDetails())

'''print()
Employee.showOrganizationName()
Employee.showMessage()'''
