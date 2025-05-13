#The year is 2199... we have become an interplanetary species and can travel to other planets in the solar system! 🚀

#Create a weight conversion program that:

#Asks the user what their Earth weight is (as a float).
#Asks the user for a planet number (as an int).
#Then, use an if/elif/else statement to calculate the user's weight on the destination planet.

#To calculate the user's weight:

#destination weight=Earth weight × relative gravity
#Number	Planet	Relative Gravity
#1	Mercury	0.38
#2	Venus	0.91
#3	Mars	0.38
#4	Jupiter	2.53
#5	Saturn	1.07
#6	Uranus	0.89
#7	Neptune	1.14
#If the user enters a planet number outside of 1 - 7, print a message that says 'Invalid planet number'.

earth_weight = float(input("Qual seu peso na Terra? "))

while True:
    planet = int(input("Escolha um numero dos planetas a seguir: " \
    "\n#1 Mercurio \n#2 Venus \n#3 Marte \n#4 Jupiter \n#5 Saturno \n#6 Urano \n#7 Netuno \n \n"))
    if planet == 1:
        destination_weight = earth_weight*0.38
        print("Seu peso em Mercurio é ", destination_weight)
        break
    elif planet == 2:
        destination_weight = earth_weight*0.91
        print("Seu peso em Venus é ",destination_weight)
        break
    elif planet == 3 :
        destination_weight = earth_weight*0.38
        print("Seu peso em Marte é ",destination_weight)
        break
    elif planet == 4:
        destination_weight = earth_weight*2.53
        print("Seu peso em Jupiter é ",destination_weight)
        break
    elif planet == 5 :
        destination_weight = earth_weight*1.07
        print("Seu peso em Saturno é ",destination_weight)
        break
    elif planet == 6:
        destination_weight = earth_weight*0.89
        print("Seu peso em Urano é ",destination_weight)
        break
    elif planet == 7:
        destination_weight = earth_weight*1.14
        print("Seu peso em Netuno é ",destination_weight)
        break
    else:
        print('Invalid planet number')
