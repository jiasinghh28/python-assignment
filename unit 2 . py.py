#animal 
class Animal:
    def speak(self):
        print("Animal speaking")

class dog(Animal):
    def bark(self):
        print("dog barking")


d=dog()
d.speak()
d.bark()

#calculation

class calculation1:
    def summation(self,a,b):
        return(a+b);

class calculation2:
    def multiplication(self,a,b):
        return(a*b);

class derivied (calculation1,calculation2):
    def divide(self,a,b):
        return(a/b);

d=derivied()
print(d.summation(10,20))
print(d.multiplication(10,20))
print(d.divide(10,20))


#bank/method overriding 

class bank:
    def getroi(self):
        return 10;
class sbi(bank):
    def getroi(self):
        return 7;
class icici(bank):
    def getroi(self):
        return 8;

b1=bank()
b2=sbi()
b3=icici()

print("bank rate of interest:",b1.getroi());
print("sbi rate of interest:" ,b2.getroi());
print("icici rate of interest:" , b3.getroi());

