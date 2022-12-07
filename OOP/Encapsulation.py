## Encapsulation
# Encapsulation is like invisible box, we don't know
# what's in the backside 

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

class relation:
    def __init__(self, info, education):
        self.info = info 
        self.education = education
    def __str__(self):
        return "%s and fun fact is they both studying in %s but different university"% (self.info, self.education)

infos = relation(m, "B.Sc")
print(infos)



















