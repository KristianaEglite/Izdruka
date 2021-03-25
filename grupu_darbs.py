#Nosacījums: Aprēķini ievadīto naturālo skaitļu faktoriālo summu.
n = int(input("Ievadi naturālu skaitli: "))
while True:
    if n<1:
        n = (input("Ievadi naturālu skaitli: "))
    else:
        break

faktorials = 1
summa = 0

for i in range(n):
    faktorials = faktorials*(i+1)
    summa = summa + faktorials
    print(faktorials, summa) #pārbaudīt
print (f"Pirmo {n} skaitļu faktoriālu summa ir {summa}.")