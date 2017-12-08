from cmath import pi


class Esfera(object):
    def __init__(self, r):
        self.radio = r
        self.volumen = 0

    def obtvol(self):
        r = self.radio
        self.volumen = (4 / 3) * pi * (r ** 3)
        return self.volumen


class Cilindro(object):
    def __init__(self, r, h):
        self.radio = r
        self.altura = h
        self.volumen = 0


    def obtvol(self):
        r = self.radio
        h = self.altura
        self.volumen = pi * (r ** 2) * h
        return self.volumen


class Cono(object):
    def __init__(self, r, h):
        self.radio = r
        self.altura = h
        self.volumen = 0

    def obtvol(self):
        r = self.radio
        h = self.altura
        self.volumen = (1 / 3) * pi * (r ** 2) * h
        return self.volumen


if __name__ == '__main__':
    o = 'y'

    while o == "Y" or o == "y":

        opc = input("Ingrese la figura geometrica que desee encontrar (Cilindro, Cono o Esfera): ").lower()
        if opc == "esfera":
            print("     Esfera")
            r = int(input("Ingrese el radio de la esfera: "))
            s = Esfera(r)
            print("El volumen de la esfera es: ", s.obtvol())
        elif opc == "cono":
            print("     Cono")
            r = int(input("Ingrese el radio de el cono: "))
            h = int(input("Ingrese la altura de el cono: "))
            d = Cono(r, h)
            print("El volumen de el cono es: ", d.obtvol())
        elif opc == "cilindro":
            print("     Cilindro")
            r = int(input("Ingrese el radio de el cilindro: "))
            h = int(input("Ingrese la altura de el cilindro: "))
            c = Cilindro(r, h)
            print("El volumen de el cilindro es: ", c.obtvol())
        else:
            print("Figura erronea, vuelva a intentarlo.")

        o = input("Desea continuar? Y o N: ")
