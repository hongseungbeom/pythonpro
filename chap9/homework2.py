class Food:
  def __init__(self, name, level):
      self.name = name
      self.level = level

  def get_level(self):
      return self.level

  def set_critter_level(self, critter):
      critter.hunger -= self.level
      if critter.hunger < 0:
          critter.hunger = 0
      critter._Critter__pass_time()


class Critter(object):
  """A virtual pet"""

  def __init__(self, name, hunger=0, boredom=0):
      self.name = name
      self.hunger = hunger
      self.boredom = boredom

  def __pass_time(self):
      self.hunger += 1
      self.boredom += 1

  @property
  def mood(self):
      unhappiness = self.hunger + self.boredom
      if unhappiness < 5:
          m = "happy"
      elif 5 <= unhappiness <= 10:
          m = "okay"
      elif 11 <= unhappiness <= 15:
          m = "frustrated"
      else:
          m = "mad"
      return m

  def talk(self):
      print("I'm", self.name, "and I feel", self.mood, "now.")
      self.__pass_time()

  def feed(self, food):
      print("Brruppp. Thank you for the", food.name + ".")
      food.set_critter_level(self)

  def play(self, fun=4):
      print("Wheee!")
      self.boredom -= fun
      if self.boredom < 0:
          self.boredom = 0
      self.__pass_time()


def main():
  crit_name = input("What’s your critter’s name?: ")
  crit = Critter(crit_name)
  
  food1 = Food("사료", 3)
  food2 = Food("고기", 5)
  food3 = Food("개껌", 4)

  choice = None
  while choice != "0":
      print(
          """
      Critter Caretaker

      0 - Quit
      1 - Listen to your critter
      2 - Feed your critter
      3 - Play with your critter
      """
      )
      choice = input("Choice: ")
      print()

      if choice == "0":
          print("Good-bye.")
      elif choice == "1":
          crit.talk()
      elif choice == "2":
          print("Choose a food item:")
          print("1 -", food1.name)
          print("2 -", food2.name)
          print("3 -", food3.name)
          food_choice = input("Food Choice: ")

          if food_choice == "1":
              crit.feed(food1)
          elif food_choice == "2":
              crit.feed(food2)
          elif food_choice == "3":
              crit.feed(food3)
          else:
              print("\nSorry, invalid food choice.")
      elif choice == "3":
          crit.play()
      else:
          print("\nSorry,", choice, "isn't a valid choice.")


main()
input("\n\nPress the enter key to exit.")
