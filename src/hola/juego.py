import random

secreto = random.randint(1, 100)

def main() -> None:
    intentos = 0

    while True:                      # bucle del juego
        try:
            tu_numero = int(input('¿Cuál crees que es el número? '))
        except ValueError:
            print('Eso no es un número válido')
            continue                 # vuelve a preguntar, sin comparar
        intentos += 1


        if tu_numero == secreto:
            print('¡Felicidades! Lo lograste en', intentos, 'intentos')
            break                    # aquí sí se acaba el juego
        elif tu_numero < secreto:
            print('Más alto')
        else:
            print('Más bajo')

main()
print(secreto)



