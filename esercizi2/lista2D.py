from random import randint

righe = 3
colonne = 3

griglia = []

for x in range(righe):    
    colonna = []
    for y in range(colonne):
        colonna.append(randint(1, 50))
    griglia.append(colonna)


for i in range(len(griglia)):
    print(griglia[i])


sel_riga = int(input("Scegli una riga: ")) - 1
sel_colonna = int(input("Scegli una colonna: ")) - 1

print(f"L'elemento selezionato è {griglia[sel_riga][sel_colonna]}")