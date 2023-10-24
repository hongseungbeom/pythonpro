print("   High Scores Keeper")
print("\n  0-Quit")
print("  1-List Scores")
print("  2-Add a Score")

scores = [("Moe", 1000), ("Larry", 1500)]

a = input("Choice: ")
while a != 0:
  if a == 1:
    for x in scores:
      print(x)
      print("High Scores")
  else :
    name = input("What is the player's name?: ")
    score = int(input("What score did the player get?:"))
    scores.append((name, score))
    scores.sort(key=lambda x: x[1], reverse=True)
    print(scores)
  a = input("Choice: ")
