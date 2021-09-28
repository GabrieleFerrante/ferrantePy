giorni = int(input("Giorni di noleggio: "))

costo_totale = giorni * 40
if giorni == 1:
    costo_totale += 5

print("Il costo totale del noleggio sarà " + str(costo_totale) + "€")
