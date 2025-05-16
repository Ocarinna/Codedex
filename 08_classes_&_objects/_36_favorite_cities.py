#Ever wonder how many people live in New York City? What about London?

#Create a favorite_cities.py program.

#Let's make a City class that uses the __init__() method to define the following attributes:

#name (string)
#country (string)
#population (integer rounded to the nearest thousand people)
#landmarks (list of strings)
#Next, create an object for your hometown and assign the attributes above.

#Lastly, create another object of the city that you've always wanted to visit!

#Bonus: Add 2-3 more attributes, like nickname, founding year, mayor, etc.

class city:
    #name=''
    #country=''
    #population=0.0
    #landmarks=''
    def __init__(self,name,contry,population,landmarks,team,park):
        self.name=name
        self.country=contry
        self.population=population
        self.landmarks=landmarks
        self.team=team
        self.park=park


sao_paulo = city('São Paulo', 'Brasil',11450000,'Sé','Corinthians','Parque Ibirapuera')

print(vars(sao_paulo))
