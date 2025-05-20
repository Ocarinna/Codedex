#A gambling machine was invented in Brooklyn around 1891. Players would insert a nickel and pull a lever. If it's a good poker hand, you win a free beer. Soon, many bars in the city had it. This was a precursor to the modern slot machine.

#Create a slot_machine.py program using random.

#The items are symbols of common fruits and sevens (7️⃣). In each round, the slot machine displays three random items. If there are three sevens, you win!

#Final Program Output

#Create a symbols list and include the following items: '🍒',' 🍇', '🍉', '7️⃣'.

#Next, create a results variable that uses the .choices() method from the random module and get three random symbols. Make sure to import the required module at the top of the file!

#Then, print each value from results, separated by | pipe characters:

#🍉 | 🍒 | 🍇

#Lastly, use an if/else statement:

#If all of the list items in results are equal to '7️⃣', print "Jackpot! 💰".
#Else, print "Thanks for playing!".
#Bonus:

#Rewrite this program with a play() function.
#Add a while loop for the player to keep playing, round after round.
#Ask the player for a 'Y' or 'N' input to keep playing with input().

import random

def play():
    symbols=['🍒',' 🍇', '🍉','7️⃣']

    results=random.choices(symbols,k=3)

    if all(symbols=='7️⃣' for symbols in results):
        print(results, "\nJackpot 💰")
    else:
        print(results, "\nObrigado por jogar")

while True:
    print("Quer jogar?")
    choice=input("Digite S para jogar, N para sair: \n").upper()

    if choice=="S":
        play()
    elif choice=="N":
        print("\n Obrigado por jogar")
        print("Volte sempre!")
        break
    else:
        print("Comando não aceito, S ou N")