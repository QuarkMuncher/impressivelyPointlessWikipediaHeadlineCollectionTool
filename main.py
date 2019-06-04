import time as tid
import requests as forespørgsler
from bs4 import BeautifulSoup as SmukSuppe

def whut():
    resultat = forespørgsler.get('https://en.wikipedia.org/wiki/Special:Random')
    suppe = SmukSuppe(resultat.content, 'html.parser')
    kondenseret_suppe = suppe.h1
    fil = open("TheMeaningOfLife.txt", "a+")
    if kondenseret_suppe.i:
        loven = kondenseret_suppe.decode_contents().replace("<i>", "").replace("</i>", "").replace('&amp;', 'og') + " er ikke nice"
        fil.write(loven + "\n")
        print(loven)
    else:
        loven = suppe.h1.decode_contents().replace('&amp;', 'og') + " er nice"
        fil.write(loven + "\n")
        print(loven)
    fil.close()


while(True):
    whut()
    tid.sleep( 3 )
