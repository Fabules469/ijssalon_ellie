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
        
def onderstreep(tekst):
    uit = []
    uit.append(tekst)
    uit.append(len(tekst) * "=")
    #print((len(tekst) * "="))
    #print(tekst)
    #print((len(tekst) * "="))
    return uit
    
#print(fooi_pp(100, 2))
#print()
#print(onderstreep("Test programma"))
