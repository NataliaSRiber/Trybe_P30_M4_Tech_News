from tech_news.database import search_news
import datetime


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    news_list = search_news({"title": {"$regex": title, "$options": "i"}})
    return [(news["title"], news["url"]) for news in news_list]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        datetime.date.fromisoformat(date)
        per_date_list = search_news({"timestamp": {"$regex": date}})
        return [(news["title"], news["url"]) for news in per_date_list]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""
    news_list = search_news({"sources": {"$regex": source, "$options": "i"}})
    return [(news["title"], news["url"]) for news in news_list]

# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
