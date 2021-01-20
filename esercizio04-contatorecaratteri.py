from collections import Counter

stringa = input("Inserisci una stringa: ")
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVXYZ"

#ESECUZIONE

stringa = stringa.upper()
contatore = Counter()

for carattere in stringa:
    contatore[carattere] += 1

dizionario_finale = dict(contatore)

for keys, values in dizionario_finale.items():
    print(f'Carattere: "{keys}", Ripetizioni: "{values}"')
