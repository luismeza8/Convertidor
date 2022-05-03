import Binario
import BCD
import Hexadecimal
import Octal


def solicitar_datos_a_usuario():
    bases_soportadas = ["2", "8", "10", "16", "BCD", "bcd"]
    base_origen = input(
        """
2 - Binario
8 - Octal
10 - Decimal
16 - Hexadecimal
BCD - BCD
Elige la base desde donde conviertes: [2, 8, 10, 16, BCD]: """)

    if base_origen not in bases_soportadas:
        print("La base que ingresaste no está soportada")
        return

    numero = input(
        f"Ok, vas a convertir desde la base {base_origen}. Ingresa el número a convertir: ")

    comprobacion = False

    if base_origen == "2":
        while comprobacion == False:
            for i in numero:
                if i in '10':
                    comprobacion = True
                else:
                    comprobacion = False
                    print("Número binario no valido")
                    numero = input(
                        f"Ok, vas a convertir desde la base {base_origen}. Ingresa el número a convertir: ")

    base_destino = input(
        """
2 - Binario
8 - Octal
10 - Decimal
16 - Hexadecimal
BCD - BCD
Elige la base a la que conviertes: [2, 8, 10, 16, BCD]: """)
    if base_destino not in bases_soportadas:
        print("La base de destino no está soportada")
        return
    return (base_origen, numero, base_destino)


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


if __name__ == '__main__':

    while True:
        datos = solicitar_datos_a_usuario()
        # Comprobamos si los datos son correctos
        if datos:
            base_origen, numero, base_destino = datos
            # Para ahorrarnos código, vamos a convertir el número a decimal (sin importar la base de origen) y luego ese número
            # lo convertimos a la base de destino
            numero_decimal = obtener_numero_decimal(base_origen, numero)
            # Y a ese decimal lo convertimos a la base deseada
            resultado = convertir(numero_decimal, base_destino)
            print(resultado)
