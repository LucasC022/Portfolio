from random import *

numero_intentos = 8
numero_pensado = randint(1, 100)
lista_numeros = []

print("\n\t\tBienvenido al adivina adivinador\n")
nombre_competidor = input("Por favor, para empezar introduce tu nombre: ")
print(f"\nBueno querido/a {nombre_competidor}, estoy pensando un número entre 1 y 100 y solo tenés 8 intentos para adivinar qué numero es")

numero_competidor = int(input("\n¿Qué número crees que estoy pensando?: "))
while numero_intentos != 0 or numero_competidor != numero_pensado:
    if numero_competidor > numero_pensado:
        print(f"\nUff {nombre_competidor}, casi pero no. El número que elegiste es mayor.")
        numero_competidor = int(input("Vuelve a intentarlo. ¿Qué número crees que estoy pensando?: "))
        numero_intentos -= 1
        lista_numeros.append(numero_competidor)
    elif numero_competidor < numero_pensado:
        print(f"\nUff {nombre_competidor}, casi pero no. El número que elegiste es menor.")
        numero_competidor = int(input("Vuelve a intentarlo. ¿Qué número crees que estoy pensando?: "))
        numero_intentos -= 1
        lista_numeros.append(numero_competidor)
    else: 
        print(f"\nFelicitaciones {nombre_competidor}, has introducido el numero correctamente. El número que había pensado era el {numero_pensado}")
        lista_numeros.append(numero_competidor)
        break


print(f"\nLos numeros introducidos fueron; {lista_numeros}\n")
if numero_competidor != numero_pensado:
    print(f"\nLo siento, se han terminado los intentos. Estoy seguro que la próxima lo lograrás.")