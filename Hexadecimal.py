negativo = False


def obtener_caracter_hexadecimal(valor):
    # Se necesita como String
    valor = str(valor)

    equivalencias = {
        "10": "A",
        "11": "B",
        "12": "C",
        "13": "D",
        "14": "E",
        "15": "F",
    }
    if valor in equivalencias:
        return equivalencias[valor]
    else:
        return valor


def decimal_a_hexadecimal(decimal):
    hexadecimal = ""
    while decimal > 0:
        residuo = decimal % 16
        verdadero_caracter = obtener_caracter_hexadecimal(residuo)
        hexadecimal = verdadero_caracter + hexadecimal
        decimal = int(decimal / 16)
    return hexadecimal


def obtener_valor_real(caracter_hexadecimal):
    equivalencias = {
        "f": 15,
        "e": 14,
        "d": 13,
        "c": 12,
        "b": 11,
        "a": 10,
    }
    if caracter_hexadecimal in equivalencias:
        return equivalencias[caracter_hexadecimal]
    else:
        return int(caracter_hexadecimal)


def hexadecimal_a_decimal(hexadecimal):
    # Convertir a minúsculas para hacer las cosas más simples
    hexadecimal = hexadecimal.lower()

    # Comprobamos si el número es negativo
    if hexadecimal[0] == "-":
        negativo = True
        hexadecimal = hexadecimal[1:]

    # La debemos recorrer del final al principio, así que la invertimos
    hexadecimal = hexadecimal[::-1]
    decimal = 0
    posicion = 0

    for digito in hexadecimal:
        # Necesitamos que nos de un 10 para la A, y los dígitos hexadecimales
        valor = obtener_valor_real(digito)
        elevado = 16 ** posicion
        equivalencia = elevado * valor
        decimal += equivalencia
        posicion += 1

    # Si el número ingresado es negativo el número decimal se pasa a negativo
    if negativo:
        decimal = f"-{decimal}"

    return decimal
