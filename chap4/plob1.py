import random as rd
mood = rd.randrange(5) 
print("I sense your energy. Your true emotions are coming across my screen.")
print("You are....")
if mood == 0:
  print(" ----------")
  print("l          l")
  print("l  0    0  l")
  print("l    <     l")
  print("l '-....-' l")
  print(" ----------")
elif mood == 1:
  print(" ----------")
  print("l          l")
  print("l  0    0  l")
  print("l    <     l")
  print("l  ------- l")
  print(" ----------")
elif mood == 2:
  print(" ----------")
  print("l          l")
  print("l  0    0  l")
  print("l    <     l")
  print("l .-''''-. l")
  print(" ----------")
elif mood == 3:
  print(" ----------")
  print("l  U    U  l")
  print("l  0    0  l")
  print("l  | <  |  l")
  print("l    __    l")
  print(" ----------")

else:
  print("Illegal mood value!")

print("....today.")

print("\nPress the enter key to quit")
