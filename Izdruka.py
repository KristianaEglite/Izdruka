#komentārus var
#rakstīt vairākās
#rindās
print("Sveika, pasaule!")
print(2 * 2)
print(2 * 2, 2 * 3, 2 * 4, "Python")
print(f"Ja saskaitīsim 5 ar 7, iegūsim {5+7}."
      )  #kombinētā izdruka - teksts un aprēķins
print("Sveika, " + "pasaule!")
print("Kristiāna " * 5)
print(f"Šajā gadā būs {365*60*60*24} sekundes.")
print(0.1 + 0.2 - 0.3)
print()

#Mainīgie
a = 5
print(a)
print(a + a)
a = a + a  #zīme "=" nozīmē piešķiršanu
print(a)
print(type(a))
a = 30.1
print(type(a))  #float=decimāldaļas

mani_ieākumi = 430
nodoklis = 0.1  #10%
maniNodokli = mani_ieākumi * nodoklis
print(maniNodokli)

#help
help("keywords")

#Datu ievade - input
#Pirmā versija
print("Ievadi vārdu: ")
x = input()
print("Tavs ievadītais vārds ir " + x)

#Otrā versija
x = input("Ievadi vārdu: ")
print("Tavs ievadītais vārds ir " + x)

#Skaitļu ievade 
skaitlis = int( input("Ievadi veselu skaitli: ")) #pārveido ievadīto datu tipu par int
print(f"Tavs ievadītais skaitlis ir {skaitlis}.")