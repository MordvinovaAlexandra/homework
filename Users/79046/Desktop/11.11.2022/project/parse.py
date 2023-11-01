import httpx
from bs4 import BeautifulSoup

def clean(text: str) -> str: 
    return text.replace("\n", " ").replace("\t", " ").replace("\r", " ").strip()

def get_html(url) -> str:
    response = httpx.get(url)
    html = response.text
    return html


def parse(url):
    html = get_html(url)
    parser = BeautifulSoup(html, features="html.parser")
    return parser
