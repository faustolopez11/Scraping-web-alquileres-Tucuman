import json
import time
from scrapling.fetchers import StealthyFetcher

def scraping_mercadolibre():
    fetcher = StealthyFetcher()
    base_url = "https://inmuebles.mercadolibre.com.ar/departamentos/alquiler/tucuman/"
    todos_los_datos = []
    pagina = 1

    while True:
        # Lógica de URL: Pag 1 es base, Pag 2 es _Desde_49, Pag 3 es _Desde_97...
        if pagina == 1:
            url = base_url
        else:
            desde = (48 * (pagina - 1)) + 1
            url = f"{base_url}_Desde_{desde}_NoIndex_True"
        
        print(f"--- Extrayendo Página {pagina} | URL: {url} ---")
        
        response = fetcher.fetch(url, solve_cloudflare=True)
        time.sleep(5)  # ML es sensible, dale tiempo de respirar

        # Detectar fin de resultados o redirección a página 1
        if pagina > 1 and f"_Desde_{desde}" not in response.url:
            print("Redirección detectada. Fin de los resultados.")
            break

        # Selector de avisos (Grilla o Lista)
        avisos = response.css('.ui-search-layout__item, .ui-search-result__wrapper')

        if not avisos:
            print("No se encontraron más avisos.")
            break

        for aviso in avisos:
            # Extracción de datos
            raw_titulo = aviso.css('h3.poly-component__title-wrapper a::text').get()
            link = aviso.css('h3.poly-component__title-wrapper a::attr(href)').get()
            
            moneda = aviso.css('.andes-money-amount__currency-symbol::text').get()
            monto = aviso.css('.andes-money-amount__fraction::text').get()
            precio = f"{moneda} {monto}" if moneda and monto else "Consultar"
            
            raw_ubica = aviso.css('.poly-component__location::text').get()
            lista_attr = aviso.css('li.poly-attributes_list__item ::text').getall()
            caracteristicas = " | ".join([a.strip() for a in lista_attr if a.strip()])

            # Guardado limpio
            info_depto = {
                "id_pagina": pagina,
                "titulo": raw_titulo.strip() if raw_titulo else "N/A",
                "precio": precio,
                "ubicacion": raw_ubica.strip() if raw_ubica else "N/A",
                "caracteristicas": caracteristicas,
                "link": link
            }
            todos_los_datos.append(info_depto)

        print(f"Éxito: {len(avisos)} avisos procesados.")
        
        # Límite de seguridad para no quedar en bucle infinito (ML suele cortar en pag 40)
        if pagina >= 45: 
            break
            
        pagina += 1
        time.sleep(2)

    # Guardado a JSON
    with open('alquileres_tucuman_ml.json', 'w', encoding='utf-8') as f:
        json.dump(todos_los_datos, f, ensure_ascii=False, indent=4)

    print(f"--- PROCESO FINALIZADO ---")
    print(f"Total capturado: {len(todos_los_datos)} inmuebles.")

if __name__ == "__main__":
    scraping_mercadolibre()