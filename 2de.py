import requests

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
    try:
        veranderde_dag = input("Welke dag wil je veranderen? Antwoord zoals 05-10-2024: ")

        veranderde_info = int(input("Welke informatie wil je veranderen? 1: CV ketel, 2: ventilatie, 3: bewatering: "))

        nieuwe_waarde = input("Wat moet de nieuwe waarde zijn? ")
    except:
        print('dit is geen geldige waarde')

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

def weerinhuizen():
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": 52.2992,
        "longitude": 5.2418,
        "current": "temperature_2m",
        "timezone": "Europe/Amsterdam"
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()
    temperatuur = data["current"]["temperature_2m"]
    return temperatuur

def weervandeweek():
    totaal_temp = 0
    dagen = ('1234567')
    for dag in dagen:
        try:
            print('het is dag ' + (dag))
            temperatuurC = float(input('wat is de temperatuur in graden celcius?'))
            windsnelheid = float(input('wat is de windsnelheid in M/S?'))
            luchtvochtigheid = float(input('wat is de luchtvochtigheid in %?'))
        except:
            print ('dit is geen geldige waarde')

        totaal_temp += temperatuurC
        farenheit = ((temperatuurC) * 1.8) + 32
        print('de afgelopen dagen is het gemideld, ' + str(totaal_temp / int(dag)))

        print("de temperatuur in farenheit is " + str(farenheit))
        gevoelstemperatuur = temperatuurC - luchtvochtigheid / 100 * windsnelheid
        print("de gevoelstemperatuur is " + str(gevoelstemperatuur))

        if gevoelstemperatuur < 0 and windsnelheid > 10:
            print('Het is heel koud en het stormt, doe de verwarming aan')
        elif gevoelstemperatuur < 0 and windsnelheid <= 10:
            print('Het is behoorlijk koud! Verwarming aan op de benedenverdieping!')
        elif gevoelstemperatuur >= 0 and gevoelstemperatuur < 10 and windsnelheid > 12:
            print('Het is best koud en het waait; verwarming aan en roosters dicht!')
        elif gevoelstemperatuur >= 0 and gevoelstemperatuur < 10 and windsnelheid < 12:
            print('Het is een beetje koud, elektrische kachel op de benedenverdieping aan!')
        elif gevoelstemperatuur >= 10 and gevoelstemperatuur < 22:
            print('Heerlijk weer, niet te koud of te warm.')
        else:
            print('Warm! Airco aan!')

        print('')
        print('=======================================================================================')
        print('')

while True:
    optie = (input("""welke optie wilt u?
    typ 1 voor het aantal dagen in het systeem te zien.
    typ 2 Automatisch alle actuatoren berekenen en naar uitvoerbestand schrijven
    typ 3 voor het overschrijven van een waarde
    typ 4 voor het huidige weer in huizen
    typ 5 om uw informatie van de week in te vullen zodat u benodige informatie terug krijgt
    typ 6 om te stoppen"""))

    if optie == '1':
        hetaantaldagen = aantal_dagen()
        print (f"het aantal dagen is {hetaantaldagen}")
    elif optie == '2':
        auto_bereken(bestand,bestand2)
    elif optie == '3':
        resultaat = override_settings()
        if resultaat == 0:
            print("Instelling succesvol veranderd.")
        elif resultaat == -1:
            print("Datum niet gevonden.")
        elif resultaat == -3:
            print("Ongeldige keuze.")
    elif optie == '4':
        temperatuur = weerinhuizen()
        print(f"De temperatuur in Huizen is {temperatuur} °C")
    elif optie == '5':
        weervandeweek()
    elif optie == '6':
        break
    else:
        print ('dit is geen geldige waarde, kan u het opnieuw invullen?')