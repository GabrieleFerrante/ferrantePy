alunni = [
    {'nome': 'Mario', 'voti': {'matematica': 6, 'italiano': 6, 'scienze': 7, 'inglese': 4}},
    {'nome': 'Giovanni', 'voti': {'matematica': 4, 'italiano': 6, 'scienze': 5, 'inglese': 7}},
    {'nome': 'Paola', 'voti': {'matematica': 9, 'italiano': 6, 'scienze': 8, 'inglese': 8}}
]

for i in alunni:
    nome = i['nome']
    media = sum(i['voti'].values()) / len(i['voti'])
    print(f'La media dei voti di {nome} è {media}')