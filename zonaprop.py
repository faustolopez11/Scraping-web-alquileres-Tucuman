import json
import time
from scrapling.fetchers import StealthyFetcher

def scraping_completo_zonaprop():
    fetcher = StealthyFetcher()
    base_url = "https://www.zonaprop.com.ar/departamentos-alquiler-tucuman"
    todos_los_datos = []
    pagina = 1

    while True:
        # Construimos la URL dinámicamente
        url = f"{base_url}-pagina-{pagina}.html" if pagina > 1 else f"{base_url}.html"
        print(f"--- Extrayendo Página {pagina} ---")
        
        response = fetcher.fetch(url, solve_cloudflare=True, humanize=True)
        time.sleep(4) # Espera de renderizado crucial en sitios pesados

        # NUEVA VALIDACIÓN: Si la URL real donde terminamos no contiene el número de página que pedimos
        # significa que nos redireccionaron a la última página válida.
        if pagina > 1 and f"pagina-{pagina}" not in response.url:
            print(f"Redirección detectada en página {pagina}. Llegamos al final real.")
            break

        # SELECCIÓN DEL CONTENEDOR PADRE
        avisos = response.css('.postingCard-module__posting-container')

        # BUCLE DE VALIDACIÓN: Si no hay avisos, se terminó la web
        if not avisos:
            print(f"No se detectaron más alquileres en la página {pagina}. Fin del proceso.")
            break

        for aviso in avisos:
            # Extracción limpia
            p = aviso.css('.postingPrices-module__price::text').get()
            e = aviso.css('.postingPrices-module__expenses::text').get()
            f = aviso.css('[data-qa="POSTING_CARD_FEATURES"] ::text').getall()
            dir_text = aviso.css('.postingLocations-module__location-address::text').get()
            loc_text = aviso.css('[data-qa="POSTING_CARD_LOCATION"] ::text').get()
            desc = aviso.css('[data-qa="POSTING_CARD_DESCRIPTION"] ::text').get()

            # Formateo de datos para legibilidad
            info_depto = {
                "id_pagina": pagina,
                "precio": p.strip() if p else "N/A",
                "expensas": e.strip() if e else "Incluidas/No indica",
                "caracteristicas": " | ".join([item.strip() for item in f if item.strip()]),
                "direccion_completa": f"{dir_text or ''} {loc_text or ''}".strip(),
                "resumen": desc.strip().replace('\n', ' ')[:200] if desc else "N/A",
                "link": "https://www.zonaprop.com.ar" + (aviso.css('a::attr(href)').get() or "")
            }
            todos_los_datos.append(info_depto)

        print(f"Éxito: {len(avisos)} departamentos añadidos.")
        pagina += 1
        time.sleep(2) # Respeto al servidor (Anti-ban)

    # GUARDADO FINAL
    with open('alquileres_tucuman_total.json', 'w', encoding='utf-8') as f:
        json.dump(todos_los_datos, f, ensure_ascii=False, indent=4)
    
    print(f"--- PROCESO FINALIZADO ---")
    print(f"Total de departamentos scrapeados: {len(todos_los_datos)}")

if __name__ == "__main__":
    scraping_completo_zonaprop()