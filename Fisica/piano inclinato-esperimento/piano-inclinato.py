import csv
from guizero import *
from math import sqrt
import matplotlib.pyplot as plt

#DATI
gradi_30_h, gradi_30_b = 19, 21
gradi_30_ipotenusa = round(sqrt(gradi_30_h**2 + gradi_30_b**2))
gradi_45_h, gradi_45_b = 16, 29
gradi_45_ipotenusa = round(sqrt(gradi_45_h**2 + gradi_45_b**2))
gradi_60_h, gradi_60_b = 12, 36
gradi_60_ipotenusa = round(sqrt(gradi_60_h**2 + gradi_60_b**2))

tempo_medio = 1.5
peso_corpo = 0.16


#PERCORSI FILE
file30_1 = './30/test1/data.csv'
file30_2 = './30/test2/data.csv'
file30_3 = './30/test3/data.csv'
file45_1 = './45/test1/data.csv'
file45_2 = './45/test2/data.csv'
file45_3 = './45/test3/data.csv'
file60_1 = './60/test1/data.csv'
file60_2 = './60/test2/data.csv'
file60_3 = './60/test3/data.csv'

#ESTRATTORE DATI
def data(path, column):
    output = []
    datas = []

    with open(path, 'r') as f:
        reader = csv.reader(f)
        i = 1
        for row in reader:
            if i <= 117:
                datas.append(row[column-1])
                i += 1
            else: break
    datas.pop(0)
    for j in datas:
        output.append(float(j))

    return output


#CALCOLO VELOCITA'
def speed(acceleration, mass):
    output = []
    for i in acceleration:
        output.append(i * mass)
    
    return output


#DATI
data30_1_acc = data(file30_1, 5)
data30_1_t = data(file30_1, 1)
data30_1_spd = speed(data30_1_acc, peso_corpo)

data30_2_acc = data(file30_2, 5)
data30_2_t = data(file30_2, 1)
data30_2_spd = speed(data30_2_acc, peso_corpo)

data30_3_acc = data(file30_3, 5)
data30_3_t = data(file30_3, 1)
data30_3_spd = speed(data30_3_acc, peso_corpo)


data45_1_acc = data(file45_1, 5)
data45_1_t = data(file45_1, 1)
data45_1_spd = speed(data45_1_acc, peso_corpo)

data45_2_acc = data(file45_2, 5)
data45_2_t = data(file45_2, 1)
data45_2_spd = speed(data45_2_acc, peso_corpo)

data45_3_acc = data(file45_3, 5)
data45_3_t = data(file45_3, 1)
data45_3_spd = speed(data45_3_acc, peso_corpo)


data60_1_acc = data(file60_1, 5)
data60_1_t = data(file60_1, 1)
data60_1_spd = speed(data60_1_acc, peso_corpo)

data60_2_acc = data(file60_2, 5)
data60_2_t = data(file60_2, 1)
data60_2_spd = speed(data60_2_acc, peso_corpo)

data60_3_acc = data(file60_3, 5)
data60_3_t = data(file60_3, 1)
data60_3_spd = speed(data60_2_acc, peso_corpo)


#GRAFICO
def graph(gradi):
    fig, (gf1, gf2, gf3) = plt.subplots(nrows=1, ncols=3)

    if gradi == 30 or gradi == '30':
        fig.suptitle('30 gradi')

        gf1.scatter(data30_1_t, data30_1_spd)
        gf1.scatter(data30_1_t, data30_1_acc)

        gf2.scatter(data30_2_t, data30_2_spd)
        gf2.scatter(data30_2_t, data30_2_acc)

        gf3.scatter(data30_3_t, data30_3_spd)
        gf3.scatter(data30_3_t, data30_3_acc)

        gf1.legend(['Velocità', 'Accelerazione'])
        gf2.legend(['Velocità', 'Accelerazione'])
        gf3.legend(['Velocità', 'Accelerazione'])

        txt_spd.clear()
        txt_spd.append(f'Velocità media: {round(gradi_30_ipotenusa / data30_1_t[-1])}')

    elif gradi == 45 or gradi == '45':
        fig.suptitle('45 gradi')

        gf1.scatter(data45_1_t, data45_1_spd)
        gf1.scatter(data45_1_t, data45_1_acc)

        gf2.scatter(data45_2_t, data45_2_spd)
        gf2.scatter(data45_2_t, data45_2_acc)

        gf3.scatter(data45_3_t, data45_3_spd)
        gf3.scatter(data45_3_t, data45_3_acc)

        gf1.legend(['Velocità', 'Accelerazione'])
        gf2.legend(['Velocità', 'Accelerazione'])
        gf3.legend(['Velocità', 'Accelerazione'])

        txt_spd.clear()
        txt_spd.append(f'Velocità media: {round(gradi_45_ipotenusa / data45_1_t[-1])}')

    else:
        fig.suptitle('60 gradi')

        gf1.scatter(data60_1_t, data60_1_spd)
        gf1.scatter(data60_1_t, data60_1_acc)

        gf2.scatter(data60_2_t, data60_2_spd)
        gf2.scatter(data60_2_t, data60_2_acc)

        gf3.scatter(data60_3_t, data60_3_spd)
        gf3.scatter(data60_3_t, data60_3_acc)

        gf1.legend(['Velocità', 'Accelerazione'])
        gf2.legend(['Velocità', 'Accelerazione'])
        gf3.legend(['Velocità', 'Accelerazione'])

        txt_spd.clear()
        txt_spd.append(f'Velocità media: {round(gradi_60_ipotenusa / data60_1_t[-1])}')



    plt.show()

#GUI

app = App(title='Grafici sul piano inclinato', width=1100, height=200, layout='grid', bg='#ffffff')

txt_30ht = Text(master=app, text = f'Altezza triangolo con 30 gradi: {gradi_30_h}cm', grid=[0,0], align='left')
txt_30bs = Text(master=app, text = f'Base triangolo con 30 gradi: {gradi_30_b}cm', grid=[0,1], align='left')
txt_30hy = Text(master=app, text = f'Ipotenusa triangolo con 30 gradi: {gradi_30_ipotenusa}cm', grid=[0,2], align='left')

txt_45ht = Text(master=app, text = f'Altezza triangolo con 45 gradi: {gradi_45_h}cm', grid=[1,0], align='left')
txt_45bs = Text(master=app, text = f'Base triangolo con 45 gradi: {gradi_45_b}cm', grid=[1,1], align='left')
txt_45hy = Text(master=app, text = f'Ipotenusa triangolo con 45 gradi: {gradi_45_ipotenusa}cm', grid=[1,2], align='left')

txt_60ht = Text(master=app, text = f'Altezza triangolo con 60 gradi: {gradi_60_h}cm', grid=[2,0], align='left')
txt_60bs = Text(master=app, text = f'Base triangolo con 60 gradi: {gradi_60_b}cm', grid=[2,1], align='left')
txt_60hy = Text(master=app, text = f'Ipotenusa triangolo con 60 gradi: {gradi_60_ipotenusa}cm', grid=[2,2], align='left')

txt_peso = Text(master=app, text = f'Peso del corpo: {gradi_60_ipotenusa}kg', grid=[3,0], align='left')
txt_superficie = Text(master=app, text = f'Materiale della superficie: Cartone', grid=[3,1], align='left')

but_30 = PushButton(app, command=graph, args=[30], text='30 gradi', grid=[0, 3])
but_45 = PushButton(app, command=graph, args=[45], text='45 gradi', grid=[1, 3])
but_60 = PushButton(app, command=graph, args=[60], text='60 gradi', grid=[2, 3])

txt_spd = Text(app, text='', grid=[0,4])

app.display()