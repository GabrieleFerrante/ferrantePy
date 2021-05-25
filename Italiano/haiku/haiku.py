#GRUPPO: FERRANTE, RUSSO, BARRA

import random
import csv



def extractor(filename):
    with open(filename, 'r', encoding='utf8') as f:
        reader = list(csv.reader(f))
        reader.pop(0)

        output = reader[random.randint(-2, len(reader)-1)]

        return output 

print(extractor('versi.csv'))