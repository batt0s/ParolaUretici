import requests
from bs4 import BeautifulSoup

URL = "https://evrimagaci.org/sozler/rastgele"

def get_quote():
    r = requests.get(URL)
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find("a", class_="quote")
    quote = a.contents[0]
    return quote
