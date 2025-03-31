mijn_dictionary1 = { "2" : 4,
                    "4" : 16,
                    "10": 100,
                    "12": 144}

def mijn_functie1(keuze1):
    print("De waarde is:", mijn_dictionary1[keuze1])

keuze1 = input("Argument1:")
while keuze1 not in mijn_dictionary1:
    print("Dit argument is niet bekend.")
    keuze1 = input("Argument1:")

if keuze1:
    mijn_functie1(keuze1)

print() #lege regel ter onderscheiding van het uitvoer resultaat

lijst1 = [15, 9, 36, 4]
lijst2 = [14, 10, 24, 6]
lijst3 = [15, 5, 50, 2]
lijst4 = [120, 80, 2000, 5]

mijn_dictionary2 = {"12.3": lijst1,
                    "12.2": lijst2,
                    "10.5": lijst3,
                    "100.20": lijst4}

def mijn_functie2(keuze2):
    print("De waarde is:",mijn_dictionary2[keuze2])

keuze2 = input("Argument2:")
while keuze2 not in mijn_dictionary2:
    print("Dit argument is niet bekend.")
    keuze2 = input("Argument2:")

if keuze2:
    mijn_functie2(keuze2)