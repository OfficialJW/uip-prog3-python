import re

if __name__ == '__main__':

    patrones = '[a-ce-gi-oq-z0-9][a-z0-9][{a-df-qs-z}\s][{a-ce-z}\s]'
    palabras = ['rap them', 'tapeth', 'Apt', 'apth', 'tarreth', 'wrap/try', 'aleht', 'peth',
                'sap tray', '87ap9th', 'apothecary', 'happy them', 'tarpth', 'ddpdg']

    for palabra in palabras:
        if re.match(patrones, palabra):
            print("La palabra " + palabra + " es correcta.")
        else:
            print("La palabra " + palabra + " no es correcta.")