"""
#Nr1
a = int(input("Ievadi veselu skaiti: "))
for skaitlis in range(1, a + 1):
    if (skaitlis % 2 != 0):
        print(skaitlis)
#Nr2
a = int(input("Ievadi vienu veselu skaiti: "))
b = int(input("Ievadi otru veselu skaiti: "))
if (a<b):
    for i in range(a,b+1):
        print(i)
else:
    for c in range(a,b-1,-1):
        print(a)
        a = a-1
#Nr3
a = int(input("Ievadi veselu skaiti: "))
while (a>=0):
    if(a%2 == 0):
        print(a)
    a = a -1

#Nr4
myList = []
for i in range(10):
    n = float(input(f"Ievadi {i+1}. skaitli: "))
    myList.append(n)
print(myList)


#Nr5
sk = 1
a = int(input("Ievadi veselu skaitli: "))
while (sk*sk<=a):
    print(sk**2)
    sk+=1


#Nr6
a = int(input("Ievadi veselu skaitli lielāku, vai vienādu ar 2: "))
n=0
while (a<2):
    a = int(input("Ievadi veselu skaitli lielāku par 2: "))
dalitajs = 2
while True:
    if n % dalitajs ==0:
        print(f"Mazākais skaitlis, ar ko {a} dalās bez atlikuma, ir {dalitajs}.")
        break
    else:
        dalitajs += 1
"""
#Nr7
x = 5
a = ""
for sk in range(x, 5):
    a = a + str(sk)
    print(a)
