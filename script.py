import re # regex um links zu filtern
import requests
from tabulate import tabulate
from bs4 import BeautifulSoup
url = "https://www.spiegel.de"
r = requests.get(url)
s = BeautifulSoup(r.text, "html.parser")
pattern = re.compile(r"https://www\.spiegel\.de/tests/")

#Section = abschnitt ie. Bild d. Tages, Themen d. Tages...
for section in s.find_all("section"):
    #if section.find_all("span", attrs={"ANZEIGE"}):
     #   continue
    articles = section.find_all(lambda tag: tag.name == "article" and tag.get("data-target-teaser") in ["m-news","xl-news","xl-opinion-compact","l-news-wide"])
    for article in articles :
        link = article.find("a", href=True)
        #skip tests- artikel
        if link and re.search(pattern, link['href']):
            continue
        print("-----------------------------------------")
        article_text=article.text
        clean_text=re.sub(r"\s+"," ", article_text).strip().replace("Zur Merkliste hinzufügen","")
        link = article.find("a")
        print(clean_text)
        print(link.get("href"))
#article_teaser = s.find_all_next(attrs=="m-news-compact")

pattern = re.compile(r"https://www\.spiegel\.de/tests/")

