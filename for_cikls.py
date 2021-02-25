#iterācija - kādas darbības atkārtota izpildīšana (iterable)
mainigais = [1, 2, 3]  #list
for elements in mainigais:
    print(elements)

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for x in myList:
    print(x)

for _ in myList:  #var nerakstīt cikla mainīgo
    print("Sveiki")

#atrast pāra skaitļus
for skaitlis in myList:
    if (skaitlis % 2 == 0):
        print(skaitlis)
    else:
        print(f"Nepāra skaitlis: {skaitlis}")

#aprēķināt summu
summa = 0
for sk in myList:
    summa = summa + sk
    print(f"Pēc {sk} skaitļu saskaitīšanas summa ir {summa}")

print(summa)

#drukā tekstu
myString = "Sveika pasaule!"
for burts in myString:
    print(burts, end = " ")

for burts in "programma":
    print(burts, end = " ")

#drukā tuple
tup = (1, 2, 3, 4)
for elements in tup:
    print(elements)

myList = [(1, 2),(3,4),(5,6),(7,8)] #sapakotie tuples / packed tuples
print(len(myList))

for elements in myList:
    print(elements)

for (a,b) in myList: #atpako - tuple unpacking
    print(a)

myList = [(1,2,3),(4,5,6),(7,8,9)]
for (a,b,c) in myList:
    print(c)

#vārdnīcas 
d = {"k1":11, "k2":12, "k3":13}
for elements in d:
    print(elements) #izdrukā atslēgas

for elements in d.items():
    print(elements) #izdrukā atslēgu/vērtību pārus
    
for atslega,vertiba in d.items():
    print(vertiba)

#izdrukā skaitļus ar range 
for skaitlis in range(15): #intervāls no [0;15)
    print(skaitlis +1) 

for skaitlis in range(4,15): #intervāls [4;15)
    print(skaitlis)

for skaitlis in range(4,15,3):#sākot ar 4, beidzot ar 15, izdrukā katru trešo
    print(skaitlis)
