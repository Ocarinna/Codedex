#The Sorting Hat is a magical talking hat at Hogwarts School of Witchcraft and Wizardry. The hat decides which of the four "Houses" each first-year student goes to:

#🦁 Gryffindor
#🦅 Ravenclaw
#🦡 Hufflepuff
#🐍 Slytherin

#Write a program that asks the user some questions with the int() and input() functions:

#Q1) Do you like Dawn or Dusk?
#    1) Dawn
#    2) Dusk

#If answer is equal to 1, Gryffindor and Ravenclaw both get a +1.
#Else if answer is equal to 2, Hufflepuff and Slytherin both get a +1.
#Else, output the message "Wrong input."
#Q2) When I’m dead, I want people to remember me as:
#    1) The Good
#    2) The Great
#    3) The Wise
#    4) The Bold

#If the answer is 1, Hufflepuff +2.
#Else if answer is 2, Slytherin +2.
#Else if answer is 3, Ravenclaw +2.
#Else if answer is 4, Gryffindor +2.
#Else, output the message "Wrong input."
#Q3) Which kind of instrument most pleases your ear?
#    1) The violin
#    2) The trumpet
#    3) The piano
#    4) The drum

#If the answer is 1, Slytherin +4.
#Else if the answer is 2, Hufflepuff +4.
#Else if the answer is 3, Ravenclaw +4.
#Else if the answer is 4, Gryffindor +4.
#Else, output "Wrong input."
#Lastly, print out the score for each house.

#Bonus: If you want to go further, see if you can figure out how to print out the house with the most points!

gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slythenrin = 0 

while True:
    print("Q1) Você prefere um amanhacer ou anoitecer? \n(1) amanhecer \n(2) anoitecer")
    q1 = int(input("Digite sua resposta 1 ou 2: "))
    if q1 == 1:
        gryffindor +=1
        ravenclaw +=1
        break
    elif q1 == 2:
        hufflepuff +=1
        slythenrin +=1
        break
    else:
        print("Resposta aceitas somente (1) ou (2)")

while True:
    print("Q2) Quando eu morrer, quero que as pessoas se lembre de mim como? \n(1) O Bondoso \n(2) O Grande \n(3) O Sábio \n(4) O Corajoso")
    q2 = int(input("Digite sua resposta 1 a 4: "))
    if q2 == 1:
        hufflepuff +=2
        break
    elif q2 == 2:
        slythenrin +=2
        break
    elif q2 == 3:
        ravenclaw +=2
        break
    elif q2 == 4:
        gryffindor +=2
        break
    else:
        print("Resposta aceitas somente (1), (2), (3) ou (4)")

while True:
    print("Q3) Qual o instrumento agrada seu ouvido? \n(1) Violino \n(2) Trompete \n(3) Piano \n(4) Tambor")
    q3 = int(input("Digite sua resposta 1 a 4: "))
    if q3 == 1:
        slythenrin +=4
        break
    elif q3 == 2:
        hufflepuff +=4
        break
    elif q3 == 3:
        ravenclaw +=4
        break
    elif q3 == 4:
        gryffindor +=4
        break
    else:
        print("Resposta aceitas somente (1), (2), (3) ou (4)")

scores = {
    "Gryffindor": gryffindor,
    "Ravenclaw": ravenclaw,
    "Hufflepuff": hufflepuff,
    "Slytherin": slythenrin
}
max_scores = max(scores.values())
winners = [house for house, score in scores.items() if score == max_scores]

if len(winners) == 1:
    print("\n O Chapéu Seletor escolheu: ", winners[0])

else:
    print("\n Está empatado entre: ", ", ".join(winners))
