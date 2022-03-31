class Quarto:

    def __init__(self, nome="", dimensoes=""):
        self.nome = nome
        self.dimensoes = dimensoes


class Mobilia:

    def __init__(self, nome="", funcao="", material="", quarto=None):
        self.nome = nome
        self.funcao = funcao
        self.material = material
        self.quarto = quarto

    def __repr__(self):
        s = self.nome + "," + self.funcao + "," + self.material
        if self.quarto:
            s += str(self.quarto)
        return s


class Casa:

    def __init__(self, formato="", quartos=None):
        self.formato = formato
        self.quartos = quartos

    def __repr__(self):
        s = self.formato
        for q in self.quartos:
            s += "," + str(q)
        return s


if __name__ == "__main__":
    q1 = Quarto(nome="Sala", dimensoes="5x6m")
    m1 = Mobilia(nome="armario", funcao="coisa da sala",
                 material="madeira", quarto=q1)
    c1 = Casa(formato="Germanica", quartos=[q1])

    print(q1)
    print(m1)
    print(c1)
