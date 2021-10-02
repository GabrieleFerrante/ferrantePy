class Retta:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def eqImplicita(self):
        # PRIMO TERMINE
        incognita_1 = f"{self.a}x" if self.a != 0 else ""
        incognita_1 = f"x" if self.a == 1 else incognita_1
        incognita_1 = f"-x" if self.a == -1 else incognita_1
        incognita_1 = incognita_1 if self.a <= 0 else f"+{incognita_1}"

        # SECONDO TERMINE
        incognita_2 = f"{self.b}y" if self.b != 0 else ""
        incognita_2 = f"y" if self.b == 1 else incognita_2
        incognita_2 = f"-y" if self.b == -1 else incognita_2
        incognita_2 = incognita_2 if self.b <= 0 else f"+{incognita_2}"

        # TERMINE NOTO
        noto = f"{self.c}" if self.c != 0 else ""
        noto = noto if self.c <= 0 else f"+{noto}"

        return f"{incognita_1}{incognita_2}{noto}=0"

    def eqEsplicita(self):
        if self.b == 0:
            return "Se b è uguale a 0 non è possibile esplicitare l'equazione."

        b = self.b if self.b >= 0 else -self.b

        # VARIABILE INDIPENDENTE
        a = self.a if self.b >= 0 else -self.a

        ind = f"{a}/{b}x" if abs(self.b) != 1 else f"{a}x"
        ind = ind if a <= 0 else f"+{ind}"
        ind = ind if a != 0 else ""

        # TERMINE NOTO
        c = self.c if self.b >= 0 else -self.c

        noto = f"{c}/{b}" if abs(self.b) != 1 else f"{c}"
        noto = noto if c <= 0 else f"+{noto}"
        noto = noto if c != 0 else ""

        return f"y={ind}{noto}"

    def punti(self, x):
        return x, round(self.a / self.b * x + self.c / self.b, 2)


def main():
    a, b, c = [float(i) if float(i).is_integer() else round(float(i)) for i in
               input("Inserisci a, b e c separati da spazi: ").split()]

    retta = Retta(a, b, c)
    print(f"Equazione implicita: {retta.eqImplicita()}")
    print(f"Equazione esplicita: {retta.eqEsplicita()}")
    print(f"x e y dato x={retta.punti(float(input('Inserisci x: ')))}")


if __name__ == '__main__':
    main()
