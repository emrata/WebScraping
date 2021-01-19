import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3


def pasarADB(equipo, players, price, dorsales, paises, edades, posiciones):
    conn = sqlite3.connect('equipos.db')
    c = conn.cursor()
    # c.execute('''CREATE TABLE infoJugador(jugador TEXT, edad INT, pais TEXT, equipos TEXT, dorsal INT, posicion TEXT, precio FLOAT)''')

    i = 0
    while i < len(players):
        c.execute('''INSERT INTO infoJugador VALUES(?, ?, ?, ?, ?, ?, ?)''',
                  (players[i], edades[i], paises[i], equipo[i], dorsales[i], posiciones[i], price[i]))
        i = i + 1
    print("Información migrada a la DB")
    c.close()


def scrapeo(url, players, prices, dorsales, paises, edades, posiciones):
    header = {"User-Agent": "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
    """"
    Mapeo de la página para ello se crea priero el 
    árbol de la página usando los headers originales del navegador
    """
    pageTree = requests.get(url, headers=header)
    pageSoup = BeautifulSoup(pageTree.content, 'html.parser')

    # Cuando la función ha encontrado los objetos que buscamos los añade a la lista de jugadores

    for i in pageSoup.find_all("td", {"itemprop": "athlete"}):
        players.append(i.text)

    for i in pageSoup.find_all("td", {"class": "rechts hauptlink"}):
        prices.append(i.text)

    for i in pageSoup.find_all("div", {"class": "rn_nummer"}):
        dorsales.append(i.text)

    for i in pageSoup.find_all(lambda tag: tag.name == 'td' and tag.get('class') == ['zentriert']):
        img = i.find('img', alt=True)
        if img is not None:
            paises.append(img['alt'])

    for i in pageSoup.find_all(lambda tag: tag.name == 'td' and tag.get('class') == ['zentriert']):

        if len(i.text) > 3:
            edades.append(i.text)

    for i in pageSoup.find_all(lambda tag: tag.name == 'table' and tag.get('class') == ['inline-table']):
        length = len(i.text)
        if i.text[length - 7:length] == "Portero":
            text = i.text[length - 7:length]
            posiciones.append(text)
        if i.text[length - 15:length] == "Defensa central":
            text = i.text[length - 15:length]
            posiciones.append(text)
        if i.text[length - 17:length] == "Lateral izquierdo":
            text = i.text[length - 17:length]
            posiciones.append(text)
        if i.text[length - 15:length] == "Lateral derecho":
            text = i.text[length - 15:length]
            posiciones.append(text)
        if i.text[length - 6:length] == "Pivote":
            text = i.text[length - 6:length]
            posiciones.append(text)
        if i.text[length - 11:length] == "Mediocentro":
            text = i.text[length - 11:length]
            posiciones.append(text)
        if i.text[length - 20:length] == "Mediocentro ofensivo":
            text = i.text[length - 20:length]
            posiciones.append(text)
        if i.text[length - 17:length] == "Extremo izquierdo":
            text = i.text[length - 17:length]
            posiciones.append(text)
        if i.text[length - 15:length] == "Extremo derecho":
            text = i.text[length - 15:length]
            posiciones.append(text)
        if i.text[length - 10:length] == "Mediapunta":
            text = i.text[length - 10:length]
            posiciones.append(text)
        if i.text[length - 16:length] == "Delantero centro":
            text = i.text[length - 16:length]
            posiciones.append(text)
        if i.text[length - 18:length] == "Interior izquierdo":
            text = i.text[length - 18:length]
            posiciones.append(text)
        if i.text[length - 16:length] == "Interior derecho":
            text = i.text[length - 16:length]
            posiciones.append(text)

    d = (
        {"Players": players, "Dorsal": dorsales, "Valor": prices, "Edad": edades, "Pais": paises,
         "Posicion": posiciones})

    df = pd.DataFrame(data=d)
    print(df)


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

nombreEquipos = {

    0: "\nA T L E T I C O\n",
    1: "\nB A R C E L O N A\n",
    2: "\nR E A L   M A D R I D\n",
    3: "\nS E V I L L A \n",
    4: "\nR E A L   S O C I E D A D\n",
    5: "\nV I L L A R R E A L\n",
    6: "\nV A L E N C I A\n",
    7: "\nA T H L E T I C\n",
    8: "\nB E T I S\n",
    9: "\nG E T A F E\n",
    10: "\nG R A N A D A\n",
    11: "\nC E L T A\n",
    12: "\nL E V A N T E\n",
    13: "\nA L A V E S\n",
    14: "\nO S A S U N A\n",
    15: "\nE I B A R\n",
    16: "\nV A L L A D O L I D\n",
    17: "\nH U E S C A\n",
    18: "\nC A D I Z\n",
    19: "\nE L C H E\n"

}

urlTransfermark = "https://www.transfermarkt.es/"

PlayersList = list()
ValuesList = list()
DorsalList = list()
PaisList = list()
EdadList = list()
PosicionList = list()

for clave in urlTeamsLaliga:
    valor = nombreEquipos[clave]
    print(valor)
    scrapeo(urlTransfermark + urlTeamsLaliga[clave], PlayersList, ValuesList, DorsalList, PaisList, EdadList,
            PosicionList)
    pasarADB(nombreEquipos[clave], PlayersList, ValuesList, DorsalList, PaisList, EdadList, PosicionList)
    PlayersList = list()
    ValuesList = list()
    DorsalList = list()
    PaisList = list()
    EdadList = list()
    PosicionList = list()
