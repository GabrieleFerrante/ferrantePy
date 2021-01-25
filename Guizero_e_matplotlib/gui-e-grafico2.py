from os import read
from random import randint
import matplotlib.pyplot as plt
from guizero import *

app = App(title="Lettura dati-2", width = 600, height = 600, bg = "#ffffff")
graph = Picture(app, image = None)

coordX = []
coordY = []

def data2coord():
    
    datas = ""

    for line in range(100):
        datas = datas + str(randint(1, 100)) + "," + str(randint(1, 100)) + "\n"

    f = open(box_dati.value, "w")

    f.write(datas)

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


label = Text(app, text = "Inserisci il nome del file da generare:")
box_dati = TextBox(app, width = 40)
but = PushButton(app, command = grafico, text = "Genera")
destroy_button = PushButton(app, command = graph.destroy, text = "Elimina grafico")

app.display()