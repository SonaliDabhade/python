class calculation:
    def Summation(self,a,b):
        return a+b;
class calculation2:
    def Multiplication(self,a,b):
        return a*b;
class Derived(calculation,calculation2):
    def Divide(self,a,b):
        return a/b;
d = Derived()  
print(d.Summation(10,30))  
print(d.Multiplication(10,40))  
print(d.Divide(10,30))   