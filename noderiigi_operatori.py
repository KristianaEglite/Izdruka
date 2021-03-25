#vienkarši piepildīt list [] ar elementiem
saraksts = list(range(0, 11, 2))  #no 0, līdz 10, ik pa 2
print(saraksts)

#enumerate - parāda indeksus tuple(atpakošana) formā
vards = "Pasaule"
for i in enumerate(vards):
    print(i)  #izdod indeksus katram vārdam

#atpakojot tuples
vards = "Pasaule"
for indekss, burts in enumerate(vards):
    print(indekss)
    print(burts)
    print("\n")

#zip - sapakot vairākus list kopā kā tuple
myList1 = [1, 2, 3]
myList2 = ["a", "b", "c"]
for i in zip(myList1, myList2):
    print(i) #sapako divus listus kopā, izveidojās tuple

myList3 = [100,200,300]
for i in zip(myList1, myList2, myList3):
    print(i) #ja pievieno ceturto elementu - nesanāks, jo jāsakrīt indeksu skaitam


#in izmanto, lai noskaidrotu vai objektā atrodams meklētais elements
print("x" in [1, 2, 3]) #meklēs vai x atrodas listā (bulleans - True/False)
print(2 in [1, 2, 3])
print("a" in "pasaule") 
print("myKey" in {"myKey":345})
d = {"myKey":345}
print(345 in d.keys())
print(345 in d.values())

#min un max
myList = [10,20,30,40,100]
print(min(myList))
print(max(myList))

#bibliotēku importēšana
#random - nejaušs gadījuma skaitlis
from random import shuffle
myList = [1,2,3,4,5,6,7,8,9,10]
print(myList)
shuffle(myList)
print(myList)

from random import randint
print(randint(0,100))