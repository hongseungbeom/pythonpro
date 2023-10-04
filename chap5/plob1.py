inventory =()
inventory = ("sword","armor", "shield","healing potion")
print("Your items:")
for item in inventory:
  print (item)

print("\nPress the enter key to continue.")
print("You have", len(inventory), "items in your possesstion.")

print("\nPress the enter key to continue.")
if "healing potion" in inventory:
  print("You will live to fight another day")

a = int(input("\nEnter the index number for an item in inventory:"))
print("At index", a, "is", inventory[a])

slice1 = int(input("Enter the index number to begin a slice:"))
slice2 = int(input("Enter the index number to end a slice:"))
print("inventory[ ",slice1," : ",slice2," ]                     ", end='')
item = ['sword','armor', 'shield','healing potion']
print(item[slice1:slice2])

print("\nPress the enter key to continue.")
print("You find a chest. It contains:")
print("<'gold', 'gems'>")
chest = ("gold", "gems")
inventory += chest
print("You add the contents of the chest to your inventory.")
print("Your inventory is now:")
print(inventory)
