#GRUPPO: FERRANTE, RUSSO, BARRA

import random
import csv
import os.path as path

running_file = path.basename(__file__)
file_dir = __file__.replace(running_file, '')
data_path = file_dir + 'versi.csv'


def extractor(filename):
    with open(filename, 'r') as f:
        reader = list(csv.reader(f))
        reader.pop(0)
        return reader[random.randint(0, len(reader)-1)]

while True:
    print(extractor(data_path)[0])
    print(extractor(data_path)[1])
    print(extractor(data_path)[2])
    print('\n')

    inp = input('Scrivi "Fatto" per concludere o qualcos\'altro per continuare:\n')
    if inp.lower() == 'fatto' or inp.lower() == 'done':
        break