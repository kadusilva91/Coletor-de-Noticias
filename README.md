# Coletor de Notícias

Um coletor de notícias desenvolvido em Python para extrair títulos e links de notícias de sites populares. O projeto utiliza `requests` para requisições HTTP e `BeautifulSoup` para análise de HTML, demonstrando habilidades em web scraping e automação.

---

## Funcionalidades

- **Coleta de notícias**: Extrai títulos e links de notícias de sites como G1, CNN Brasil e UOL.
- **Requisições HTTP**: Utiliza a biblioteca `requests` para acessar páginas web.
- **Análise de HTML**: Usa `BeautifulSoup` para processar e extrair dados do HTML.
- **Correção de links**: Converte links relativos em absolutos com `urllib.parse.urljoin`.
- **Limitação de resultados**: Exibe apenas os 3 primeiros resultados de cada site.
- **Tratamento de erros**: Exibe mensagens informativas em caso de falhas nas requisições.

---

## Tecnologias Utilizadas

- **Python 3.x**
- Bibliotecas:
  - `requests`: Para requisições HTTP.
  - `beautifulsoup4`: Para análise de HTML.
  - `urllib.parse`: Para manipulação de URLs.

---

## Como Executar

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/coletor-noticias.git
   cd coletor-noticias
