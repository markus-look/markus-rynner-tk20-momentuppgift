# Markus Rynner, TK20
#Moment03u09
'''
monadLon = int(input('Vad är din månadslön?'))
kommunalskat = 0.2136 * monadLon
landstingsSkatt = 0.1148 * monadLon
vinst = monadLon - kommunalskat - landstingsSkatt

print(""""Utskrift
Månadslön \t {0}
Kommunal skatt \t {1}
Landsstingsskatt \t {2}
Kvar efter skatt \t {3}
""".format(monadLon, int(kommunalskat), int(landstingsSkatt), int(vinst) ))
'''
# Markus Rynner, TK20
#Moment03u09

statskatt = 0
varnSkatt = 0
#monadLon = int(input('Vad är din månadslön?'))
kommunalskat = 0
landstingsSkatt = 0
'''
if monadLon < 19247:
    kommunalskat += 0 * monadLon
    landstingsSkatt += 0 * monadLon
elif monadLon >= 19247:
    kommunalskat = 0.2136 * (monadLon - 19247)
    landstingsSkatt = 0.1148 * (monadLon - 19247)
    if monadLon >= 468700:
        statskatt = 0.2 * (monadLon - 468700)
        if monadLon >= 675000:
            varnSkatt = 0.05 * (monadLon - 675000)
tSkatt = kommunalskat + landstingsSkatt + varnSkatt + statskatt
percentage = tSkatt/monadLon * 100
vinst = monadLon - tSkatt
print(""""Utskrift
Månadslön \t {0}
Kommunal skatt \t {1}
Landsstingsskatt \t {2}
""".format(monadLon, int(kommunalskat), int(landstingsSkatt), int(vinst) ))
if statskatt != 0:
    print("Statskatt \t {0}".format(int(statskatt)))
if varnSkatt != 0:
    print("Varnskatt \t {0}".format(int(varnSkatt)))
print("Kvar efter skatt \t {0}".format(int(vinst)))
print("Andel betald skatt: \t {0:.1f}%".format(percentage))
'''
print("Årsinkomst \t Månadsinkomst \t Total Skatt \t Netto / Mån \t Kommunals \t Statlig s. \t Total Skatt %")

lonExample = (1500, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000, 60000)
for monadLon in (lonExample):
    if monadLon < 19247:
        kommunalskat += 0 * monadLon
        landstingsSkatt += 0 * monadLon
    elif monadLon >= 19247:
        kommunalskat = 0.2136 * (monadLon - 19247)
        landstingsSkatt = 0.1148 * (monadLon - 19247)
        if monadLon >= 468700:
            statskatt = 0.2 * (monadLon - 468700)
            if monadLon >= 675000:
                varnSkatt = 0.05 * (monadLon - 675000)
    tSkatt = kommunalskat + landstingsSkatt + varnSkatt + statskatt
    percentage = tSkatt/monadLon * 100
    vinst = monadLon - tSkatt
    print(f"|{(monadLon*12):<10.0f}| {monadLon:<14.0f}| {tSkatt:<13.0f}| {vinst:<15.0f}| {kommunalskat:<10.0f}| {statskatt:<14.0f}|{percentage:12.0f}%|")
