import requests
from bs4 import BeautifulSoup


try: 
    source = requests.get("https://www.imdb.com/chart/top/")
    source.raise_for_status

    soup = BeautifulSoup(source.text,"html.parser")
    print(soup)

except Exception as e:
    print(e)
