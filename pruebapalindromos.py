#Ejercicio: Crear una funcion para determinar si una cadena es palíndromo.

def es_palindromo(cadena):
    posicion_izquierda = 0
    posicion_derecha = len(cadena) - 1

    while posicion_derecha >= posicion_izquierda:
        if not cadena[posicion_izquierda] == cadena[posicion_derecha]:
            return False

        posicion_izquierda += 1
        posicion_derecha -= 1

    return True

print(es_palindromo('1221'))
print(es_palindromo('1010'))
print(es_palindromo('1314'))