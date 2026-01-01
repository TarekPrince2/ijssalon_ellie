from algemene_functies import mijn_functie2

def aanbieding_1(smaak, prijs, korting):
    nieuw_prijs = prijs * (1 - korting)
   
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {korting} euro."

def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    btw_bedrag = totaal * btw
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag} euro btw betaald dient te worden."

def laag_en_hoog(mijn_lijst):
    return [max(mijn_lijst), min(mijn_lijst)]

def gemiddelde(mijn_lijst):
    gem = sum(mijn_lijst) / len(mijn_lijst)
    return f"De gemiddelde inkomsten deze week zijn {gem} euro."

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    return mijn_functie2(korte_lijst)