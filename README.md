# Web Scraping Tools 🕷️

Este repositorio contiene una colección de scripts desarrollados en Python diseñados para la extracción automatizada de datos (web scraping) desde distintos portales web, con un enfoque en eficiencia y estructuración de datos.

## 🚀 Características
- **Extracción multisitio:** Scripts optimizados para portales de clasificados y marketplace.
- **Salida estructurada:** Generación automática de archivos JSON para facilitar el análisis posterior.
- **Modularidad:** Código organizado en archivos `.py` independientes para cada tarea.

## 🛠️ Requisitos e Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/TU_USUARIO/TU_REPOSITORIO.git](https://github.com/TU_USUARIO/TU_REPOSITORIO.git)
   cd TU_REPOSITORIO
2. **Configurar el entorno (Recomendado):**

   ```bash
   python -m venv venv
   # En Windows:
   .\venv\Scripts\activate
   # En Linux/Mac:
   source venv/bin/activate


3. **Instalar dependencias:**
   Asegúrate de instalar las librerías necesarias (como `requests`, `playwright` o `beautifulsoup4` según tus archivos):
   ```bash
   pip install -r requirements.txt
   
📂 Estructura del Proyecto
*.py: Scripts de lógica principal para el scraping de diferentes sitios.

data/: (Local) Carpeta donde se almacenan los archivos .json generados (excluida del repositorio por privacidad).

🖥️ Uso Local
Para ejecutar cualquiera de los scrapers, simplemente corre el script deseado desde la terminal:

Bash
python nombre_del_archivo.py
⚠️ Aviso Legal (Disclaimer)
Este proyecto tiene fines estrictamente educativos y de investigación. El autor no se hace responsable del uso indebido de estas herramientas. Se recomienda revisar los términos de servicio y el archivo robots.txt de los sitios web antes de ejecutar cualquier script para asegurar el cumplimiento legal.
