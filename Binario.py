def decimal_a_binario(decimal):
    negativo = False

    if decimal < 0:
        negativo = True
        decimal = +abs(decimal)

    # Aquí almacenamos el resultado
    binario = ""

    # Mientras se pueda dividir
    while decimal > 0:
        # Saber si es 1 o 0
        residuo = int(decimal % 2)

        # Ir dividiendo el decimal
        decimal = int(decimal / 2)

        # Ir agregando 1 o 0 a la izquierda del resultado
        binario = str(residuo) + binario

    if negativo:
        return f"-{binario}"

    return binario


def binario_a_decimal(binario):
    posicion = 0
    decimal = 0
    negativo = False

    # Comprobamos si el número es negativo
    if binario[0] == "-":
        negativo = True
        binario = binario[1:]

    # Invertir la cadena porque debemos recorrerla de derecha a izquierda
    binario = binario[::-1]

    for digito in binario:
        # Elevar 2 a la posición actual
        multiplicador = 2**posicion
        decimal += int(digito) * multiplicador
        posicion += 1

    # Si el número ingresado es negativo el número decimal se pasa a negativo
    if negativo:
        return -abs(int(decimal))

    return decimal
