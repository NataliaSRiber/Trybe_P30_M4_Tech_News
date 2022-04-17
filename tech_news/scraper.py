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
    selector = Selector(html_content)
    get_links = selector.css("div.tec--list__item ~ a::attr(href)").get()
    return get_links


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    url = selector.css("link[rel='canonical']::attr(href)").get()
    title = selector.css("#js-article-title::text").get()
    timestamp = selector.css("#js-article-date::attr(datetime)").get()
    writer = selector.css(".z--font-bold *::text").get().strip()
    comments_count = selector.css("#js-comments-btn::attr(data-count)").get()
    comments_count = 0 if comments_count is None else int(comments_count)
    shares_count = selector.css(
        "div.tec--toolbar__item::text"
    ).re_first(r"[0-9][0-9]")
    shares_count = 0 if shares_count is None else shares_count
    summary = "".join(selector.css(
        "div.tec--article__body p:first-child *::text").getall())
    sources = [
        source[1:-1]
        for source in selector.css("div.z--mb-16 a::text").getall()
    ]
    categories = [
        category[1:-1]
        for category in selector.css("#js-categories a::text").getall()
    ]
    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }


# scrape_noticia(fetch(url1))


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
