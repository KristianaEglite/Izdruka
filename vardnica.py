#vārdnīcas jeb dictionaries (datu tips)
tel = {
    "direktors": "67947253",
    "vietnieks": "65676869",
    "sekretāre": "62468315"
}
print(tel["direktors"])

cenas = {
  "piens": 1.12, 
  "āboli":0.95, 
  "apelsīni":1.89}

print(cenas["piens"])
print(cenas["apelsīni"])

d = {
  "k1": 123, #integer
  "k2":[10,11,12], #list/saraksts
  "k3":{"atsl1":100, "atsl2":200} #vēlviena vardnīca
} #vārdnīcās var uzglabāt dāžadus datu tipus
print(d["k1"])
print(d["k3"]["atsl1"])
print(d["k2"][2])

my_dict = {'key1':['a','b','c']}
print(my_dict)
my_list = my_dict['key1']
burts = my_list[2]
print(burts)
print(burts.upper())
print(my_dict['key1'][2].upper())
print(my_dict['key1'][1].upper())

#pievienot jaunus objektus
new_dict = {'k1':100, 'k2':200}
print(new_dict)
new_dict['k3'] = 300 #definē jaunu elementu
print(new_dict)
new_dict['k1'] = "simts" #aizstāj elementus
print(new_dict)

#vārdnīu medotes
print(new_dict.keys()) #izdrukā atslēgas
print(new_dict.values()) #izdruka vērtības
print(new_dict.items()) #izdrukā pārus

vertibu_list = list(new_dict.values()) #pārveido vērtības par list
print(vertibu_list)

print(new_dict.get('k1')) #get() izdot norādītās atslegas vertību
print(new_dict.pop('k1')) #pop() izņem pēdējo elementu
print(new_dict)
new_dict.update({'k4':9}) #pievieno jaunu elementu pāri
print(new_dict)
new_dict.clear() #iztukšo/iztīra vārdīcu
print(new_dict)
