def clasificar_numero(numero, umbral=50):

    return "Alto" if numero >= umbral else "Bajo"


def clasificar_lista(numeros, umbral=50):

    return [clasificar_numero(n, umbral) for n in numeros]
