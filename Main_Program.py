import Binario
import BCD
import Hexadecimal
import Octal
import IEEE


def solicitar_datos_a_usuario():
    bases_soportadas = ["2", "8", "10", "16", "BCD", "bcd", "0.1", "todos"]

    base_origen = input(
        """
2 - Binario
8 - Octal
10 - Decimal
16 - Hexadecimal
BCD - BCD
0.1 - IEEE
Elige la base desde donde conviertes: [2, 8, 10, 16, BCD, 0.1]: """)

    if base_origen not in bases_soportadas:
        print("La base que ingresaste no está soportada")
        return

    numero = comprobacion(base_origen)

    base_destino = input(
        """
2 - Binario
8 - Octal
10 - Decimal
16 - Hexadecimal
BCD - BCD
0.1 - IEEE
Elige la base a la que conviertes: [2, 8, 10, 16, BCD, 0.1, todos]: """)

    if base_destino not in bases_soportadas:
        print("La base de destino no está soportada")
        return

    return (base_origen, numero, base_destino)


def comprobacion(base_origen):

    if base_origen == "bcd" or base_origen == "BCD":
        numero = input(
            f"""\nOk, vas a convertir desde la base {base_origen}.
            \nTienes que separar cada 4 digitos con un espacion. Ejemplo 0010 1001 0110.
Ingresa el número a convertir: """)
    else:
        numero = input(
            f"\nOk, vas a convertir desde la base {base_origen}. Ingresa el número a convertir: ")

    comprobacion = False

    if base_origen == "2":
        while comprobacion == False:
            for i in numero:
                if i in '10-':
                    comprobacion = True
                else:
                    comprobacion = False
                    print("Número Binario no valido")
                    numero = input(
                        f"Ok, vas a convertir desde la base {base_origen}. Ingresa el número a convertir: ")

    elif base_origen == "8":
        while comprobacion == False:
            for i in numero:
                if i in '1234567-':
                    comprobacion = True
                else:
                    comprobacion = False
                    print("Número Octal no valido")
                    numero = input(
                        f"Ok, vas a convertir desde la base {base_origen}. Ingresa el número a convertir: ")

    elif base_origen == "10":
        while comprobacion == False:
            for i in numero:
                if i in '1234567890-':
                    comprobacion = True
                else:
                    comprobacion = False
                    print("Número Decimal no valido")
                    numero = input(
                        f"Ok, vas a convertir desde la base {base_origen}. Ingresa el número a convertir: ")

    elif base_origen == "16":
        while comprobacion == False:
            for i in numero:
                if i in '123456789abcdef-':
                    comprobacion = True
                else:
                    comprobacion = False
                    print("Número Hexadecimal no valido")
                    numero = input(
                        f"Ok, vas a convertir desde la base {base_origen}. Ingresa el número a convertir: ")

    elif base_origen == "BCD" or base_origen == "bcd":
        while comprobacion == False:
            for i in numero:
                if i in '10-':
                    comprobacion = True
                else:
                    comprobacion = False
                    print("Número BCD no valido")
                    numero = input(
                        f"Ok, vas a convertir desde la base {base_origen}. Ingresa el número a convertir: ")

    elif base_origen == "IEEE" or base_origen == "0.1":
        while comprobacion == False:
            for i in numero:
                if i in '10-':
                    comprobacion = True
                else:
                    comprobacion = False
                    print("Número IEEE no valido")
                    numero = input(
                        f"Ok, vas a convertir desde la base {base_origen}. Ingresa el número a convertir: ")

    return numero


def obtener_numero_decimal(base_origen, numero):
    if base_origen == "2":
        return Binario.binario_a_decimal(numero)
    elif base_origen == "8":
        return Octal.octal_a_decimal(numero)
    elif base_origen == "10":
        return int(numero)
    elif base_origen == "16":
        return Hexadecimal.hexadecimal_a_decimal(numero)
    elif base_origen == "BCD" or base_origen == "bcd":
        return BCD.bcd_a_decimal(numero)


def convertir(numero, base_destino):
    if base_destino == "2":
        return Binario.decimal_a_binario(numero)
    elif base_destino == "8":
        return Octal.decimal_a_octal(numero)
    elif base_destino == "10":
        return int(numero)
    elif base_destino == "16":
        return Hexadecimal.decimal_a_hexadecimal(numero)
    elif base_destino == "BCD" or base_destino == "bcd":
        return BCD.decimal_a_bcd(numero)
    elif base_destino == "0.1":
        return IEEE.decimal_a_ieee(numero)
    elif base_destino == "todos":
        return f"Binario: {Binario.decimal_a_binario(numero)} \nOctal: {Octal.decimal_a_octal(numero)} \nHexadecimal: {Hexadecimal.decimal_a_hexadecimal(numero)} \nBCD: {BCD.decimal_a_bcd(numero)} \nIEEE: {IEEE.decimal_a_ieee(numero)}"


if __name__ == '__main__':

    while True:
        datos = solicitar_datos_a_usuario()
        # Comprobamos si los datos son correctos
        if datos:
            base_origen, numero, base_destino = datos
            # Para ahorrarnos código, vamos a convertir el número a decimal (sin importar la base de origen)
            # y luego ese número lo convertimos a la base de destino
            numero_decimal = obtener_numero_decimal(base_origen, numero)

            # Y a ese decimal lo convertimos a la base deseada
            resultado = convertir(numero_decimal, base_destino)
            print(f"\n{resultado}")
