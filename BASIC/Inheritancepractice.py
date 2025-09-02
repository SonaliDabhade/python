class  A:
    def insert(self,messages):
        self.messages=messages
    
    def greet(self):
        print("Hello World")

class B(A):
    def insert(self,messages):
        super().insert(messages)
        self.messages=messages
    def show(self):
        print("Say Hello")

e1 = A()
b2 = B()
b2.greet()
b2.show()     

