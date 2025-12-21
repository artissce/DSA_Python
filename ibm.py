def minSegments(s):
    # Función auxiliar: Cuenta segmentos ignorando una letra prohibida
    def count_with_skip(skip_char):
        segments = 0
        seen = set()
        
        for char in s:
            if char == skip_char: continue
            
            # Lógica Greedy: Si se repite, cerramos segmento y empezamos uno nuevo
            if char in seen:
                segments += 1
                seen = {char} # Nuevo set con el char actual
            else:
                seen.add(char)
                # Si es el primer caracter del segmento (y no se repitió), asegúrate de contar el segmento actual si no estaba contado
                if len(seen) == 1 and segments == 0: # Caso borde inicio
                     segments = 1
                elif len(seen) == 1: # Caso inicio de nuevo segmento post-corte
                     pass # Ya sumamos el segmento arriba al cortar

        # Corrección elegante: Si el set no quedó vacío al final, ese último segmento cuenta
        # Pero mi lógica de arriba cuenta "cortes". Vamos a simplificarlo más.
        return segments + 1 if seen else 0

    # Versión SUPER Simplificada de la lógica Greedy:
    def solve_greedy(skip_char):
        count = 1
        seen = set()
        has_chars = False
        for char in s:
            if char == skip_char: continue
            has_chars = True
            if char in seen:
                count += 1
                seen = {char}
            else:
                seen.add(char)
        return count if has_chars else 0

    # LA ELEGANCIA: Una sola línea para probar todas las opciones
    # Probamos eliminar solo las letras que existen en 's'
    return min(solve_greedy(char) for char in set(s))