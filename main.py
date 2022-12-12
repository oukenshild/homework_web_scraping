import bs4
import requests

KEYWORDS = ['IT-компании', 'Python', 'Искусственный интеллект', 'Машинное обучение']

HEADERS = {
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Safari/537.36',
    'Cache-Control': 'max-age=0',
    'Referer': 'https://google.com',
    'Pragma': 'no-cache'
}

base_url = 'https://habr.com'
url = base_url + '/ru/all/'

response = requests.get(url, headers=HEADERS)
text = response.text

soup = bs4.BeautifulSoup(text, features="html.parser")

articles = soup.find_all("article")
for article in articles:
    hubs = article.find_all(class_="tm-article-snippet__hubs-item")
    hubs = [hub.text.strip() for hub in hubs]
    for hub in hubs:
        if hub in KEYWORDS:
            date = article.find(class_="tm-article-snippet__datetime-published").find("time").text
            title = article.find("h2").find("span").text
            href = article.find(class_="tm-article-snippet__title-link").attrs["href"]
            link = base_url + href
            print(f"{date} - {title} - {link}")
