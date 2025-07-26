class A:
    def Employeedetails(self,Name,id,salary):
        self.Name = Name
        self.id = id 
    def show(self):
        print("Name : ",self.name)
        print("id :", self.id)
        print("salary :",self.salary)
a1 = A()
a1.Employeedetails("Revan", 20,25000)
a1.show()

a2 = A()
a2.Employeedetails("SIRI",17,30000)
a2.show()



