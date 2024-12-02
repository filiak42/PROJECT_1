#slicing
print('Slicing slova indexovani:')
print('indexovani'[:5])
print('indexovani'[-5:])
print('indexovani'[::3])

print('\n' + '=' * 10 + '\n' )

#prevadec jednotek
print('Prevadec jednotek:')
kg_lb = 2.20
km_mile = 0.62
l_gal = 0.26

kg_pocet = 80
km_pocet = 54
l_pocet = 5

kg_vysledek = kg_lb * kg_pocet
km_vysledek = km_mile * km_pocet
l_vysledek = l_gal * l_pocet
 
print(str(kg_pocet) + ' kg je ' + str(kg_vysledek) + ' lb')
print(str(km_pocet) + ' km je ' + str(km_vysledek) + ' mil')
print(str(l_pocet) + ' l je ' + str(l_vysledek) + ' gal')

# Výsledky usporne
#print(kg_pocet, 'kg je', kg_vysledek, 'lb')
#print(km_pocet, 'km je', km_vysledek, 'mil')
#print(l_pocet, 'l je', l_vysledek, 'gal')

print('\n' + '=' * 10 + '\n' )

#Cena aut
print('Cena aut:')
mercedes = 150_000
rolls_royce = 400_000
vybava = 50_000
sleva_merc = 5000

print('Sleva na Mercedes: ', sleva_merc)
print('Cena za dva Mercedesy je: ', 2 * mercedes)
print('Cena za Mercedes a Rolls-Royce: ', mercedes + rolls_royce)
print('Cena za dva Rolls-Royce s priplatkovou vybavou: ', 2 * (rolls_royce + vybava))
print('Cena za Mercedes s priplatkovou vybavou: ', mercedes + vybava)
print('Cena za Mercedes po sleve: ', mercedes - sleva_merc)

print('\n' + '=' * 10 + '\n' )

#Cele jmeno
jmeno = "Lukas"
prijmeni = "Dvorak"
cele_jmeno = jmeno + " " + prijmeni
delka_jmena = len(cele_jmeno)
print('Cele jmeno: ', cele_jmeno)
print('Delka jmena: ', delka_jmena)
print('=' * delka_jmena)
print(cele_jmeno)
print('=' * delka_jmena)

print('\n' + '=' * 10 + '\n' )

#DESTINATION
mesta = ["Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]
ceny = (150, 200, 120, 120, 100, 180)
cara = "=" * 35
nabidka = """
1 - Praha   | 150,-Kč
2 - Viden   | 200,-Kč
3 - Olomouc | 120,-Kč
4 - Svitavy | 120,-Kč
5 - Zlin    | 100,-Kč
6 - Ostrava | 180,-Kč
"""

print("VITEJTE U NASI APLIKACE DESTINATIO!")
print(cara)

print(nabidka)
print(cara)

destinace = input("CISLO DESTINACE: ")
jmeno = input("JMENO: ")
prijmeni = input("PRIJMENI: ")
email = input("E-MAIL: ")

print(cara)

cilova_stanice = mesta[int(destinace) - 1] # mesta[int(destinace) - 1
finalni_cena = ceny[int(destinace) - 1]

print(cilova_stanice)
print(finalni_cena, ",-Kč", sep='')

print(cara)

print("Cestujici:", jmeno, prijmeni)
print("Cilova destinace:", cilova_stanice)
print("Cena jizdneho:", finalni_cena, ",-Kč")
print("Jizdenku jsme odeslali na e-mail", email)