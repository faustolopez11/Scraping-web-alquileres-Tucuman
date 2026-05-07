import json
import time
from scrapling.fetchers import StealthyFetcher

def scraping_completo_argenprop():
    fetcher = StealthyFetcher()
    base_url = "https://www.argenprop.com/departamentos/alquiler/tucuman-arg"
    todos_los_datos = []
    pagina = 1

    while True:
        url = f"{base_url}?pagina-{pagina}" if pagina > 1 else f"{base_url}"
        print(f"--- Extrayendo Página {pagina} ---")
        
        response = fetcher.fetch(url, solve_cloudflare=True, humanize=True)
        time.sleep(4) # Espera de renderizado crucial en sitios pesados

        if pagina > 1 and f"pagina-{pagina}" not in response.url:
            print(f"Redirección detectada en página {pagina}. Llegamos al final real.")
            break

        # SELECCIÓN DEL CONTENEDOR PADRE
        avisos = response.css('a.card')

        # BUCLE DE VALIDACIÓN: Si no hay avisos, se terminó la web
        if not avisos:
            print(f"No se detectaron más alquileres en la página {pagina}. Fin del proceso.")
            break

        for aviso in avisos:
            # Extracción limpia
            p = aviso.css('.card__price ::text').getall()
            e = aviso.css('.card__expenses::text').get()
            c = aviso.css('.card__main-features ::text').getall()
            
            raw_dir = aviso.css('.card__address::text').get()
            direccion = raw_dir.strip() if raw_dir else ""

            raw_loc = aviso.css('.card__title--primary::text').get()
            localidad = raw_loc.strip() if raw_loc else ""

            raw_desc = aviso.css('.card__title::text').get()
            desc = raw_desc.replace('\xa0', ' ').strip() if raw_desc else ""

            link_relativo = aviso.attrib.get('href') or ""
            link_completo = "https://www.argenprop.com" + link_relativo

            # Formateo de datos para legibilidad
            info_depto = {
                "id_pagina": pagina,
                "precio": "".join([t.strip() for t in p if 'expensas' not in t.lower()]).strip(),
                "expensas": e.replace('+', '').replace('\n', ' ').strip().capitalize() if e else "No indica",
                "caracteristicas": " | ".join([f.replace('\xa0', ' ').strip() for f in c if f.strip()]),
                "direccion_completa": f"{direccion or ''} {localidad or ''}".strip(),
                "resumen": desc.strip().replace('\n', ' ')[:200] if desc else "N/A",
                "link": link_completo
            }
            todos_los_datos.append(info_depto)

        print(f"Éxito: {len(avisos)} departamentos añadidos.")
        pagina += 1
        time.sleep(2) # Respeto al servidor (Anti-ban)

    # GUARDADO FINAL
    with open('alquileres_tucuman_argenprop_total.json', 'w', encoding='utf-8') as f:
        json.dump(todos_los_datos, f, ensure_ascii=False, indent=4)
    
    print(f"--- PROCESO FINALIZADO ---")
    print(f"Total de departamentos scrapeados: {len(todos_los_datos)}")

if __name__ == "__main__":
    scraping_completo_argenprop()