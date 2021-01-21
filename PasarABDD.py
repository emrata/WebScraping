# headers = {'User-Agent':
#   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
import sqlite3
import requests
from bs4 import BeautifulSoup

import pandas as pd

con = sqlite3.connect('equipos.db')
cursorObj=con.cursor()
cursorObj.execute('''CREATE TABLE ActualizacionUno(jugador TEXT, edad INT, pais TEXT, equipos TEXT, dorsal INT, posicion TEXT, precio FLOAT)''')
con.commit()


def pasarAdb(players,price,dorsales,paises,edades,posiciones,equipo):




    i=0
    while i < len(players):
        con.execute('''INSERT INTO ActualizacionUno(jugador,edad,pais,equipos,dorsal,posicion,precio) VALUES(?, ?, ?, ?, ?, ?, ?)''',
                  (players[i], edades[i], paises[i], equipo[i], dorsales[i], posiciones[i], price[i]))
        con.commit()
        i=i+1;
    print("Informacion migrada a la DB")
#c.close()






def scrapeo(url, players, prices, dorsales, paises, edades, posiciones, equipos, playersExcel, valuesExcel, dorsalExcel,
            paisExcel, edadExcel, posicionExcel, equipoExcel):
    header = {"User-Agent": "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
    """"
    Mapeo de la página para ello se crea priero el 
    árbol de la página usando los headers originales del navegador
    """
    pageTree = requests.get(url, headers=header)
    pageSoup = BeautifulSoup(pageTree.content, 'html.parser')

    equipo = "local"
    aux = 0

    # Cuando la función ha encontrado los objetos que buscamos los añade a la lista de jugadores

    for i in pageSoup.find_all("td", {"itemprop": "athlete"}):
        players.append(i.text)
        playersExcel.append(i.text)
        aux += 1
        resultado="local"

    for i in pageSoup.find_all("td", {"class": "rechts hauptlink"}):
        prices.append(i.text)
        valuesExcel.append(i.text)

    for i in pageSoup.find_all("div", {"class": "rn_nummer"}):
        dorsales.append(i.text)
        dorsalExcel.append(i.text)

    for i in pageSoup.find_all(lambda tag: tag.name == 'td' and tag.get('class') == ['zentriert']):
        img = i.find('img', alt=True)
        if img is not None:
            paises.append(img['alt'])
            paisExcel.append(img['alt'])

    for i in pageSoup.find_all(lambda tag: tag.name == 'td' and tag.get('class') == ['zentriert']):

        if (len(i.text) > 3):
            edades.append(i.text)
            edadExcel.append(i.text)

    for i in pageSoup.find_all(lambda tag: tag.name == 'table' and tag.get('class') == ['inline-table']):
        lenght = len(i.text)
        if (i.text[lenght - 7:lenght] == "Portero"):
            text = i.text[lenght - 7:lenght]
            posiciones.append(text)
            posicionExcel.append(text)
        if (i.text[lenght - 15:lenght] == "Defensa central"):
            text = i.text[lenght - 15:lenght]
            posiciones.append(text)
            posicionExcel.append(text)
        if (i.text[lenght - 17:lenght] == "Lateral izquierdo"):
            text = i.text[lenght - 17:lenght]
            posiciones.append(text)
            posicionExcel.append(text)
        if (i.text[lenght - 15:lenght] == "Lateral derecho"):
            text = i.text[lenght - 15:lenght]
            posiciones.append(text)
            posicionExcel.append(text)
        if (i.text[lenght - 6:lenght] == "Pivote"):
            text = i.text[lenght - 6:lenght]
            posiciones.append(text)
            posicionExcel.append(text)
        if (i.text[lenght - 11:lenght] == "Mediocentro"):
            text = i.text[lenght - 11:lenght]
            posiciones.append(text)
            posicionExcel.append(text)
        if (i.text[lenght - 20:lenght] == "Mediocentro ofensivo"):
            text = i.text[lenght - 20:lenght]
            posiciones.append(text)
            posicionExcel.append(text)
        if (i.text[lenght - 17:lenght] == "Extremo izquierdo"):
            text = i.text[lenght - 17:lenght]
            posiciones.append(text)
            posicionExcel.append(text)
        if (i.text[lenght - 15:lenght] == "Extremo derecho"):
            text = i.text[lenght - 15:lenght]
            posiciones.append(text)
            posicionExcel.append(text)
        if i.text[lenght - 10:lenght] == "Mediapunta":
            text = i.text[lenght - 10:lenght]
            posiciones.append(text)
            posicionExcel.append(text)
        if i.text[lenght - 16:lenght] == "Delantero centro":
            text = i.text[lenght - 16:lenght]
            posiciones.append(text)
            posicionExcel.append(text)
        if i.text[lenght - 18:lenght] == "Interior izquierdo":
            text = i.text[lenght - 18:lenght]
            posiciones.append(text)
            posicionExcel.append(text)
        if i.text[lenght - 16:lenght] == "Interior derecho":
            text = i.text[lenght - 16:lenght]
            posiciones.append(text)
            posicionExcel.append(text)

    for i in pageSoup.find_all(lambda tag: tag.name == 'div' and tag.get('class') == ['dataName']):
        equipo = i.text
        equipo=equipo.rstrip()
        resultado=equipo[2:len(equipo)]

    for i in range(aux):
        equipos.append(resultado)
        equipoExcel.append(resultado)

    d = (
    {"Players": players, "Dorsal": dorsales, "Valor": prices, "Edad": edades, "Pais": paises, "Posicion": posiciones,
     "Equipo": equipos})
    dataDos = (
    {"Players": playersExcel, "Dorsal": dorsalExcel, "Valor": valuesExcel, "Edad": edadExcel, "Pais": paisExcel,
     "Posicion": posicionExcel, "Equipo": equipoExcel})

    df = pd.DataFrame(data=d)
    dfDos = pd.DataFrame(data=dataDos)

    print(df)
    dfDos.to_excel(r'C:\Users\AVG\Desktop\1ºCUATRI\PROYECTOS\equipos.xlsx', index=False, header=True)

    pasarAdb(players,prices,dorsales,paises,edades,posiciones,equipos)






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
EquipoList = list()

PlayersExcel = list()
ValuesExcel = list()
DorsalExcel = list()
PaisExcel = list()
EdadExcel = list()
PosicionExcel = list()
EquipoExcel = list()

for clave in urlTeamsLaliga:
    valor = nombreEquipos[clave]
    print(valor)
    scrapeo(urlTransfermark + urlTeamsLaliga[clave], PlayersList, ValuesList, DorsalList, PaisList, EdadList,
            PosicionList, EquipoList, PlayersExcel, ValuesExcel, DorsalExcel, PaisExcel, EdadExcel, PosicionExcel,
            EquipoExcel)
    PlayersList = list()
    ValuesList = list()
    DorsalList = list()
    PaisList = list()
    EdadList = list()
    PosicionList = list()
    EquipoList = list()



