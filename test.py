from collections import Counter

#1. Two Sum (fácil)
#Dado un arreglo y un número objetivo, regresa los índices de los dos números que suman ese objetivo.

#2. Invertir palabras en una frase

#"hola mundo este es un test" → "test un es este mundo hola".

frase = input('Escriba una palabra: ')

frase_invertida = ''

for i in range(len(frase) - 1, -1, -1):
    frase_invertida += frase[i]

print('Frase invertida',frase_invertida)

#3. Primer carácter no repetido

#Usa un diccionario (hash map) para contar.

# Analisis

def primer_caracterer_no_repetido(cadena):
    conteo = {}

    for c in cadena:
        # get -> si no esta, ponla en cero y + 1, 
        # si esta, agregale + 1 
        # conteo[c] = conteo.get(c, 0) + 1
        if c in conteo:
            conteo[c] += 1 # no es la primera vez que se encuentra
        else:
            conteo[c] = 1 # es la primera vez que se agrega
    for c in conteo.keys():
        if conteo[c] == 1:
            return c

def primer_caracter_no_repetido2(cadena):
    # Paso 1: Crear el Hash Map de frecuencias automáticamente
    # Esto es O(N)
    conteo = Counter(cadena)

    for c in conteo:
        if conteo[c] == 1:
            return c
    
    return None
        
texto = 'Python es tremendo'

print(primer_caracterer_no_repetido(texto))


#4. Validar paréntesis

#"(){}[]" bien formado. Usa una pila (stack).

