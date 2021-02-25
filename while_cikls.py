#while True:
#    print("Sveiki!") #drukās bezgalīgi daudz

i = 0  #tipisks cikla mainīgais
while (i < 5):
    print("Sveiki!")
    i += 1  #tas pats kas i=1+1
print("i tagad ir", i)

j = 0
while (j<5):
    print("Sveiki, nr.", j)
    j+=1

while (i > 0):
    print("Saskaitām atpakaļ", i)
    i -= 1

#ar soli 2
i = 20
while True:
    print("i ir", i)
    if (i > 26):
        break
    i += 2


#studas uzdevums 2
augstums = int(input("Kāds būs stāvu skaits? "))
i = 0
while (i < augstums):
    print("*" * augstums)
    i += 1
