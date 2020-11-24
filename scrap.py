import requests
from bs4 import BeautifulSoup

import pandas as pd

# headers = {'User-Agent':
#   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}


"""#Scrapeo equipos la liga


page = "https://www.transfermarkt.es/primera-division/startseite/wettbewerb/ES1"
pageTree = requests.get(page, headers=headers)
pageSoup = BeautifulSoup(pageTree.content, 'html.parser')
equipo = pageSoup.find_all("a", {"class": "vereinprofil_tooltip"})

equipos=list()

for i in equipo:
    equipos.append(i.text)



print(equipos)
"""
"""
#Scrapeo jugadores Barsa + valor

page = "https://www.transfermarkt.es/fc-barcelona/startseite/verein/131"
pageTree = requests.get(page, headers=headers)
pageSoup = BeautifulSoup(pageTree.content, 'html.parser')
player = pageSoup.find_all("td", {"itemprop": "athlete"})
values = pageSoup.find_all("td", {"class": "rechts hauptlink"})

jugadores=list()
valores=list()

for i in player:
    jugadores.append(i.text)

for i in values:
    valores.append(i.text)



print(jugadores)
print(valores)

"""

headers = {'User-Agent':
               'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

page = "https://www.transfermarkt.es/fc-barcelona/startseite/verein/131"
pageTree = requests.get(page, headers=headers)
pageSoup = BeautifulSoup(pageTree.content, 'html.parser')
player = pageSoup.find_all("td", {"itemprop": "athlete"})
values = pageSoup.find_all("td", {"class": "rechts hauptlink"})
dorsal = pageSoup.find_all("div", {"class": "rn_nummer"})
posicion = pageSoup.find_all("table", {"class": "inline-table"})

pageSoup.find
PlayersList = []
ValuesList = []
DorsalList = []
PosicionList = []

for i in range(0, 27):
    PlayersList.append(player[i].text)
    ValuesList.append(values[i].text)
    DorsalList.append(dorsal[i].text)
    PosicionList.append(posicion[i].text)


d = ({"Players": PlayersList, "Dorsal": DorsalList, "Values": ValuesList})

df = pd.DataFrame(data=d)
print(df)
