#GRUPPO: FERRANTE, RUSSO, BARRA

import random
import csv
import os.path as path

def extractor(filename):
    with open(filename, 'r', encoding='utf-8-sig') as f:
        reader = list(csv.reader(f))
        reader.pop(0)
        return reader[random.randint(0, len(reader)-1)]
        