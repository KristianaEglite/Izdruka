def saskaiti_skaitlus(sk1, sk2):
    rez = sk1 + sk2
    return rez
rez1 = (saskaiti_skaitlus(5, 11))
rez2 = (saskaiti_skaitlus(2.5,6.5))
rez3 = (saskaiti_skaitlus(-2, -3.5))
print(rez1 * rez2 * rez3)

#noskairdo vai tas ir pāra skaitlis
def parbaudi_pari(skaitlis):
    return skaitlis % 2 == 0

print(parbaudi_pari(45))
print(parbaudi_pari(2))

#atgriež true, ja sarakstā ir kaut viens pāra skaitlis
def parbaudi_pari_list(saraksts):
    for skaitlis in saraksts:
        if skaitlis % 2 == 0:
            return True
print(parbaudi_pari_list([1,5,3]))