# headers = {'User-Agent':
#   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}


def scrapeo(url, players, prices,dorsales,playersExcel,valuesExcel,dorsalExcel):
    header = {"User-Agent": "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
    """"
    Mapeo de la página para ello se crea priero el 
    árbol de la página usando los headers originales del navegador
    """
    pageTree = requests.get(url, headers=header)
    pageSoup = BeautifulSoup(pageTree.content, 'html.parser')




    """"
    A continuación encontrará en cada una de las etiquetas tr del sourcecode 
    las que coincidan con los parámetros que usamos como filtro en este caso
    los jugadores tienen asociado un atributo llamado athlete
    ocurre lo mismo para encontrar el precio del jugador en el que hay dos
    clases asociadas a los jugadores una que se llama rechts y otra llamada
    hauptlink
    """
    player = pageSoup.find_all("td", {"itemprop": "athlete"})
    price = pageSoup.find_all("td", {"class": "rechts hauptlink"})
    dorsal = pageSoup.find_all("div", {"class": "rn_nummer"})

    # Cuando la función ha encontrado los objetos que buscamos los añade a la lista de jugadores



    for i in player:
        players.append(i.text)
        playersExcel.append(i.text)

    for i in price:
        prices.append(i.text)
        valuesExcel.append(i.text)

    for i in dorsal:
        dorsales.append(i.text)
        dorsalExcel.append(i.text)





    d = ({"Players": players, "     Dorsal": dorsales, "      Valor": prices})
    dataDos = ({"Players": playersExcel, "     Dorsal": dorsalExcel, "      Valor": valuesExcel})

    dfDos=pd.DataFrame(data=dataDos)

    df = pd.DataFrame(data=d)
    print(df)

    dfDos.to_excel(r'C:\Users\AVG\Desktop\1ºCUATRI\PROYECTOS\equipos.xlsx', index=False,header=True)









import requests
from bs4 import BeautifulSoup

import pandas as pd


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

nombreEquipos={

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

PlayersExcel=list()
ValuesExcel=list()
DorsalExcel=list()


for clave in urlTeamsLaliga:

    valor= nombreEquipos[clave]
    print(valor)
    scrapeo(urlTransfermark + urlTeamsLaliga[clave], PlayersList, ValuesList,DorsalList,PlayersExcel,ValuesExcel,DorsalExcel)
    PlayersList = list()
    ValuesList = list()
    DorsalList = list()
