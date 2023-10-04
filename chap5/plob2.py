import random as rd
print("Welcome to Word Jumble!")
print("Unscramble the letters to make a word.")
words = ('difficult', 'banana', 'apple', 'python', 'daegu', 'catholic', 'university')
a = rd.choice(words)
answer = a
a = list(a)
rd.shuffle(a)
print("Jumble word: ", end='')
for i in a: 
  print(i, end='')
b = input("\nYour guess:")
if (answer == b):
  print("correct")
else:
  print("Sorry, that's not correct. The word was :", answer)
 
