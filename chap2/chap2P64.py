print("                         Trust Fund Buddy")
print("Totals our monthly spending so that your trust fund doesn't run out")
print("<and you're forced to get a real job>.")
print("")
print("Please enter the requested, monthly costs.   Since you;re rish, ignore pennies and use only doller amounts.")
print("")
print("")

Lam = input("Lamborghini Tune-Ups: ")
Lam = int(Lam)
Man = int(input("Manhattan Apartment: "))
Pri = int(input("Private Jet Rental: "))
Gift = int(input("Gifts: "))
Din = int(input("Dinning Out: "))
Sta = int(input("Staff <butlers, chep, driver, assistant>: "))
Pers = int(input("Personal Guru and Coach: "))
Com = int(input("Computer Games: "))

total = Lam + Man + Pri + Gift + Din + Sta + Pers + Com

print("\nGrand Total: ", total)
