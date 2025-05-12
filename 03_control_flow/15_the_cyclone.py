#Since 1927, "The Cyclone" roller coaster has delighted visitors at Coney Island (Brooklyn, NY). 🎢

#They're now installing a new entry system (the height requirement is 137 cm and the cost is 10 credits) and need your help writing the program for it!

#Create a new file called the_cyclone.py.

#Ask the user what their height is and how many credits they have, and store the values in a height variable and a credits variable.

#Use a combination of relational and logical operators to create the rules:

#If they are tall enough and have enough credits, print "Enjoy the ride!"
#Else if they have enough credits, but they aren't tall enough, print "You are not tall enough to ride."
#Else if they are tall enough, but they don't have enough credits, print "You don't have enough credits."
#Else, print a message saying they have not met either requirement.

print("No Cyclone, precisa ter 137cm de altura e custa 10 Cbucks para poder aproveitar o brinquedo")
altura = int(input("Informe sua altura em CM: "))
cbucks = int(input("Quantos CBucks tem na carteira? "))

if altura >= 137 and cbucks >= 10:
  print("Aproveite o passeio")
elif altura < 137 and cbucks >= 10:
  print("Você não tem altura minima para entrar no brinquedo")
elif altura >= 137 and cbucks < 10:
  print("Você não tem CBucks para pagar entrada do brinquedo")
else:
  print("Você não atende os requisitos do brinquedo")