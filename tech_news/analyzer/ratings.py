from tech_news.database import get_collection


# Para esste requisito consultei o repositório de Amós Rodrigues
# Fonte: https://github.com/tryber/sd-013-c-tech-news/pull/17/commits
# /23cd701740860c13d9f7f16c7e33bc47f44fefc0
# Fonte: https://kb.objectrocket.com/mongo-db/project-in-mongodb-what-is-
# project-and-how-to-use-it-in-mongodb-462
# Requisito 10
def top_5_news():
    """Seu código deve vir aqui"""
    news_list = get_collection().aggregate([
        {
            '$project': {
                "title": 1, "url": 1,
                "popularity": {"$add": ["$shares_count", "$comments_count"]}
            }
        },
        {"$sort": {"popularity": -1, "title": 1}}, {"$limit": 5}
    ])
    return [(news["title"], news["url"]) for news in news_list]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
