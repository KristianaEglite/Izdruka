#uzdevums = pārveidot celsijus fārenheitos.
celsiji = [0, 10, 20, 34.5]
farenheiti = [(9 / 5) * temp + 32 for temp in celsiji]
print(farenheiti)

celsiji = [0, 10, 20, 60]
farenheiti = []
for temp in celsiji:
    f = (9 / 5) * temp + 32
    farenheiti.append(f)
print(farenheiti)