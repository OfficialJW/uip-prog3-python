print("     Palabra Secreta")
nombre = input("Ingrese el nombre: ")

palabra_secreta = "azul"

print("Hola! " + nombre)
print("Intenta adivinar la palabra que va en el espacio de la oracion. Tienes 3 intentos.")
print("Mi color favorito es sereno y calmante. El color es: ")

intentos = 0

while intentos < 2:
    palabra = input("Ingrese la palabra: ").lower()

    if palabra not in palabra_secreta:
        print("Incorrecto! Intenta de nuevo.")
        intentos += 1

    else:
        print("Enhorabuena! Conseguistes la palabra secreta!")
        exit();

palabra = input("Ingrese la palabra: ").lower()
if palabra not in palabra_secreta:
    print("Incorrecto! Se te acabaron los intentos.")
    intentos += 1











