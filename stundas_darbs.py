"""
#pirmais uzdevums
a = 15
b = 2.5
c = 4.78
#lielākais skaitlis
if (a > b) and (a > c):
    print("15 ir lielākais skaitlis")
elif(b > a) and (b > c):
    print ("2.5 ir lielākais skaitlis")
else:
    print("4.78 ir lielākais skaitlis")

#mazākais skaitlis
if (a < b) and (a < c):
    print("15 ir mazākais skaitlis")
elif (b < a) and (b < c):
    print("2.5 ir mazākais skaitlis")
else:
    print("4.8 ir mazākais skaitlis")

#risinājums ar list
myList = [a, b, c]
myList.sort()
print(
    f"Lielākais skaitlis ir {myList[-1]}, bet mazākais skaitlis ir {myList[0]}"
)

#otrais uzdevums
gradi = float(input("Ievadi tavu ķermeņa temperatūru skaitļos: "))
if (gradi < 35):
    print("Vai nav par aukstu?")
elif (gradi >= 35) and (gradi <= 37):
    print("Viss kārtībā")
else:
    print("Iespējams drudzis")
"""
#stundas uzdevums
atr = ""
if (atr == "banka"):
    print ("Te ir daudz naudas")
elif (atr == "veikals"):
    print("Jānopērk āboli")
elif (atr == "aptieka"):
    print("Man ir iesnas")
else:
    print ("Ābolu nav")