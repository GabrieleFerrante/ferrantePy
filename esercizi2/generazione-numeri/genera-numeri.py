from random import randint

numeri = 100

with open("testo.txt", "w") as f:
    for i in range(numeri):
        f.write(str(randint(1,100)) + "\n")
