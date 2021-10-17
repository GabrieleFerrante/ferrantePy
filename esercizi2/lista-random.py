from random import randint

numeri = []

for i in range(5):
    numeri.append(randint(1, 8))

print(numeri)

carattere = input("Scegli un carattere da contare: ")
counter = 0

for i in numeri:
    if (carattere == str(i)):
        counter += 1

print(f"Il carattere {carattere} compare {counter} volte.")
