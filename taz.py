import re # regex um links zu filtern
import requests
from bs4 import BeautifulSoup
url = "https://www.taz.de"
r = requests.get(url)
s = BeautifulSoup(r.text, "html.parser")

#Section = abschnitt ie. Bild d. Tages, Themen d. Tages...
def grepArticles(section):
    links = section.find_all("a", href=True)
    for link in links:
        print(link)
        print("LINK :"+link.text.strip())
        paragraphs = link.find_all("p")
        for paragraph in paragraphs :
            if paragraph :
                print("PARAG :"+paragraph.text)
                print("------------------")
            else :
                continue

        '''
        link = article.find("a", href=True)
        if link and "Ressort" not in article.text:
            if not has_article :
                has_article = True
                continue
            else : 
                print("----------------------------")
                print(link.text)
                '''

for section in s.find_all("section"):
    grepArticles(section)
    '''
    if "Anzeige" in section.text.strip(): 
        continue
    else :
        #print("SECTION :"+section.text)
        grepArticles(section)
        '''
