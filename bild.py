from bs4 import BeautifulSoup
import re
import requests
pattern = re.compile(r"https://images\.bild\.de/ | https://hey\.bild\.de | https://www\.fitbook\.de | https://www\.stylebook\.de | https://www\.travelbook\.de | https://www\.bild\.de/video")
url = "https://www.bild.de"
r = requests.get(url)
s = BeautifulSoup(r.text)

for section in s.find_all("section") :
    articles = section.find_all("article", class_=["mini-quad", "quad", "super-a"])
    #print(articles)
    for article in articles :
        #print(article)
        print("-----------------------------------")
        link_unclean = article.find("a", href=True)
        link_clean = link_unclean.get("href")
        print(link_clean)
        text_span = article.find("span", class_="teaser__title__kicker")
        text_span2 = article.find("span", class_="teaser__title__headline")
        if text_span :
            print("TEXT"+text_span.text.strip())
            print("HEADLINE"+text_span2.text.strip())
        else : continue

'''
#for article in s.find_all("article", attrs={"class":"mini-quad", "quad"}):
    #print(article)
    links = article.find_all("a")
    #print(links)
    for link in links:
        text = link.text
        href = link.get("href")
        #print(href)
        if link == [] and not re.search(pattern, link['href']):
            continue
        print("------------------------------------")
        print(link.text)
        print(href)
        #href = link.find_all("a")
        #print(href)
    
'''