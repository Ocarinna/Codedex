#Create a todo.py program that will define a todo list that contains the following items:

#'🏦 Get quarters.'
#'🧺 Do laundry.'
#'🌳 Take a walk.'
#'💈 Get a haircut.'
#'🍵 Make some tea.'
#'💻 Complete Lists chapter.'
#'💖 Call mom.'
#'📺 Watch My Hero Academia.'
#Print the first item and the second item. What did you get?

#Next, use slicing to print the third, fourth, and fifth items.

#Try printing out the item at index 9 to see the IndexError before moving on.

todo = ['🏦 Get quarters.', '🧺 Do laundry.', '🌳 Take a walk.', '💈 Get a haircut.', '🍵 Make some tea.', '💻 Complete Lists chapter.', '💖 Call mom.', '📺 Watch My Hero Academia.']

print(todo[1], todo[2])

print(todo[2 : 5])

print(todo[9])