## Method Overloading
# When two or more methods with the same name but 
# different arguments present in a function then we 
# can call it method overloading.

class overloading:
    def overload(self):
        print('No argument')
    def overload(self, b):
        print('one argument b=', b)
    def overload(self, b,c):
        print('two arguments {} and {}'.format(b,c))
        
obj = overloading()
obj.overload(200,300) 
       


## Method Overriding        
# In different classes, methods are in the same name
# and same argument then we can call it method overriding.

class football:
    def fun(self):
        print('Football is my favorite game')
class player(football):
    def fun(self):
        print('Cristiano Ronaldo was my favorite player.')

obj = player()
obj.fun()
