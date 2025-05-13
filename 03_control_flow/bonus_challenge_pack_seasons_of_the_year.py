#Ah, the four seasons in the year — winter, spring, summer, or fall; all you have to do is call!

#Ask the user the month number using the input() function.

#Check for the four seasons using an if/elif/else statement and logical operators:

#month is 1, 2, 3, print 'Winter 🌨️'
#month is 4, 5, 6, print 'Spring 🌱'
#month is 7, 8, 9, print 'Summer 🌻'
#month is 10, 11, 12, print 'Autumn 🍂'
#Everything else is 'Invalid'
#Logical operators in Python include the and and or keywords. Which one should you use?

month = int(input("Informe um mês do ano pelo seu número: "))

if month >= 1 and month <= 3:
    print('Winter 🌨️')
elif month >= 4 and month <= 6:
    print('Spring 🌱')
elif month >= 7 and month <= 9:
    print('Summer 🌻')
elif month >= 10 and month <= 12:
    print('Autumn 🍂')
else:
    print('Invalid')