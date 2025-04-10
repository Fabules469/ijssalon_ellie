def decoreer(tekst = ""):
    lengte = len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()

def fooi_pp(bedrag, personen): 
    try:   
        bedrag_pp = bedrag/personen
    except:
        bedrag_pp = "??"
        print(f"Bedrag is: {bedrag_pp}")
        exit()
    else:
        return f"Het bedrag per persoon is {bedrag_pp} euro"    
        
def onderstreep(tekst=""):
    lengte = len(tekst) + 15
    print(lengte * "=")
    

def som(dict_naam):
    totaal = 0
    for item in dict_naam:
        totaal += dict_naam[item]
    return totaal