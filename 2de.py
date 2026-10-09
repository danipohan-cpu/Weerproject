bestand = open( "inputfile", 'r')
bestand2 = open("outputfile",'a')

def auto_bereken(bestand,bestand2 ):
    next(bestand)
    for regel in bestand:
        dataperdag = regel.split()
        datum = str(dataperdag[0])
        tempverschil = int(dataperdag[2]) - int(dataperdag[3])
        if tempverschil >= 20:
            CVstand = 100
        elif tempverschil < 20 and tempverschil >= 10:
            CVstand = 50
        elif tempverschil < 10:
            CVstand = 0
        aantalpersonen = int(dataperdag[1])
        (ventilatiestand) = int(aantalpersonen)+1
        if (ventilatiestand) > 4:
            ventilatiestand = 4
        if int(dataperdag[4]) < 3:
            bewatering = True
        elif int(dataperdag[4]) >= 3:
            bewatering = False
        bestand2.write(
            f"{datum};{CVstand};{ventilatiestand};{bewatering}\n"
        )
bestand.close

def aantal_dagen():
    aantaldagen = -1
    bestand = open("inputfile", 'r')
    for regel in bestand:
        aantaldagen += 1
    return aantaldagen

def override_settings():
    bestand2 = open("outputfile", "r")
    regels = bestand2.readlines()
    bestand2.close()
    datumgevonden = True

    veranderde_dag = input("Welke dag wil je veranderen? Antwoord zoals 05-10-2024: ")

    veranderde_info = int(input("Welke informatie wil je veranderen? 1: CV ketel, 2: ventilatie, 3: bewatering: "))

    nieuwe_waarde = input("Wat moet de nieuwe waarde zijn? ")

    nieuwe_regels = []

    for regel in regels:
        dataperdag = regel.strip().split(";")
        if veranderde_dag == dataperdag[0]:
            dataperdag[veranderde_info] = nieuwe_waarde
            datumgevonden = False
        nieuwe_regels.append(dataperdag)
    if datumgevonden == True:
        eindresultaat = -1
        return eindresultaat

    if veranderde_info < 1:
        eindresultaat = -3
        return eindresultaat
    elif veranderde_info > 3:
        eindresultaat = -3
        return eindresultaat

    bestand2 = open("outputfile", "w")
    for dataperdag in nieuwe_regels:
        bestand2.write(f"{dataperdag[0]};{dataperdag[1]};{dataperdag[2]};{dataperdag[3]}\n")
    bestand2.close()
    eindresultaat = 0
    return eindresultaat



optie = int(input("""welke optie wilt u?
typ 1 voor het aantal dagen in het systeem te zien.
typ 2 Automatisch alle actuatoren berekenen en naar uitvoerbestand schrijven
typ 3 voor het overschrijven van een waarde"""))

if optie == 1:
    hetaantaldagen = aantal_dagen()
    print (f"het aantal dagen is {hetaantaldagen}")
elif optie == 2:
    auto_bereken(bestand,bestand2)
elif optie == 3:
    resultaat = override_settings()
    if resultaat == 0:
        print("Instelling succesvol veranderd.")
    elif resultaat == -1:
        print("Datum niet gevonden.")
    elif resultaat == -3:
        print("Ongeldige keuze.")