# def comprobar_numero(valor):
#     if "0" not in valor or "1" not in valor:
#         return True

#     return False

# def separar_numero(valor, )

import Conversiones

equivalencias = {
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


def bcd_a_decimal(numero):
    pass


def decimal_a_bcd(numero):
    numero = str(numero)

    for i in numero:
        numero_bcd = f"{numero_bcd} {equivalencias[i]}"

    return numero_bcd
