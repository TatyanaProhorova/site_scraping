from bs4 import BeautifulSoup
# import requests

### Здесь закомментировано получение с сайта, использую локальную копию страницы

# ret = requests.get('https://habr.com/ru/all/')
# ret.raise_for_status()
# soup = BeautifulSoup(ret.text, features='html.parser')


KEYWORDS = {'SQL', 'web', 'python'}
with open("D:/Netology_html_parsing/site_html_text.html", encoding="utf-8") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
articles = soup.find_all('article')
for article in articles:
    article_word_set = set(article.text.split())
    if article_word_set & KEYWORDS:
        article_title = article.find("h2")
        article_name = article_title.find("span").text
        link = "https://habr.com" + article_title.find("a").attrs.get('href')
        publishing_time = article.find("time").attrs.get("title")
        print(publishing_time, " -", article_name, " -", link)


