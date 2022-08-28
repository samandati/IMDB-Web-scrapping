import requests
from bs4 import BeautifulSoup


try: 
    source = requests.get(" ")
    source.raise_for_status

    soup = source.Beautifulsoup(text,)

except Exception as e:
    print(e)
