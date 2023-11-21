try:
  num = float(input("Enter a number: "))
except ValueError:

  print("That's not a number!")


for value in (None, "Hi!"):
  try:
      print("Attempting to convert", value, "->")
      print(float(value))
  except (TypeError, ValueError):

      print("Something went wrong!")


for value in (None, "Hi!"):
  try:
      print("Attempting to convert", value, "->")
      print(float(value))
  except TypeError:

      print("Can only convert string or number")
  except ValueError:

      print("Can only convert a string of digits!")

try:
  num = float(input("\nEnter a number: "))
except ValueError as e:

  print("Not a number! Or as Python would say:\n", e)

try:
  num = float(input("\nEnter a number: "))
except ValueError:
  # Handle the case where the input is not a valid number
  print("That was not a number!")
else:
  # Execute if no exception is raised
  print("You entered the number", num)
