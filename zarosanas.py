#zarošanās if/else/elif(kombinācija else+if)
"""
if nosacījums:
    izplidāmā darbība
elif cits nosacījums:
    izpildāmā darbība
else:
    izpildāmā darbība (visos pārējios gadījumos)
    """
x = 6
if (x > 5):
    print("Skaitlis ir lielāks par 5")
elif (x > 0):
    print("Skaitlis ir lielāks par 0")
else:
    print("Nav pozitīvs skaitlis")

if True:
    print("Patiesi") 

suns_grib_est = False
if suns_grib_est:
    print("Pabaro suni")
else:
    print("Suns ir paēdis")