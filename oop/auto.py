class Auto:
    garanzia = 1
    assicurazione = True
    parcoAuto = 0

    def __init__(self, proprietario, marca, modello, cilindrata, cavalli, colore):
        self.proprietario = proprietario
        self.marca = marca
        self.modello = modello
        self.cilindrata = cilindrata
        self.cavalli = cavalli
        self.colore = colore

        Auto.parcoAuto += 1

    # Funzioni Get
    def getProprietario(self):
        return self.proprietario

    def getMarca(self):
        return self.marca

    def getModello(self):
        return self.modello

    def getCilindrata(self):
        return self.cilindrata

    def getCavalli(self):
        return self.cavalli

    def getColore(self):
        return self.colore

    def getAll(self):
        return (f"\nProprietario: {self.proprietario}"
                f"\nMarca: {self.marca}"
                f"\nModello: {self.modello}"
                f"\nCilindrata: {self.cilindrata}"
                f"\nCavalli: {self.cavalli}"
                f"\nColore: {self.colore}")

    # Funzioni Set
    def setProprietario(self, value):
        self.proprietario = value

    def setMarca(self, value):
        self.marca = value

    def setModello(self, value):
        self.modello = value

    def setCilindrata(self, value):
        self.cilindrata = value

    def setCavalli(self, value):
        self.cavalli = value

    def setColore(self, value):
        self.colore = value


def main():
    auto_giovanni = Auto("Giovanni", "Ford", "Fiesta", 1500, 200, "Verde")
    print(auto_giovanni.getAll())


if __name__ == "__main__":
    main()
