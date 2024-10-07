from collections import Counter
import string

# Mensaje cifrado
#mensaje_cifrado = """RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE. AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE"""
mensaje_cifrado = input("\nIntroduce texto a descifrar en mayusculas ")

# Frecuencia de letras en castellano, de mayor a menor
frecuencia_castellano = "EAOSRNIDLCTUMPBVGQHFYZJXKW"

# Eliminar espacios, numeros y puntuación del mensaje cifrado
mensaje_sin_espacios = ''.join([c for c in mensaje_cifrado if c in string.ascii_uppercase])

# Calcular la frecuencia de las letras en el mensaje cifrado
frecuencia_cifrado = Counter(mensaje_sin_espacios)


# Mostrar las frecuencias del mensaje cifrado
print("Frecuencias en el mensaje cifrado:")
for letra, frecuencia in frecuencia_cifrado.most_common():
    print(f"{letra}: {frecuencia}")

# Ordenar las letras del mensaje cifrado según su frecuencia
letras_cifradas_ordenadas = [letra for letra, _ in frecuencia_cifrado.most_common()]

# Crear un mapeo inicial basado en la frecuencia
mapeo_inicial = {letra_cifrada: letra_castellano for letra_cifrada, letra_castellano in zip(letras_cifradas_ordenadas, frecuencia_castellano)}

# Función para descifrar el mensaje basado en un mapeo de letras
def descifrar(mensaje, mapeo):
    return ''.join([mapeo.get(c, c) for c in mensaje])


# Función para guardar el mensaje descifrado en un archivo
def save_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

# Mostrar el mensaje descifrado con el mapeo inicial
mensaje_descifrado_inicial = descifrar(mensaje_cifrado, mapeo_inicial)
print("\nMensaje descifrado inicialmente:")
print(mensaje_descifrado_inicial)

# Interacción con el usuario para ajustar el descifrado
def ajustar_mapeo(mapeo):
    mensaje_descifrado_ajustado = descifrar(mensaje_cifrado, mapeo)

    while True:
        print("\nMapeo actual de letras:")
        for k, v in mapeo.items():
            print(f"{k} -> {v}")
        
        # Pedir al usuario que ingrese letras para ajustar
        cambiar = input("\n¿Quieres cambiar una letra en el mapeo? (s/n): ").lower()
        if cambiar != 's':
            # Guardar el diccionario en alfabeto_descifrado.txt
            with open("alfabeto_descifrado.txt", "w") as file:
                for k, v in mapeo.items():
                    file.write(f"{k} -> {v}\n")
            print("El mapeo final ha sido guardado en alfabeto_descifrado.txt")
            break
        
        letra_cifrada = input("Ingresa la letra cifrada que quieres cambiar: ").upper()
        nueva_letra = input("Ingresa la nueva letra para mapearla: ").upper()
        
        # Actualizar el mapeo
        if letra_cifrada in mapeo:
            mapeo[letra_cifrada] = nueva_letra
        else:
            print("Letra no encontrada en el mapeo.")
        
        # Mostrar el mensaje con el mapeo ajustado
        mensaje_descifrado_ajustado = descifrar(mensaje_cifrado, mapeo)
        print("\nMensaje inicial:")
        print(mensaje_cifrado)
        print("\nMensaje descifrado con el mapeo ajustado:")
        print(mensaje_descifrado_ajustado)

        
    # Save the final decrypted message to a file
    save_to_file('mensaje_descifrado.txt', mensaje_descifrado_ajustado)
    print("\nEl mensaje descifrado final se ha guardado en 'mensaje_descifrado.txt'.")



# Ejecutar la interacción con el usuario
ajustar_mapeo(mapeo_inicial)

