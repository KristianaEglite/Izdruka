"""
vards = input("Kā tevi sauc? ")
print(f"Tavs vārds ir {vards}")

gadi = int(input("Cik tev gadu? "))
print(f"Tev ir {gadi} gadi.")
dzimsanasGads = 2021 - gadi
print(f"Tavs dzimšanas gads ir {dzimsanasGads}.")


celsijs = int(input("Uzraksti temperatūru pēc Celsija grādiem:"))
gradi = celsijs * 9 / 5 + 32
print(f"Temperatūra pēc Farenheita būs {celsijs} pēc Celsija skalas ir {gradi} gradi pēc Farenheita skalas.")

platums = float(input("Uzraksti telpas platumu: "))
garums = float(input("Uzraksti telpas garumu: "))
augstums = float(input("Uzraksti telpas augstumu: "))
tilpums = platums * garums * augstums
print(f"Telpas tilpums ir {tilpums}")
"""

#Strings (rakstzīmju virknes)
print("Sveiki!")
print('sveiki')
print("i'm going on a run")
print('Arī šis ir "risinājums"')
print("Sveika, \npasaule!") 
print("Sveika, \tpasaule!")

#String garums - len()
print(len("sveiki"))
print(len("Ko tu domā?"))
# [sākums:beigas:solis]
myString = "Sveiki, pasaule!"
print(myString)
print(myString[0]) #izdrukā pirmo rakstzīmi
print(myString[8])#izdrukā 9. rakstzīmi
print(myString[13])#izdrukā 14. rakstzīmi
print(myString[-2])#izdrukā 14. rakstzīmi
print(myString[-1])#izdrukā pēdējo rakstzīmi