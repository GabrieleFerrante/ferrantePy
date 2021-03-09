print("Inserisci 5 numeri:")

numeri = []

for i in range(5):
    numero = input(f"Numero {i+1}:")
    try:
        int(numero)
        numeri.append(numero)
    except:
        print("Deve essere un numero intero.")
        break

print(list(reversed(numeri)))