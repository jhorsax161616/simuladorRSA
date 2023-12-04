import random
from sympy import mod_inverse


key = "AFOE439&(y"
key2 = "91642ris#x"
key3 = "83rqposgk0"

def encrypt(value: int) -> str:
    value_encypt = ""
    
    for number in str(value):
        value_encypt += key[int(number)] + key2[int(number)] + key3[int(number)]
        
    return value_encypt

def decrypt(value: str) -> int:
    value_key = ""
    for letter in value[::3]:
        value_key += str(key.index(letter))
        
    return int(value_key)

def generar_primo(bits) -> int:
    # Generar un número primo aleatorio de 'bits' bits
    primo = 4  # Inicialización para entrar al bucle
    while not es_primo(primo):
        primo = random.getrandbits(bits)
    return primo

def es_primo(n, k=5) -> bool:
    # Probabilisticamente verifica si un número es primo usando el test de Miller-Rabin
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    # Expresa n - 1 como 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Realiza el test de Miller-Rabin k veces
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generar_clave_privada(p: int, q:int, e:int = 65537) -> tuple:
    N = p * q
    phi_N = (p - 1) * (q - 1)

    # Calcula el exponente de desencriptación 'd'
    d = mod_inverse(e, phi_N)
    # Llave privada
    llave_privada = (N, d)
    
    return llave_privada

def generar_clave_publica(p: int, q:int,  e:int = 65537) -> tuple:
    N = p * q
    # Llave pública
    llave_publica = (N, e)
    
    return llave_publica

def cifrar_mensaje(mensaje: str, llave_publica: tuple) -> str:
    # Desempaquetar la llave pública
    N, e = llave_publica
    
    # Convertir el mensaje a números (por ejemplo, usando codificación ASCII)
    mensaje_numeros = [ord(c) for c in mensaje]

    # Cifrar cada número del mensaje
    mensaje_cifrado = "_".join([str(pow(num, e, N)) for num in mensaje_numeros])

    return mensaje_cifrado

def descifrar_mensaje(mensaje_cifrado: str, llave_privada: tuple) -> str:
    # Desempaquetar la llave privada
    N, d = llave_privada

    #
    mensaje_cifrado = mensaje_cifrado.split("_")
    mensaje_cifrado = [int(i) for i in mensaje_cifrado]
    
    # Descifrar cada número del mensaje cifrado
    mensaje_descifrado_numeros = [pow(num, d, N) for num in mensaje_cifrado]

    # Convertir los números descifrados a caracteres
    mensaje_descifrado = ''.join([chr(num) for num in mensaje_descifrado_numeros])

    return mensaje_descifrado

def llave_a_texto_public(llave: tuple):
    # Convierte una llave publica a un formato de texto plano
    n, e = llave
    texto_plano = f"\t==== LLAVE PUBLICA ====\n{encrypt(n)}\n{encrypt(e)}"
    return texto_plano

def llave_a_texto_private(llave: tuple):
    # Convierte una llave privada a un formato de texto plano
    n, d = llave
    texto_plano = f"\t==== LLAVE PRIVADA ====\n{encrypt(n)}\n{encrypt(d)}"
    return texto_plano

def texto_a_llave(texto_plano: str):
    # Parsea el formato de texto plano y recupera la llave
    lines = texto_plano.split('\n')
    n = int(decrypt(lines[1]))
    exponent = int(decrypt(lines[2]))
    llave = (n, exponent)
    return llave

def es_numero(number: str) -> bool:
    try:
        int(number)
    except:
        return False
    return True
