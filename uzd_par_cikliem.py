#uzd1
#lietotājs ievada divus skaitļus. Izdrukāt visus skaitļus, kas atrodas pa vidu/izdrukā visus intervāla skaitļus. Abus galapunktus ieskaitot.

viens = int(input("Ievadi vienu skaitļus: "))
divi = int(input("Ievadi citu skaitļus: "))
for skaitli in range(viens, divi+1):
    print(skaitli)

#uzd2
#aprēķināt skaitļa faktoriālu izmantojot ciklu. Lietotājs ievada veselu skaitli. Faktoriāls = 1*2*3*...*n.
a = int(input("Ievadi veselu skaitļus: "))
faktorials = 1
for i in range(1,a+1):
    faktorials = faktorials * i
print(f"Skaitļa {a} faktoriāls ir {faktorials}")

#uzd3
#no lietotāja ievadīta intervāla, izvadi visus veselos skaitļus, kas dalās ar konkrētu skaitli(norāda lietotājs)
a = int(input("Ievadi sākuma skaitļus: "))
b = int(input("Ievadi beigu skaitļus: "))
c = int(input("Ievadi skaitli, ar kuru dalīt: "))
for i in range(a, b + 1):
    if (i % c == 0):
        print(i)
