from helper import onderstreep

def presenteer(dict_naam, totaal):
    for item, waarde in dict_naam.items():
        print(f"{item} : {waarde} euro")
    onderstreep("Totalen inkomsten")
    print(f"Totaal: {totaal} euro")

