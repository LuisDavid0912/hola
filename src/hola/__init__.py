def main() -> None:
    try:
        edad = int(input('¿Cuántos años tienes? '))
    except ValueError:
        print('Eso eno es un numero valido')
        return

    tiene_id = True

    if edad < 18 or not tiene_id:
        print('Acceso denegado')
    else:
        print('bienvenido')





