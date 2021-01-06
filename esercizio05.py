from os import read
from random import randint
import matplotlib.pyplot as plt
import numpy as np

coordX = []
coordY = []

datas = ""

for line in range(100):
    datas = datas + str(randint(1, 100)) + "," + str(randint(1, 100)) + "\n"

 #print(f"Dati: \n{datas}")


f = open("esercizio05-dati.txt", "w")

f.write(datas)

f = open("esercizio05-dati.txt", "r")

for line in f:
    values = str(f.readline())
    values = values.strip("\n")
    values = values.split(",")
    values = list(values)
    coordX.append(int(values[0]))
    coordY.append(int(values[1]))

f.close()

coordX.sort()
coordY.sort()

print("Valori")
print(f"X: {coordX}")
print(f"Y: {coordY}")

plt.plot(coordX, coordY)
plt.ylabel("Random generated numbers")
plt.show()