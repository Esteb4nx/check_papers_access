# **Verificación de Accesibilidad de Artículos Científicos**

Este software permite verificar automáticamente si los artículos científicos, identificados por sus DOIs, son accesibles de forma gratuita utilizando la API de Unpaywall. Está diseñado para procesar archivos CSV con una lista de DOIs y generar un reporte con el estado de accesibilidad de cada artículo.

## **Características**
- Verifica si un artículo es accesible gratuitamente o no.
- Maneja errores en los DOIs y omite líneas inválidas automáticamente.
- Genera un archivo CSV de salida con los resultados.
- Compatible con Python 3.8+ y `pandas` 1.4+.

---

## **Requisitos**
### **1. Software**
- **Python 3.8 o superior**
- Librerías de Python:
  - `pandas`
  - `requests`

### **2. Archivo de entrada**
Un archivo CSV llamado `papers_list.csv` con las siguientes columnas:
- `N`: Un identificador único para cada artículo.
- `doi`: El DOI del artículo científico.

Ejemplo de archivo de entrada:

```csv
N,doi
1,10.1145/3341525.3394002
2,10.1145/3422392.3422506
3,10.1145/3606094.3606463
4,10.1145/3675669.3675674
5,10.1145/3625704.3625753
```

### **3. Conexión a Internet**
El script utiliza la API de Unpaywall para consultar el estado de accesibilidad de los artículos, por lo que es necesario estar conectado a Internet.

---

## **Instalación**
### **1. Clonar el repositorio**
Clona este repositorio en tu máquina local:
```bash
git clone https://github.com/Esteb4nx/check_papers_access.git
cd check_papers_access
```

### **2. Instalar dependencias**
Instala las dependencias requeridas:
```bash
pip install pandas requests
```

### **3. Configurar el correo para la API**
Edita el archivo `check_papers_access.py` y reemplaza `TuCorreo@ejemplo.com` con tu correo electrónico. Esto es necesario para acceder a la API de Unpaywall.

---

## **Uso**
1. **Preparar el archivo de entrada**
   Crea un archivo CSV llamado `papers_list.csv` con las columnas `N` y `doi`, siguiendo el formato indicado en los requisitos.

2. **Ejecutar el script**
   Ejecuta el script en la terminal:
   ```bash
   python check_papers_access.py
   ```

3. **Revisar el archivo de salida**
   Una vez que el script termine, se generará un archivo llamado `papers_accessibility_result.csv` en la misma carpeta. Este archivo contendrá las siguientes columnas:
   - `id`: Identificador único del artículo.
   - `doi`: DOI del artículo.
   - `acceso`: Estado de accesibilidad (`Gratuito`, `No gratuito`, `Error en la API`, etc.).

Ejemplo de salida:
```csv
id,doi,acceso
1,10.1145/3341525.3394002,Gratuito
2,10.1145/3422392.3422506,No gratuito
3,10.1145/3606094.3606463,Gratuito
```

---

## **Detalles técnicos**
### **Validación de DOIs**
- Se valida que el DOI esté en el formato correcto utilizando expresiones regulares.
- Si un DOI es inválido o no está presente, la línea correspondiente se omite del procesamiento.

### **Interacción con la API de Unpaywall**
- El script consulta la API de Unpaywall para determinar si un artículo es accesible gratuitamente.
- Se respetan límites de solicitudes con un retraso de 200 ms entre cada consulta.

### **Manejo de errores**
- El script ignora automáticamente líneas con datos mal formados.
- Si ocurre un error al consultar la API, se registra en el archivo de salida.

---

## **Posibles errores y soluciones**
### **1. Error: "Error tokenizing data"**
Esto ocurre si el archivo CSV tiene más o menos columnas de las esperadas. Asegúrate de que el archivo tenga solo las columnas `N` y `doi` correctamente formateadas.

### **2. Error: "No module named 'pandas' o 'requests'"**
Esto significa que no has instalado las librerías necesarias. Instálalas con:
```bash
pip install pandas requests
```

### **3. API no responde**
Verifica tu conexión a Internet y asegúrate de que el correo configurado es válido.

---

## **Contribuciones**
Si deseas contribuir a este proyecto, puedes hacerlo mediante un pull request o contactando al autor directamente.

---

## **Licencia**
Este proyecto está bajo la licencia MIT. Puedes usarlo libremente, pero sin garantías de funcionamiento.

---
