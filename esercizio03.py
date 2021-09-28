stringa = input("Inserisci una stringa:")
alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]


def trova_carattere_ripetuto(a):
    for i in range(26):
        for x in a:
            if x == alfabeto[i]:
                print("filler")


trova_carattere_ripetuto(stringa)

# Non sono riuscito a svolgere l'esercizio
