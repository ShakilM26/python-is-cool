#************************* Abstraction ***************************

class python:
    def __init__(self, one, two, three):
        # using double underscore before any variable or method 
        # make them private
        self.__one = one 
        self.__two = two
        self.__three = three 
    def __sum(self):
        return self.__one + self.__two + self.__three
    def __double(self):
        return self.__one + self.__two 

p = python(20, 50, 80)

# To access the private data as output we have to write
# obj._classname__variablename

print(p._python__one)
print(p._python__sum())
print(p._python__double())




#************************* Inheritance ***************************

# Under the inheritance the child class inherits some/all of the 
# characteristics from Parent Class

# Inheritance is of two types. 
# i. Multilevel 
# ii. Multiclass

#1. Inheriting single class property into child class

class father:
    def __init__(self, a,b,c):
        self.a = a 
        self.b = b
        self.c = c
    def fun(self):
        print('This is Parent class. But this is taken by child.')
        
class son(father):
    pass

obj = son(10,20,30)
print(obj.a, obj.c)
obj.fun()



## Inheriting limited number of variable from parent class using super() 

class father:
    def __init__(self, a,b,c):
        self.a = a 
        self.b = b
        self.c = c
    def fun(self):
        print('This is Parent class. But this is taken by child.')

class child(father):
    def __init__(self, a, b):
        super().__init__(self, a, b)
        self.a = a
        self.b = b
    def difference(self):
        return self.b - self.a 
    
    
obj = child(100, 400)
print(obj.difference())
    
    
## Inheriting multiple class property into child class

class parents:
    def father(self):
        print('Father is the king of our family.')
class parents1:
    def mother(self):
        print('Mother is the queen of our family.')

class child(parents, parents1):
    pass

obj = child()
obj.father()
obj.mother()
    
    


#************************* Encapsulation ***************************

# Composite Encapsulation pass all the objects as a variable
class Laptop:
    def __init__(self, brand_name, model, price):
        self.brand_name = brand_name
        self.model = model
        self.price = price
    def __str__(self):
        return "\n \tbrand_name: "+str(self.brand_name)+"\n \tmodel: "+str(self.model)+"\n \tprice: "+str(self.price)+"\n"

class Configuration:
    def __init__(self,RAM,Corei,Gen):
        self.RAM = RAM
        self.Corei = Corei
        self.Gen = Gen 
    def __str__(self):
        return " \n \tRAM: "+str(self.RAM)+"\n \tCore-i: "+str(self.Corei)+"\n \tGen: "+str(self.Gen)

class buy_year:
    def __init__(self,buy_year):
        self.buy_year = buy_year
    def __str__(self):
        return " \n \tbuy_year: "+str(self.buy_year)

class description:
    def __init__(self, Laptop, Configuration, buy_year):
        self.Laptop = Laptop
        self.Configuration = Configuration
        self.buy_year = buy_year
    
    def __str__(self):
        return "Laptop_Description \t"+str(self.Laptop)+"\n Configuration \t"+str(self.Configuration)+"\n \n Buying_year \n \n"+str(self.buy_year)

l = Laptop('HP', 'Pavilion', '44,400')
c = Configuration("4GB", 3, 7)
b = buy_year(2017)
d = description(l, c, b)
print(d)



# Dynamic Extension pass some of the object as a variable

class marrige:
    def __init__(self, couple_name, denmohor):
        self.couple_name = couple_name
        self.denmohor = denmohor
    def __str__(self):
        return "%s tying the knot with %s denmohor"% (self.couple_name, self.denmohor)
m = marrige('Shakil-Mou', 10500)
print(m)






#************************* Polymorphism **************************

def result(a,b):
    return a+b

integer = result(1,1)
string = result('Almirr', ' Shakil')
list_extension = result([1,2,3], [4,5,6])
print(integer) 
print(string)
print(list_extension)

