from posixpath import split


def bcd_a_decimal(numero):
    equivalencias = {
        "0000": "0",
        "0001": "1",
        "0010": "2",
        "0011": "3",
        "0100": "4",
        "0101": "5",
        "0110": "6",
        "0111": "7",
        "1000": "8",
        "1001": "9",
    }

    divicion = str(numero).split(" ")
    numero_decimal = ""

    for i in divicion:
        numero_decimal = f"{numero_decimal} {equivalencias[i]}"

    numero_decimal = numero_decimal.translate({ord(' '): None})

    return int(numero_decimal)


def decimal_a_bcd(numero):
    equivalencias = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
    }

    numero_bcd = ""
    numero = str(numero)
    for i in numero:
        numero_bcd = f"{numero_bcd} {equivalencias[i]}"

    return numero_bcd
