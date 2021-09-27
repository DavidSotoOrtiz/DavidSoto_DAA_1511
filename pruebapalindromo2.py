# Ejercicio: Crear una funcion para encontrar el siguiente numero palindromo

# 91, 11 ,1991, 1001

# n = 191, 202
# n = 11, 22
# 
import sys
def siguiente_palindromo(n):

    """
    Encuentra el siguiente numero palindromo
    """
    for i in range(n + 1, sys.maxsize ):
        if str(i) == str(i)[::-1]:
            return i  
if __name__ == "__main__":
    print(siguiente_palindromo(0000))
    print(siguiente_palindromo(11))
    print(siguiente_palindromo(19:91))
    print(siguiente_palindromo(101))
