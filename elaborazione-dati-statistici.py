from tkinter import Image, image_names
import matplotlib.pyplot as plt
from guizero import *
import csv

datiPc = "dati-pc.csv"
datiInternet = "dati-internet.csv"
datiSelezionati = {
    "dati": "",
    "anno": "",
    "utilizzo": ""
}


#FUNZIONI
def select_pc():
    datiSelezionati["dati"] = datiPc
    print(datiSelezionati["dati"])

def select_internet():
    datiSelezionati["dati"] = datiInternet
    print(datiSelezionati["dati"])

def select_2018():
    datiSelezionati["anno"] = "2018"
    print(datiSelezionati["anno"])

def select_2019():
    datiSelezionati["anno"] = "2019"
    print(datiSelezionati["anno"])

def select_non_usano():
    datiSelezionati["utilizzo"] = "no"
    print(datiSelezionati["utilizzo"])

def select_usano():
    datiSelezionati["utilizzo"] = "si"
    print(datiSelezionati["utilizzo"])

#CSV
x = []
y = []

def csv2data():
    datas = []

    with open(datiSelezionati["dati"], "r") as file:
        reader = csv.reader(file)
        for row in reader:
            datas.append(row)

    datas.pop(0)

    if y != []:
        for i in y:
            y.pop(0)

    if datiSelezionati["dati"] == datiPc:
        if datiSelezionati["anno"] == "2018":
            if datiSelezionati["utilizzo"] == "si":
                for i in range(13):
                    x.append(datas[i][1])
                    y.append(datas[i][2])
            else:
                for i in range(13):
                    x.append(datas[i][1])
                    y.append(datas[i][7])
        else:
            if datiSelezionati["utilizzo"] == "si":
                for i in range(14,26):
                    x.append(datas[i][1])
                    y.append(datas[i][7])
            else:
                for i in range(14,26):
                    x.append(datas[i][1])
                    y.append(datas[i][7])
    else:
        if datiSelezionati["anno"] == "2018":
            if datiSelezionati["utilizzo"] == "si":
                for i in range(12):
                    x.append(datas[i][1])
                    y.append(datas[i][2])
            else:
                for i in range(12):
                    x.append(datas[i][1])
                    y.append(datas[i][7])
        else:
            if datiSelezionati["utilizzo"] == "si":
                for i in range(13,24):
                    x.append(datas[i][1])
                    y.append(datas[i][2])
            else:
                for i in range(13,24):
                    x.append(datas[i][1])
                    y.append(datas[i][7])

#GRAFICO

def grafico():
    csv2data()
    plt.bar(x, y, width=0.6)
    # plt.set_xscale("linear")
    plt.xticks(rotation=328)
    plt.savefig("elaborazione-dati-statistici.png")
    graph = Picture(app, image="elaborazione-dati-statistici.png", grid=[2,0])

#GUI

app = App(title="Grafico", bg="#ffffff", layout="grid")
message = Text(app, text="Seleziona i parametri del grafico", grid=[0,0], width="fill", height="fill")
butPc = PushButton(app, grid=[0,1], command=select_pc, text="PC")
butInt = PushButton(app, grid=[1,1], command=select_internet, text="Internet")
but18 = PushButton(app, grid=[0,2], command=select_2018, text="2018")
but19 = PushButton(app, grid=[1,2], command=select_2019, text="2019")
butUsano = PushButton(app, grid=[0,3], command=select_usano, text="Usano")
butNonUsano = PushButton(app, grid=[1,3], command=select_non_usano, text="Non usano")
gen_but = PushButton(app, grid=[0,4], command=grafico, text="Genera")

app.display()