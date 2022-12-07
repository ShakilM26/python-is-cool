# Inheritance
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
    
    
    