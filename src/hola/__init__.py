def main() -> None:
    while True:
        try:
            edad = int(input('¿Cuántos años tienes? '))
            break
        except ValueError:
            print('Eso no es un número valido, intenta de nuevo')
           

    tiene_id = True

    if edad < 18 or not tiene_id:
        print('Acceso denegado')
    else:
        print('bienvenido')






