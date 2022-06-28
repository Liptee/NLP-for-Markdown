import bs4 as bs
import urllib.request
import re

def extractHeader(string):
    try:
        splitted = string.split()
        res = splitted[0] + " " + splitted[1]
        return res
    except:
        print("Something wrong in extractHeader")
        return False

def wiki_saver(url):
    scrapped_data = urllib.request.urlopen(url)
    article = scrapped_data.read()
    parsed_article = bs.BeautifulSoup(article, 'lxml')
    paragraphs = parsed_article.find_all('p')
    article_text = ""

    for p in paragraphs:
        article_text += p.text

    header = extractHeader(article_text)
    if header:
        path = f'data/{header}.md'

        with open(path, "w", encoding='utf-8') as f:
            f.write(article_text)

while True:
    url = input("Give me URL: ")
    wiki_saver(url)