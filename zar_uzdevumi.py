#pirmais uzdevums
vards = input ("Ievadi tekstu: ")
x = len(vards)
print(len(vards))

#Otrais uzdevums
ievadi_vardu = input("Ievadi savu vārdu: ")
print (ievadi_vardu[0])

#Trešais uzdevums
saule = "Sveika pasaule"
pedejais = saule[9:]
print (pedejais)

#Ceturtais uzdevums
x = input("Uzraksti kādu teikumu: ")
print(x.upper())

#piektais uzdevums
x = input("Ievadi teikumu: ")
print(x.lower())

#sestais uzdevums
x = "Samērcēt"
pirmais_burts = x[1:]
print("P" + pirmais_burts)

#septītais  uzdevums
txt = " Sveika, Pasaule! "
x = txt.strip()
print(x)

#astotais uzdevums
txt = "Šis ir sākums"
x = txt.replace("sākums", "rezultāts")
print(x)

#devītais uzdevums
tavs_vards = input("Ieraksti savu vārdu: ")
x1 = tavs_vards[0]
x2 = tavs_vards[1:-1]
x3 = tavs_vards[-1]
print (x1.lower() + x2.lower() + x3.upper())
x4 = "?"
print("Pamatīgs juceklis, vai ne, " + x1 + x4)