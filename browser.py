
import requests
from bs4 import BeautifulSoup, NavigableString

def fetch_and_parse(url):
    # 1. Fazer o request
    resp = requests.get(url)
    resp.raise_for_status()

    # 2. Carregar no BeautifulSoup
    soup = BeautifulSoup(resp.text, "html.parser")

    # 3. Função recursiva para processar os nós
    def process_node(node):
        if isinstance(node, NavigableString):
            # Texto simples
            text = node.strip()
            if text:
                print(text, end=" ")
        elif node.name == "img":
            src = node.get("src")
            if src:
                print(f"[IMG: {src}]")
        elif node.name == "a":
            href = node.get("href")
            if href:
                print(f"[LINK: {href}]")
        elif node.name in ["p", "br"]:
            print("\r\n")
        else:
            # processar filhos
            for child in node.children:
                process_node(child)

    # 4. Percorrer todo o documento
    for child in soup.body.descendants if soup.body else soup.descendants:
        process_node(child)

# Exemplo:
print("\033c\033[43;30m\ngive me the url?")
i=input()
fetch_and_parse(i)
