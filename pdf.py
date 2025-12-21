from pypdf import PdfWriter
import os

def fusionar_pdfs(archivos_pdf, nombre_salida):
    """
    Combina (merge) múltiples archivos PDF en uno solo.

    :param archivos_pdf: Una lista de cadenas, donde cada cadena es la ruta a un archivo PDF.
    :param nombre_salida: Una cadena con el nombre/ruta del archivo PDF resultante.
    """
    # Inicializar el objeto PdfWriter que construirá el nuevo PDF
    combinador = PdfWriter()

    print(f"Iniciando la fusión de {len(archivos_pdf)} archivos...")

    try:
        # Iterar sobre la lista de archivos de entrada
        for ruta_pdf in archivos_pdf:
            # Asegúrate de que el archivo exista antes de intentar agregarlo
            if not os.path.exists(ruta_pdf):
                print(f"⚠️ Advertencia: Archivo no encontrado - {ruta_pdf}. Saltando.")
                continue

            # Agregar el PDF actual al combinador
            print(f"  -> Agregando: {os.path.basename(ruta_pdf)}")
            combinador.append(ruta_pdf)

        # Escribir el PDF combinado en el archivo de salida
        with open(nombre_salida, "wb") as salida:
            combinador.write(salida)

        print(f"\n✅ Fusión completada exitosamente. Archivo guardado como: {nombre_salida}")

    except Exception as e:
        print(f"\n❌ Ocurrió un error durante la fusión: {e}")

# --- Ejemplo de Uso ---

# 1. Define la lista de archivos PDF que deseas fusionar
#    Asegúrate de que estas rutas sean correctas en tu sistema.
#    El orden en la lista es el orden en que aparecerán en el PDF final.
archivos_a_fusionar = [
    "C:\\Users\\anita\\Downloads\\bigo.pdf",
    "C:\\Users\\anita\\Downloads\\bd.pdf",
    "C:\\Users\\anita\\Downloads\\oop.pdf"
    
]

# 2. Define el nombre del archivo de salida
pdf_final = "documento_fusionado.pdf"

# 3. Llamar a la función
# NOTA: Para que este script funcione, debes asegurarte de que los 
# archivos 'documento1.pdf', 'capitulo_2.pdf', y 'anexo.pdf' existan en
# el mismo directorio que este script, o proporcionar las rutas completas.
fusionar_pdfs(archivos_a_fusionar, pdf_final)