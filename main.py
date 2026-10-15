def weervandeweek():
    totaal_temp = 0
    dagen = ('1234567')
    for dag in dagen:
        try:
            print('het is dag ' + (dag))
            temperatuurC_invoer = input('wat is de temperatuur in graden celcius?')
            if temperatuurC_invoer == '':
                break
        except ValueError:
            print ('dit is geen geldige waarde')
        try:
            temperatuurC = float(temperatuurC_invoer)
        except ValueError:
            print('Dit is geen geldige waarde')
            break
        try:
            windsnelheid_invoer = input('wat is de windsnelheid in M/S?')
            if windsnelheid_invoer == '':
                break
        except ValueError:
            print ('dit is geen geldige waarde')
        try:
            windsnelheid = float(windsnelheid_invoer)
        except ValueError:
            print('Dit is geen geldige waarde')
            break
        try:
            luchtvochtigheid_invoer = input('wat is de luchtvochtigheid in %?')
            if luchtvochtigheid_invoer == '':
                break
        except ValueError:
            print ('dit is geen geldige waarde')
        try:
            luchtvochtigheid = float(luchtvochtigheid_invoer)
        except ValueError:
            print('Dit is geen geldige waarde')
            break

        totaal_temp += float(temperatuurC)
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
        print('=====================================================================================')
        print('')
