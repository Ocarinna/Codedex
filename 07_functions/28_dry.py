#Create a dry.py program and check out the complete list of built-in functions:

#Find 4 built-in functions that we have used previously in the course.
#Pick 1 built-in function that we have not seen before.
#Use each of these once in the program.

#For the new function, try to read the documentation (😵‍💫) or Google it (👍)!

#Add a comment for each built-in function to explain how they work.

numeros = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]

name = input("Me diga seu nome? \n")
#função lê a lina do terminal e converte em string

print(max(numeros))
#Verifica qual é o maior valor de uma lista e retorna.

print(min(numeros))
#Verifica qual é o menor numero de uma lista e retorna

idade = int(input("Qual sua idade? \n"))
#Converte para integer um a informações de numero ou string(texto)

for indice, item in enumerate(numeros):
    print(f"{indice}: {item}")
    #enumera as posições de itens numa lista
