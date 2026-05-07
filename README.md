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

**Estructura y Uso**
   ```markdown
## 📂 Estructura del Proyecto
- `*.py`: Scripts de scraping independientes.
- `*.json`: (Excluidos mediante .gitignore) Archivos de datos generados localmente.
- `.gitignore`: Configuración para evitar subir datos sensibles o archivos basura de Python.

## 🖥️ Uso
Para ejecutar los scrapers, asegúrate de estar en la raíz del proyecto y corre:
```bash
python nombre_de_tu_script.py
