#Autori: Ferrante Gabriele, Russo Jorge, Barra Mario
import os
from typing import List
import matplotlib.pyplot as plt
from guizero import *
import csv

datiPc = "dati-pc.csv"
datiInternet = "dati-internet.csv"
datiSelezionati = {
    "dati": datiPc,
    "anno": "2018",
    "utilizzo": "si"
}
nomeImmagineGrafico = "elaborazione-dati-statistici.png"
colore = ""

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

def esadecimale(n):
    if n < 16:
        return str(hex(n)).replace("x","")
    elif n >= 16 and n <= 255:
        return str(hex(n)).replace("0x","")

#CSV

x = []
y = []

def csv2data():

    global x, y

    datas = []

    with open(datiSelezionati["dati"], "r") as file:
        reader = csv.reader(file)
        for row in reader:
            datas.append(row)

    datas.pop(0)

    if y != []:
         y = []
    
    if x != []:
        x = []

    if datiSelezionati["dati"] == datiPc:
        if datiSelezionati["anno"] == "2018":
            if datiSelezionati["utilizzo"] == "si":
                for i in range(13):
                    x.append(datas[i][1])
                    valore = datas[i][2].replace(",",".")
                    y.append(float(valore))
            else:
                for i in range(13):
                    x.append(datas[i][1])
                    valore = datas[i][7].replace(",",".")
                    y.append(float(valore))
        else:
            if datiSelezionati["utilizzo"] == "si":
                for i in range(13,26):
                    x.append(datas[i][1])
                    valore = datas[i][7].replace(",",".")
                    y.append(float(valore))
            else:
                for i in range(13,26):
                    x.append(datas[i][1])
                    valore = datas[i][7].replace(",",".")
                    y.append(float(valore))
    else:
        if datiSelezionati["anno"] == "2018":
            if datiSelezionati["utilizzo"] == "si":
                for i in range(12):
                    x.append(datas[i][1])
                    valore = datas[i][2].replace(",",".")
                    y.append(float(valore))
            else:
                for i in range(12):
                    x.append(datas[i][1])
                    valore = datas[i][7].replace(",",".")
                    y.append(float(valore))
        else:
            if datiSelezionati["utilizzo"] == "si":
                for i in range(12,24):
                    x.append(datas[i][1])
                    valore = datas[i][2].replace(",",".")
                    y.append(float(valore))
            else:
                for i in range(12,24):
                    x.append(datas[i][1])
                    valore = datas[i][7].replace(",",".")
                    y.append(float(valore))

#GRAFICO

def grafico():
    csv2data()
    colore = "#" + esadecimale(red_slider.value) + esadecimale(green_slider.value) + esadecimale(blue_slider.value)

    if os.path.exists(nomeImmagineGrafico):
        os.remove(nomeImmagineGrafico)
    else: pass

    plt.bar(x, y, width=0.6, color=colore)
    plt.xticks(rotation=328)
    plt.savefig(nomeImmagineGrafico)
    plt.clf()

    graph = Picture(app, image=nomeImmagineGrafico, grid=[2,2])

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
testo_colore = Text(app, text="Colore del grafico:", grid=[4, 0])
red_slider = Slider(app, end=255, grid=[4,1])
red_slider.text_color = "#ff0000"
green_slider = Slider(app, end=255, grid=[4,2])
green_slider.text_color = "#00ff00"
blue_slider = Slider(app, end=255, grid=[4,3])
blue_slider.text_color = "#0000ff"

app.display()
