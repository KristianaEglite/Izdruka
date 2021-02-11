#lists jeb saraksti
[1, 2, 3, [4, 5]]
myList = ["teksts", 100, 12.8, "teksts"]
print(myList)
print(len(myList))
mylist = ["viens", "divi", "trīs", "četri"]
print(mylist)
print(mylist[0])  #izdrukā pirmo elementu (ar indeksu 0)
print(mylist[1:])  #izdrukā no otrā elementa līdz pēdējam

#var konkatinēt (apvienot)
cits_list = ["pieci", "seši"]
print(mylist +
      cits_list)  #izdrukā sarakstu apvienojumu, bet neizmaina pašus sarakstus
jauns_list = mylist + cits_list
print(jauns_list)
jauns_list[0] = 1  #definē pirmo elementu (aizstāaj iepriekšējo)
print(jauns_list)

#elementu pievienošana
jauns_list.append("septiņi")  #appent - pievieno
print(jauns_list)
jauns_list.append(8)
print(jauns_list)

#elementu noņemšana
jauns_list.pop() #ar "pop" noņem pēdējo elementu
print(jauns_list)
pop_elements = jauns_list.pop()
print(pop_elements) #izdrukā noņemto elmentu
jauns_list.pop(5) #noņem elementu ar norādīto indeksu
print(jauns_list)


#elementu kārtošana
new_list = ['b', 'a', 'z', 'e']
print(new_list)
new_list.sort()
print(new_list)
new_list.reverse()
print(new_list)
num_list = [4, 1, 8, 3]
print(num_list)
num_list.reverse()
print(num_list)
num_list.sort()
print(num_list)
s = [1, 2, 3, 100, 12.8]
s.sort()
print(s)

#saraksts sarakstā (nested)
nested_list = [8, 6, [5, 7]]
print(len(nested_list))
print(nested_list[1])
print(nested_list[2][1]) #izdrukā ligzsaraksta elementu

#piemēri
augli = ["ābols", "banāns", "gurķis"]
print (augli[2])
#aizstāt elementu - gurķis - apelsīns
augli[2] = "apelsīns"
print (augli)
#pievienot beigās bumbieris
augli.append("bumbieris")
print(augli)

#iespraust konkretā vietā jaunu elementu "citrons"
augli.insert(2,"citrons")
print(augli)
augli.pop(1)
print(augli)

#izdrukāt pilnā teikumā, cik augļu ir sarakstā
print(f"Šajā sarakstā ir {len(augli)} augļi.")