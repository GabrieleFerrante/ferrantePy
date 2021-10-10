class Retta:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def getA(self):
        return self.__a

    def getB(self):
        return self.__b

    def getC(self):
        return self.__c

    def eqImplicita(self):
        # PRIMO TERMINE
        incognita_1 = f"{self.__a}x" if self.__a != 0 else ""
        incognita_1 = f"x" if self.__a == 1 else incognita_1
        incognita_1 = f"-x" if self.__a == -1 else incognita_1
        incognita_1 = incognita_1 if self.__a <= 0 else f"+{incognita_1}"

        # SECONDO TERMINE
        incognita_2 = f"{self.__b}y" if self.__b != 0 else ""
        incognita_2 = f"y" if self.__b == 1 else incognita_2
        incognita_2 = f"-y" if self.__b == -1 else incognita_2
        incognita_2 = incognita_2 if self.__b <= 0 else f"+{incognita_2}"

        # TERMINE NOTO
        noto = f"{self.__c}" if self.__c != 0 else ""
        noto = noto if self.__c <= 0 else f"+{noto}"

        return f"{incognita_1}{incognita_2}{noto}=0"

    def eqEsplicita(self):
        if self.__b == 0:
            raise ZeroDivisionError

        b = self.__b if self.__b >= 0 else -self.__b

        # VARIABILE INDIPENDENTE
        a = self.__a if self.__b >= 0 else -self.__a

        ind = f"{a}/{b}x" if abs(self.__b) != 1 else f"{a}x"
        ind = ind if a <= 0 else f"+{ind}"
        ind = ind if a != 0 else ""

        # TERMINE NOTO
        c = self.__c if self.__b >= 0 else -self.__c

        noto = f"{c}/{b}" if abs(self.__b) != 1 else f"{c}"
        noto = noto if c <= 0 else f"+{noto}"
        noto = noto if c != 0 else ""

        return f"y={ind}{noto}"

    def trovaY(self, x):
        return x, round(self.__a / self.__b * x + self.__c / self.__b, 2)

    def punti(self, n, m):
        return [self.trovaY(i) for i in range(min(n, m), max(n, m) + 1)]

    def m(self):
        if self.__b != 0:
            return self.__a / self.__b
        else:
            raise ZeroDivisionError


def main():
    a, b, c = [float(i) if not float(i).is_integer() else round(float(i)) for i in
               input("Inserisci a, b e c separati da spazi: ").split()]

    retta = Retta(a, b, c)
    print(type(retta.m()))


if __name__ == '__main__':
    main()