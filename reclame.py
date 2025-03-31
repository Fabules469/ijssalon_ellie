from algemene_functies import mijn_functie2

print()#lege regel
def aanbieding_1(smaak, prijs, korting):
    print(f"Vandaag in aanbieding: emmertje ijs (1 liter) {smaak}, van {prijs} voor {prijs - (prijs * korting)} euro.")

aanbieding_1("aardbei",4, 0.1)

print()
week_inkomen = [220, 430, 125, 160, 205, 90, 345]

totaal = 0
def inkomsten_totaal1(inkomsten):
    global totaal
    totaal = sum(inkomsten)
    return totaal

print(f"Totaal van alle bedragen is {inkomsten_totaal1(week_inkomen)} euro.")

print()
btw = 0.09
def inkomsten_totaal2(inkomsten, btw):
    print(f"Het totaal van alle inkomen van deze week is {totaal} euro, waarover het {totaal * btw} euro betaald dient te worden.")

inkomsten_totaal2(totaal, btw)

print()
mijn_lijst = [220, 430, 125, 160, 205, 90, 345]

def laag_en_hoog(lijst):
    print(f"Hoogste waarde is {max(mijn_lijst)}, laagste waarde is {min(mijn_lijst)}")

laag_en_hoog(mijn_lijst)

print()
def gemiddelde(lijst1):
    return sum(lijst1) / len(lijst1)

print(f"De gemiddelde inkomsten deze week zijn {round(gemiddelde(mijn_lijst))} euro.")

print()
invoer_lijst = [10, 5, 3, 2, 1, 9]

def hoog_laag(lijst2):
    print(f"Hoogste waarde is {max(lijst2)}, laagste waarde is {min(lijst2)}")

def meervoudig(lijst2):
    hoog_laag(lijst2)

meervoudig(invoer_lijst)

print()#Dit is de laaste gedeelte vanaf vraag 12 huiswerk verzoek, die ik niet helemaal begrijpt wat er oorspronkelijk gevraagd wordt.
#graag een uitleg hiervan AUB!
invoer_lijst2 = [100, 987, 234, 123, 786, 87, 109, 184]
korte_lijst = []

def combinatie(lijst3):
    laag_en_hoog(lijst3)
    print(f"Hoogste waarde is {max(lijst3)}, laagste waarde is {min(lijst3)}")
    korte_lijst.append(max(lijst3))
    korte_lijst.append(min(lijst3))

print()
combinatie(invoer_lijst2)
print()
print(list(korte_lijst))