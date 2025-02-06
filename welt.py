import requests
import re

url = "https://www.welt.de"
r = requests.get(url)
s = BeautifulSoup(r.text, "html-parser")

