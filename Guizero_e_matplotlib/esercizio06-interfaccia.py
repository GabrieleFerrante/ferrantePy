from os import read
from random import randint
import matplotlib.pyplot as plt
from guizero import *

coordX = []
coordY = []

def data2coord():

    f = open(box_dati.value, "r")

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

def grafico():

    data2coord()
    plt.plot(coordX, coordY)
    plt.savefig("grafico.png")
    plt.clf()
    graph = Picture(app, image = "grafico.png")


app = App(title="Lettura dati", width = 600, height = 600, bg = "#ffffff")

label = Text(app, text = "Inserisci il nome del file da leggere:")
box_dati = TextBox(app, width = 40)
but = PushButton(app, command = grafico, text = "Genera")


app.display()
