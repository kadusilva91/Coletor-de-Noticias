import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Headers para simular um navegador
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Função para coletar notícias de um site
def coletar_noticias(url, seletor_titulo):
    try:
        resposta = requests.get(url, headers=headers)
        resposta.raise_for_status()  # Verifica se a requisição foi bem-sucedida
        soup = BeautifulSoup(resposta.text, 'html.parser')
        noticias = []

        # Pega os títulos e links
        for item in soup.select(seletor_titulo):
            titulo = item.text.strip()
            link = item['href']  # Pega o link diretamente do elemento <a>

            # Corrige links relativos usando urljoin
            link = urljoin(url, link)

            noticias.append((titulo, link))
        return noticias
    except Exception as e:
        print(f"Erro ao acessar {url}: {e}")
        return []

# Lista de sites de notícias
sites = [
    {'url': 'https://g1.globo.com', 'titulo': 'a.feed-post-link'},
    {'url': 'https://www.cnnbrasil.com.br', 'titulo': 'a.home__title-link'},
    {'url': 'https://www.uol.com.br', 'titulo': 'a.hyperlink'}
]

# Coleta e exibe as notícias
for site in sites:
    print(f"\n🔍 Notícias de: {site['url']}")
    noticias = coletar_noticias(site['url'], site['titulo'])

    if noticias:
        for titulo, link in noticias[:3]:  # Limita a 3 notícias por site
            print(f"📌 {titulo} -> {link}")
    else:
        print("Nenhuma notícia encontrada.")
