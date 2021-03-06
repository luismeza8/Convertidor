def decimal_a_octal(decimal):
    octal = ""
    negativo = False

    if decimal < 0:
        negativo = True
        decimal = +abs(decimal)

    while decimal > 0:
        residuo = decimal % 8
        octal = str(residuo) + octal
        decimal = int(decimal / 8)

    if negativo:
        return f"-{octal}"

    return octal


def octal_a_decimal(octal):
    decimal = 0
    posicion = 0
    negativo = False

    # Comprobamos si el número es negativo
    if octal[0] == "-":
        negativo = True
        octal = octal[1:]

    # Invertir octal, porque debemos recorrerlo de derecha a izquierda
    # pero for in empieza de izquierda a derecha
    octal = octal[::-1]

    for digito in octal:
        valor_entero = int(digito)
        numero_elevado = int(8 ** posicion)
        equivalencia = int(numero_elevado * valor_entero)
        decimal += equivalencia
        posicion += 1

    # Si el número ingresado es negativo el número decimal se pasa a negativo
    if negativo:
        return -abs(int(decimal))

    return decimal
