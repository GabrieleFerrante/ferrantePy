import csv
import matplotlib.pyplot as plt

#ESTRATTORE DATI
def data(path, column):
    with open(path, 'r') as f:
        datas = list(csv.reader(f))
        datas.pop(0)
        output = []
        counter = 0
        for i in datas:
            if counter <= 236:
                output.append(round(float(i[column-1],), 2))
            counter += 1
        return output

#CALCOLATORE VELOCITA'
def speed(acceleration, mass):
    output = []
    for i in acceleration:
        output.append(i * mass)
    return output

#GRAFICI
def graph(deg, testNum, time, accX, velX, accY, velY, absAcc, absVel):
    fig, (gf1, gf2, gf3) = plt.subplots(nrows=1, ncols=3)

    fig.suptitle(f'{deg} gradi-Lancio N°{testNum}')

    gf1.plot(time, velX)
    gf1.plot(time, accX)
    gf1.legend(['Velocità x', 'Accelerazione x'])

    gf2.plot(time, velY)
    gf2.plot(time, accY)
    gf2.legend(['Velocità y', 'Accelerazione y'])

    gf3.plot(time, absVel)
    gf3.plot(time, absAcc)
    gf3.legend(['Velocità assoluta', 'Accelerazione assoluta'])
    
    plt.savefig(f'./gradi{deg}_{testNum}.png')
    plt.show()


#DATI
peso_corpo = 0.16

dati0_1 = {
    'Tempo': data('./gradi0/dati_1.csv', 1),
    'Accelerazione x': data('./gradi0/dati_1.csv', 2),
    'Accelerazione y': data('./gradi0/dati_1.csv', 3),
    'Accelerazione': data('./gradi0/dati_1.csv', 5),
}
dati0_1['Velocità x'] = speed(dati0_1['Accelerazione x'], peso_corpo)
dati0_1['Velocità y'] = speed(dati0_1['Accelerazione y'], peso_corpo)
dati0_1['Velocità'] = speed(dati0_1['Accelerazione'], peso_corpo)

dati0_2 = {
    'Tempo': data('./gradi0/dati_2.csv', 1),
    'Accelerazione x': data('./gradi0/dati_2.csv', 2),
    'Accelerazione y': data('./gradi0/dati_2.csv', 3),
    'Accelerazione': data('./gradi0/dati_2.csv', 5)
}
dati0_2['Velocità x'] = speed(dati0_2['Accelerazione x'], peso_corpo)
dati0_2['Velocità y'] = speed(dati0_2['Accelerazione y'], peso_corpo)
dati0_2['Velocità'] = speed(dati0_2['Accelerazione'], peso_corpo)

dati30_1 = {
    'Tempo': data('./gradi30/dati_1.csv', 1),
    'Accelerazione x': data('./gradi30/dati_1.csv', 2),
    'Accelerazione y': data('./gradi30/dati_1.csv', 3),
    'Accelerazione': data('./gradi30/dati_1.csv', 5)
}
dati30_1['Velocità x'] = speed(dati30_1['Accelerazione x'], peso_corpo)
dati30_1['Velocità y'] = speed(dati30_1['Accelerazione y'], peso_corpo)
dati30_1['Velocità'] = speed(dati30_1['Accelerazione'], peso_corpo)

dati30_2 = {
    'Tempo': data('./gradi30/dati_2.csv', 1),
    'Accelerazione x': data('./gradi30/dati_2.csv', 2),
    'Accelerazione y': data('./gradi30/dati_2.csv', 3),
    'Accelerazione': data('./gradi30/dati_2.csv', 5)
}
dati30_2['Velocità x'] = speed(dati30_2['Accelerazione x'], peso_corpo)
dati30_2['Velocità y'] = speed(dati30_2['Accelerazione y'], peso_corpo)
dati30_2['Velocità'] = speed(dati30_2['Accelerazione'], peso_corpo)

scelta_gradi = input('Scegli tra 0 gradi o 30 gradi: ')
scelta_lancio = input('Scegli il lancio tra 1 e 2: ')

if str(scelta_gradi) == '0':
    if str(scelta_lancio) == '1':
        graph(scelta_gradi, scelta_lancio, dati0_1['Tempo'], dati0_1['Accelerazione x'], dati0_1['Velocità x'], dati0_1['Accelerazione y'], dati0_1['Velocità y'], dati0_1['Accelerazione'], dati0_1['Velocità'])
        print('Intervallo di tempo: ' + dati0_1['Tempo'][-1]-dati0_1['Tempo'][0])
        print('Differenza di velocità x: ' + dati0_1['Velocità x'][-1]-dati0_1['Velocità x'][0])
        print('Differenza di velocità y: ' + dati0_1['Velocità y'][-1]-dati0_1['Velocità y'][0])
        print('Differenza di velocità assoluta: ' + dati0_1['Velocità'][-1]-dati0_1['Velocità'][0])
        print('Differenza di accelerazione x: ' + dati0_1['Accelerazione x'][-1]-dati0_1['Accelerazione x'][0])
        print('Differenza di accelerazione y: ' + dati0_1['Accelerazione y'][-1]-dati0_1['Velocità y'][0])
        print('Differenza di accelerazione assoluta: ' + dati0_1['Accelerazione'][-1]-dati0_1['Accelerazione'][0])

    elif str(scelta_lancio) == '2':
        graph(scelta_gradi, scelta_lancio, dati0_2['Tempo'], dati0_2['Accelerazione x'], dati0_2['Velocità x'], dati0_2['Accelerazione y'], dati0_2['Velocità y'], dati0_2['Accelerazione'], dati0_2['Velocità'])
        print('Intervallo di tempo: ' + dati0_2['Tempo'][-1]-dati0_2['Tempo'][0])
        print('Differenza di velocità x: ' + dati0_2['Velocità x'][-1]-dati0_2['Velocità x'][0])
        print('Differenza di velocità y: ' + dati0_2['Velocità y'][-1]-dati0_2['Velocità y'][0])
        print('Differenza di velocità assoluta: ' + dati0_2['Velocità'][-1]-dati0_2['Velocità'][0])
        print('Differenza di accelerazione x: ' + dati0_2['Accelerazione x'][-1]-dati0_2['Accelerazione x'][0])
        print('Differenza di accelerazione y: ' + dati0_2['Accelerazione y'][-1]-dati0_2['Velocità y'][0])
        print('Differenza di accelerazione assoluta: ' + dati0_2['Accelerazione'][-1]-dati0_2['Accelerazione'][0])
    
    else: print(f'{scelta_lancio} non è un\'opzione')
elif str(scelta_gradi) == '30':
    if str(scelta_lancio) == '1':
        graph(scelta_gradi, scelta_lancio, dati30_1['Tempo'], dati30_1['Accelerazione x'], dati30_1['Velocità x'], dati30_1['Accelerazione y'], dati30_1['Velocità y'], dati30_1['Accelerazione'], dati30_1['Velocità'])
        print('Intervallo di tempo: ' + dati30_1['Tempo'][-1]-dati30_1['Tempo'][0])
        print('Differenza di velocità x: ' + dati30_1['Velocità x'][-1]-dati30_1['Velocità x'][0])
        print('Differenza di velocità y: ' + dati30_1['Velocità y'][-1]-dati30_1['Velocità y'][0])
        print('Differenza di velocità assoluta: ' + dati30_1['Velocità'][-1]-dati30_1['Velocità'][0])
        print('Differenza di accelerazione x: ' + dati30_1['Accelerazione x'][-1]-dati30_1['Accelerazione x'][0])
        print('Differenza di accelerazione y: ' + dati30_1['Accelerazione y'][-1]-dati30_1['Velocità y'][0])
        print('Differenza di accelerazione assoluta: ' + dati30_1['Accelerazione'][-1]-dati30_1['Accelerazione'][0])

    elif str(scelta_lancio) == '2':
        graph(scelta_gradi, scelta_lancio, dati30_2['Tempo'], dati30_2['Accelerazione x'], dati30_2['Velocità x'], dati30_2['Accelerazione y'], dati30_2['Velocità y'], dati30_2['Accelerazione'], dati30_2['Velocità'])
        print('Intervallo di tempo: ' + dati30_2['Tempo'][-1]-dati30_2['Tempo'][0])
        print('Differenza di velocità x: ' + dati30_2['Velocità x'][-1]-dati30_2['Velocità x'][0])
        print('Differenza di velocità y: ' + dati30_2['Velocità y'][-1]-dati30_2['Velocità y'][0])
        print('Differenza di velocità assoluta: ' + dati30_2['Velocità'][-1]-dati30_2['Velocità'][0])
        print('Differenza di accelerazione x: ' + dati30_2['Accelerazione x'][-1]-dati30_2['Accelerazione x'][0])
        print('Differenza di accelerazione y: ' + dati30_2['Accelerazione y'][-1]-dati30_2['Velocità y'][0])
        print('Differenza di accelerazione assoluta: ' + dati30_2['Accelerazione'][-1]-dati30_2['Accelerazione'][0])
    
    else: print(f'{scelta_lancio} non è un\'opzione')
else: print(f'{scelta_gradi} non è un\'opzione')