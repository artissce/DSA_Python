# Representación del sistema de archivos (Grafo Dirigido)
sistema_archivos = {
    "Documentos": ["Fotos", "Lista.txt","Trabajo"],
    "Fotos": ["2023", "2024"],
    "Trabajo": ["ProyectoX", "Finanzas"],
    "ProyectoX": ["passwords.txt"], # <--- ¡AQUÍ ESTÁ EL TESORO!
    "Finanzas": [],
    "2023": [],
    "2024": [],
    "Lista.txt": [] # Es un archivo, no tiene hijos
}

def dfs_buscar_archivo(carpeta_actual, archivo_buscado, camino_recorrido):
    # --- PARTE 1: CASO BASE (El Freno) ---
    print(f"🔎 Explorando: {carpeta_actual}")
    
    # 1. ¿Encontré lo que buscaba?
    if carpeta_actual == archivo_buscado:
        print(f"¡ENCONTRADO! Ruta: {camino_recorrido}")
        return True
    
    # 2. ¿Es una carpeta vacía o un archivo sin hijos? (Caso borde)
    if carpeta_actual not in sistema_archivos:
        return False

    # --- PARTE 2: RECURSIÓN (Ir Profundo) ---
    # Reviso cada cosa que hay dentro de esta carpeta
    for contenido in sistema_archivos[carpeta_actual]:
        # Llamo a la función de nuevo (inception)
        encontrado = dfs_buscar_archivo(contenido, archivo_buscado, camino_recorrido + " -> " + contenido)
        
        # Si la llamada de adentro me dice "Lo encontré", yo también retorno True
        if encontrado:
            return True
            
    return False

# --- Ejecución ---
dfs_buscar_archivo("Documentos", "passwords.txt", "Documentos")

#template
grafo = {
    "A": ["B", "C"],  # Los vecinos de A son B y C
    "B": ["D"],
    "C": [],
    "D": []
}

def dfs(nodo, visitados):
    # 1. ¿Ya vine aquí? (Caso Base de Protección)
    if nodo in visitados:
        return
    
    # 2. Marcar como visto
    visitados.add(nodo)
    
    # 3. Procesar el nodo (Aquí va tu lógica: imprimir, sumar, checar si es lo que buscas)
    print(nodo) 
    
    # 4. Ir con los vecinos (Recursión)
    for vecino in grafo(nodo):
        dfs(vecino, visitados)

def pre_order(nodo):
    if not nodo: return
    print(nodo.val)    # 1. Proceso el nodo (Yo)
    pre_order(nodo.left)  # 2. Izquierda
    pre_order(nodo.right) # 3. Derecha

def in_order(nodo):
    if not nodo: return
    in_order(nodo.left)   # 1. Izquierda
    print(nodo.val)    # 2. Proceso el nodo (Yo)
    in_order(nodo.right)  # 3. Derecha

def post_order(nodo):
    if not nodo: return
    post_order(nodo.left) # 1. Izquierda
    post_order(nodo.right)# 2. Derecha
    print(nodo.val)    # 3. Proceso el nodo (Yo)