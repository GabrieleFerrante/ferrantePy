import csv
import matplotlib.pyplot as plt
import os.path as path


running_file = path.basename(__file__)
file_dir = __file__.replace(running_file, '')


# ESTRATTORE DATI
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

# CALCOLATORE VELOCITA'


def speed(acceleration, time):
    return [i*time[acceleration.index(i)] for i in acceleration]

# GRAFICI


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

    plt.show()


# DATI
peso_corpo = 0.16

dati0_1 = {
    'Tempo': data(file_dir + 'gradi0/dati_1.csv', 1),
    'Accelerazione x': data(file_dir + 'gradi0/dati_1.csv', 2),
    'Accelerazione y': data(file_dir + 'gradi0/dati_1.csv', 4),
    'Accelerazione': data(file_dir + 'gradi0/dati_1.csv', 5),
}
dati0_1['Velocità x'] = speed(dati0_1['Accelerazione x'], dati0_1['Tempo'])
dati0_1['Velocità y'] = speed(dati0_1['Accelerazione y'], dati0_1['Tempo'])
dati0_1['Velocità'] = speed(dati0_1['Accelerazione'], dati0_1['Tempo'])

dati0_2 = {
    'Tempo': data(file_dir + 'gradi0/dati_2.csv', 1),
    'Accelerazione x': data(file_dir + 'gradi0/dati_2.csv', 2),
    'Accelerazione y': data(file_dir + 'gradi0/dati_2.csv', 4),
    'Accelerazione': data(file_dir + 'gradi0/dati_2.csv', 5)
}
dati0_2['Velocità x'] = speed(dati0_2['Accelerazione x'], dati0_2['Tempo'])
dati0_2['Velocità y'] = speed(dati0_2['Accelerazione y'], dati0_2['Tempo'])
dati0_2['Velocità'] = speed(dati0_2['Accelerazione'], dati0_2['Tempo'])

dati30_1 = {
    'Tempo': data(file_dir + 'gradi30/dati_1.csv', 1),
    'Accelerazione x': data(file_dir + 'gradi30/dati_1.csv', 2),
    'Accelerazione y': data(file_dir + 'gradi30/dati_1.csv', 4),
    'Accelerazione': data(file_dir + 'gradi30/dati_1.csv', 5)
}
dati30_1['Velocità x'] = speed(dati30_1['Accelerazione x'], dati30_1['Tempo'])
dati30_1['Velocità y'] = speed(dati30_1['Accelerazione y'], dati30_1['Tempo'])
dati30_1['Velocità'] = speed(dati30_1['Accelerazione'], dati30_1['Tempo'])

dati30_2 = {
    'Tempo': data(file_dir + 'gradi30/dati_2.csv', 1),
    'Accelerazione x': data(file_dir + 'gradi30/dati_2.csv', 2),
    'Accelerazione y': data(file_dir + 'gradi30/dati_2.csv', 4),
    'Accelerazione': data(file_dir + 'gradi30/dati_2.csv', 5)
}
dati30_2['Velocità x'] = speed(dati30_2['Accelerazione x'], dati30_2['Tempo'])
dati30_2['Velocità y'] = speed(dati30_2['Accelerazione y'], dati30_2['Tempo'])
dati30_2['Velocità'] = speed(dati30_2['Accelerazione'], dati30_2['Tempo'])

scelta_gradi = input('Scegli tra 0 gradi o 30 gradi: ')
scelta_lancio = input('Scegli il lancio tra 1 e 2: ')

# OUTPUT
if str(scelta_gradi) == '0':
    if str(scelta_lancio) == '1':
        print('Velocità iniziale: ' + str(dati0_1['Accelerazione x'][0]*dati0_1['Tempo'][0]) + 'm/s')

        graph(scelta_gradi, scelta_lancio, dati0_1['Tempo'], dati0_1['Accelerazione x'], dati0_1['Velocità x'],
              dati0_1['Accelerazione y'], dati0_1['Velocità y'], dati0_1['Accelerazione'], dati0_1['Velocità'])
    elif str(scelta_lancio) == '2':
        print('Velocità iniziale: ' + str(dati0_2['Accelerazione x'][0]*dati0_2['Tempo'][0]) + 'm/s')

        graph(scelta_gradi, scelta_lancio, dati0_2['Tempo'], dati0_2['Accelerazione x'], dati0_2['Velocità x'],
              dati0_2['Accelerazione y'], dati0_2['Velocità y'], dati0_2['Accelerazione'], dati0_2['Velocità'])
    else:
        print(f'{scelta_lancio} non è un\'opzione')
elif str(scelta_gradi) == '30':
    if str(scelta_lancio) == '1':
        print('Velocità iniziale: ' + str(dati30_1['Accelerazione x'][0]*dati30_1['Tempo'][0]) + 'm/s')

        graph(scelta_gradi, scelta_lancio, dati30_1['Tempo'], dati30_1['Accelerazione x'], dati30_1['Velocità x'],
              dati30_1['Accelerazione y'], dati30_1['Velocità y'], dati30_1['Accelerazione'], dati30_1['Velocità'])
    elif str(scelta_lancio) == '2':
        print('Velocità iniziale: ' + str(dati30_2['Accelerazione x'][0]*dati30_2['Tempo'][0]) + 'm/s')

        graph(scelta_gradi, scelta_lancio, dati30_2['Tempo'], dati30_2['Accelerazione x'], dati30_2['Velocità x'],
              dati30_2['Accelerazione y'], dati30_2['Velocità y'], dati30_2['Accelerazione'], dati30_2['Velocità'])
    else:
        print(f'{scelta_lancio} non è un\'opzione')
else:
    print(f'{scelta_gradi} non è un\'opzione')
