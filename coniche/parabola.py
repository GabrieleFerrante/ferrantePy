class Parabola:
    def __init__(self, tipo="PARAMETRI", *args):
        if tipo == "PARAMETRI":
            self.__a = args[0]
            self.__b = args[1]
            self.__c = args[2]
            self.__delta = self.__b ** 2 - (4 * self.__a * self.__c)
        else:
            raise Exception("Il tipo specificato non è un'opzione")

    # PROPRIETA' DELLA PARABOLA
    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b

    @property
    def c(self):
        return self.__c

    @property
    def vertice(self):
        x = -(self.__b / (2 * self.__a))
        y = -(self.__delta / (4 * self.__a))
        return x, y

    @property
    def asse(self):
        return -self.__b / (2 * self.__a)

    @property
    def fuoco(self):
        x = -(self.__b / (2 * self.__a))
        y = (1 - self.__delta) / (4 * self.__a)
        return x, y

    @property
    def direttrice(self):
        return -((1 + self.__delta) / (4 * self.__a))


def main():
    parabola = Parabola()


if __name__ == '__main__':
    main()
