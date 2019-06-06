import time as tid
import requests as forespørgsler
from bs4 import BeautifulSoup as SmukSuppe
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import settings as s
from colorama import Fore, init

init()

engine = create_engine(
    f"{s.DB_DRIVER}://{s.DB_USER}:{s.DB_PASSWORD}@{s.DB_SERVER}/{s.DB_NAME}"
)
meta = MetaData()
wikilist = Table(
    "wikilist",
    meta,
    Column("id", Integer, primary_key=True),
    Column("headline", String(100)),
)


def whut():
    resultat = forespørgsler.get(
        "https://en.wikipedia.org/wiki/Special:Random"
    )
    suppe = SmukSuppe(resultat.content, "html.parser")
    kondenseret_suppe = suppe.h1

    if kondenseret_suppe.i:
        loven = (
            kondenseret_suppe.decode_contents()
            .replace("<i>", "")
            .replace("</i>", "")
            .replace("&amp;", "og")
            + " er ikke nice"
        )
        conn = engine.connect()
        ins = wikilist.insert().values(headline=loven)
        conn.execute(ins)
    else:
        loven = suppe.h1.decode_contents().replace("&amp;", "og") + " er nice"
        conn = engine.connect()
        ins = wikilist.insert().values(headline=loven)
        conn.execute(ins)


while True:
    try:
        whut()
        print(Fore.GREEN + "--------------------------------")
        print(Fore.GREEN + "|   https request Succeeded    |")
        print(Fore.GREEN + "--------------------------------")
    except Exception:
        print(Fore.RED + "--------------------------------")
        print(Fore.RED + "|   https request failed       |")
        print(Fore.RED + "--------------------------------")

    tid.sleep(3)
