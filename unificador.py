import json
import re

def limpiar_precio(precio_str):
    numeros = re.findall(r'\d+', precio_str.replace('.', '').replace(',', ''))
    return int(numeros[0]) if numeros else 0

def unificar_datos():
    try:
        with open('alquileres_tucuman_argenprop_total.json', 'r', encoding='utf-8') as f:
            argenprop = json.load(f)
        with open('alquileres_tucuman_ml.json', 'r', encoding='utf-8') as f:
            mercadolibre = json.load(f)
    except FileNotFoundError:
        print("Error: Asegúrate de tener ambos archivos JSON generados.")
        return

    vistos = set()
    unificados = []

    for item in argenprop + mercadolibre:
        # Creamos una "huella digital" del aviso para detectar duplicados
        # Usamos el precio y los primeros 20 caracteres del título/dirección
        precio_num = limpiar_precio(item.get('precio', '0'))
        resumen = (item.get('titulo') or item.get('resumen') or "")[:20].lower().strip()
        
        huella = f"{precio_num}-{resumen}"

        if huella not in vistos:
            item['precio_numerico'] = precio_num # Agregamos el precio limpio para poder ordenar
            unificados.append(item)
            vistos.add(huella)

    # Ordenar por precio de menor a mayor
    unificados.sort(key=lambda x: x['precio_numerico'])

    with open('alquileres_tucuman_CONSOLIDADO.json', 'w', encoding='utf-8') as f:
        json.dump(unificados, f, ensure_ascii=False, indent=4)
    
    print(f"Unificación completa. De {len(argenprop) + len(mercadolibre)} bajamos a {len(unificados)} avisos únicos.")

if __name__ == "__main__":
    unificar_datos()