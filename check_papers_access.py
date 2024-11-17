import requests
import pandas as pd
import time
import re

# Configura tu correo para las solicitudes
email = "TuCorreo@ejemplo.com"  # Reemplaza con tu correo
headers = {
    "User-Agent": email
}

# Archivos de entrada y salida
input_file = "papers_list.csv"  # Archivo con las columnas N, doi
output_file = "papers_accessibility_result.csv"

# Función para validar DOI
def is_valid_doi(doi):
    if pd.isna(doi) or doi.strip() == "":
        return False
    pattern = r'^10.\d{4,9}/[-._;()/:A-Z0-9]+$'
    return bool(re.match(pattern, doi, re.IGNORECASE))

def check_papers_accessibility(input_file, output_file):
    try:
        # Cargar el archivo con manejo de errores
        df = pd.read_csv(input_file, delimiter=',', on_bad_lines='skip')  # Asegúrate del delimitador

        if 'doi' not in df.columns:
            raise ValueError("El archivo de entrada debe tener la columna 'doi'.")

        # Crear una lista para almacenar resultados
        results_list = []

        # Procesar cada fila
        for index, row in df.iterrows():
            paper_id = row.get('N', index + 1)  # Usar índice como id si 'N' no está presente
            doi = row.get('doi', None)

            # Saltar líneas sin DOI válido
            if not is_valid_doi(doi):
                print(f"Saltando línea {index + 1}: DOI no válido o no proporcionado")
                continue

            # Consultar el DOI en la API de Unpaywall
            url = f"https://api.unpaywall.org/v2/{doi}?email={email}"
            try:
                response = requests.get(url, headers=headers)
                if response.status_code == 200:
                    data = response.json()
                    access_status = "Gratuito" if data.get('is_oa', False) else "No gratuito"
                else:
                    access_status = "Error en la API"
            except Exception as e:
                access_status = "Error en la solicitud"
                print(f"Error con DOI {doi}: {e}")

            # Agregar un retraso para evitar problemas con la API
            time.sleep(0.2)  # 200 ms entre solicitudes

            # Añadir los resultados a la lista
            results_list.append({
                'id': paper_id,
                'doi': doi,
                'acceso': access_status
            })

        # Convertir la lista de resultados en un DataFrame
        results = pd.DataFrame(results_list)

        # Guardar los resultados en un archivo CSV
        results.to_csv(output_file, index=False)
        print(f"Archivo con resultados guardado: {output_file}")
    except Exception as e:
        print(f"Error procesando el archivo: {e}")

# Ejecutar el script
check_papers_accessibility(input_file, output_file)
