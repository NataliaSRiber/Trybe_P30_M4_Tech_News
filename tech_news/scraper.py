import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url, timeout=3):
    """Seu código deve vir aqui"""
    time.sleep(1)
    try:
        response = requests.get(url, timeout=timeout)
    except requests.Timeout:
        return None
    if response.status_code != 200:
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    results = selector.css("h3.tec--card__title a::attr(href)").extract()
    return results


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
