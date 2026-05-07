from scrapling.fetchers import Fetcher

page = Fetcher.get('https://quotes.toscrape.com/', impersonate="chrome")

titulo = page.css('h1 a::text').get()

print("-" * 30)
print(f"¡Éxito total! El título es: {titulo}")
print("-" * 30)