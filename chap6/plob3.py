geek = {"404": "clueless.",
"Link Rot" : "the process by which web page links become obsolete.", 
"Uninstalled" : "being fired.  Especially popular during the dot-bomb era."}  

choice = None
while choice != "0":

      print("  Geek Translator")
      print("  0 - Quit") 
      print("  1 - Look Up a Geek Term")
      print("  2 - Add a Geek Term")
      print("  3 - Redefine a Geek Term")
      print("  4 - Delete a Geek Term")

      choice = input("Choice: ")
      print()

      if choice == "0":
          print("QUIT")

      elif choice == "1":
          term = input("What term do you want me to translate?: ")
          if term in geek:
              GEEK = geek[term]
              print("\n", term, "means", GEEK)
          else:
              print("\nI have no idea what ", term, "is")
      
      elif choice == "2":
          term = input("ADD: ")
          if term not in geek:
              print("\n", term, "Added.")

      elif choice == "3":
          term = input("REDEFINE GEEK : ")
          if term in geek:
              print("\n", term, "Redefined.")


      elif choice == "4":
          term = input("DELETE GEEK : ")
          if term in geek:
              del geek[term]
              print("Deleted", term)
