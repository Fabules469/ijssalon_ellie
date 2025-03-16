prijzen_dictionary = {
    "Aardbei" : "3",
    "Vanille" : "4",
    "Chocolade" : "5"
}
for k, v in prijzen_dictionary.items():
    print(k, ":",v)

print()
prijzen_dictionary["Aanbieding"] = float(prijzen_dictionary["Aardbei"]) * float("0.8") 

print()
for k, v in prijzen_dictionary.items():
    print(k, ":", v)

print()
reclame_tekst1 = f"Vandaag is de aanbieding: vanille-ijs, 1 liter slechts € {prijzen_dictionary["Aanbieding"]}"
reclame_tekst2 = reclame_tekst1
print(reclame_tekst1)

print()
print(reclame_tekst2[:61])

print()
reclame_tekst3 = reclame_tekst2[:61].upper() # alles in hoofdletter omzetten
print(reclame_tekst3)

print()
reclame_tekst4 = [reclame_tekst3[:7], reclame_tekst3[8:11], reclame_tekst3[11:13], reclame_tekst3[14:25], reclame_tekst3[26:37], reclame_tekst3[39:40], reclame_tekst3[41:46], reclame_tekst3[47:54], reclame_tekst3[55:56], reclame_tekst3[57:63]]
print(list(reclame_tekst4)) # list hoofdletter uitprinten (eerste optie)
print(reclame_tekst3.split()) # list hoofdletter uitprinten (tweede optie) welke is gemakkelijk

print()
for el in reclame_tekst4:
    print(el) # onder elkaar uitprinten

print()
for el in reclame_tekst4:
    print(el.lower()) # kleinletter omzetten en onder elkaar uitprinten

print()
print()
reclame_tekst5 = list(reclame_tekst4)
print(reclame_tekst5) # deze regel toegevoegd om de kompleet lijst uit te printen
for el in reclame_tekst5:
    if len(el) > 4:
        print(el.upper()) # item ofwel el is al hoofdletter
        print(len(el)) # deze regel toegevoegd om de werkelijk lengte aan te geven van ieder woord
    else:
        print(el.lower()) # item ofwel el wordt kleinletter. Jammer genoeg krijg ik de items Liter en slecht niet omgezet en weet geen raad mee!