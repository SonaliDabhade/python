class Person:
    def insert(self,name,age):
        self.name=name
        self.age=age
    
    def show(self):
        print("Name : ",self.name)
        print("Age : ",self.age)



class Emp(Person):
    def insert(self,name,age,salary,id):
        super().insert(name,age)
        self.salary = salary
        self.id = id
    def show(self):
          print("ID : ",self.id) 
          print("Name : ",self.name)
          print("Age : ",self.age)
          print("Salary : ",self.salary)


e1 = Emp()
e1.insert("jhon",22,30000,10001)
e1.show()