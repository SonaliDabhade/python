class Student:
    def insert(self,id,name,marks):
        self.id = id
        self.name = name
        self.marks = marks
    
    def showStudent(self):
        print("ID : ",self.id)
        print("Name : ",self.name)
        print("Marks: ",self.marks)


s1 = Student()

s1.insert(101,"Jhon",80.95)
s1.showStudent()

s2 = Student()

s2.insert(102,"Jane",80.95)
s2.showStudent()
