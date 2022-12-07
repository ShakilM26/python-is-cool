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



