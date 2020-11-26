def scrapeo(url, players, prices):
    header = {"User-Agent": "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
    """"
    Mapeo de la página para ello se crea priero el 
    árbol de la página usando los headers originales del navegador
    """
    webTree = requests.get(url, headers=header)
    webSoup = BeautifulSoup(webTree.content, 'html.parser')

    """"
    A continuación encontrará en cada una de las etiquetas tr del sourcecode 
    las que coincidan con los parámetros que usamos como filtro en este caso
    los jugadores tienen asociado un atributo llamado athlete
    ocurre lo mismo para encontrar el precio del jugador en el que hay dos
    clases asociadas a los jugadores una que se llama rechts y otra llamada
    hauptlink
    """
    player = webSoup.find_all("td", {"itemprop": "athlete"})
    price = webSoup.find_all("td", {"class": "rechts hauptlink"})

    # Cuando la función ha encontrado los objetos que buscamos los añade a la lista de jugadores
    for ply in player:
        players.append(ply.text)
    for prc in price:
        prices.append(prc.text)

    print(players)
    print(prices)


import requests
from bs4 import BeautifulSoup
import pandas as pd

# Diccionario con cada una de las URLs de los equipos de la liga
urlTeamsLaliga = {
    0: "atletico-madrid/startseite/verein/13/saison_id/2020",
    1: "fc-barcelona/startseite/verein/131/saison_id/2020",
    2: "real-madrid/startseite/verein/418/saison_id/2020",
    3: "fc-sevilla/startseite/verein/368/saison_id/2020",
    4: "real-sociedad-san-sebastian/startseite/verein/681/saison_id/2020",
    5: "fc-villarreal/startseite/verein/1050/saison_id/2020",
    6: "fc-valencia/startseite/verein/1049/saison_id/2020",
    7: "athletic-bilbao/startseite/verein/621/saison_id/2020",
    8: "real-betis-sevilla/startseite/verein/150/saison_id/2020",
    9: "fc-getafe/startseite/verein/3709/saison_id/2020",
    10: "fc-granada/startseite/verein/16795/saison_id/2020",
    11: "celta-vigo/startseite/verein/940/saison_id/2020",
    12: "ud-levante/startseite/verein/3368/saison_id/2020",
    13: "deportivo-alaves/startseite/verein/1108/saison_id/2020",
    14: "ca-osasuna/startseite/verein/331/saison_id/2020",
    15: "sd-eibar/startseite/verein/1533/saison_id/2020",
    16: "real-valladolid/startseite/verein/366/saison_id/2020",
    17: "sd-huesca/startseite/verein/5358/saison_id/2020",
    18: "cadiz-cf/startseite/verein/2687/saison_id/2020",
    19: "fc-elche/startseite/verein/1531/saison_id/2020"
}

urlTransfermark = "https://www.transfermarkt.es/"
players = list()
prices = list()

# Bucle que nos automatizará el scraping de los jugadores de cada equipo
for value in urlTeamsLaliga.values():
    scrapeo(urlTransfermark + value, players, prices)