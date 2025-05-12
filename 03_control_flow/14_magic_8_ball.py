#The Magic 8 Ball is a popular office toy and children's toy invented in the 1940s for fortune-telling and advice seeking. 🎱

#It's an oversized 8 ball with some of the following answers:

#Yes - definitely.
#It is decidedly so.
#Without a doubt.
#Reply hazy, try again.
#Ask again later.
#Better not tell you now.
#My sources say no.
#Outlook not so good.
#Very doubtful.
#Create a magic8.py program that can respond to any Yes or No questions with a different answer each time it executes.

#The output should have the following format:

#Question:      [Question]
#Magic 8 Ball:  [Answer]

#For example:

#Question:      Is Codédex better than Udemy yet?
#Magic 8 Ball:  Better not tell you now.

import random

pergunta = input("Qual sua dúvida? ")

rand_num = random.randint(1,9)

if rand_num == 1:
  print("Sem dúvida.")
elif rand_num == 2:
  print("As estrelas dizem que sim.")
elif rand_num == 3:
  print("Melhor não te contar agora.")
elif rand_num == 4:
  print("Não conte com isso.")
elif rand_num == 5:
  print("Perspectiva boa.")
elif rand_num == 6:
  print("Me pergunte depois do café.")
elif rand_num == 7:
  print("Sinais apontam para não.")
elif rand_num == 8:
  print("Sim… mas com consequências.")
else:
  print("Resposta turva, tente novamente.")
