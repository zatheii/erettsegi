adatok = {}

with open('utca.txt', 'r') as file:
    next(file)

    for line in file:
        sor_adatok = line.strip().split()

        adoszam = sor_adatok[0]
        negyzetmeter = sor_adatok[4]
        tavolsag = sor_adatok[3]
        tovabbi_adatok = ' '.join(sor_adatok[1:4])

        adatok[adoszam] = tovabbi_adatok

telek_szam = len(adatok)
print(f"{telek_szam} telek adatai találhatók az állományban.")

keresett_adoszam = input("Adja meg az adószámát: ")

if keresett_adoszam in adatok:
    print(f"További adatok: {adatok[keresett_adoszam]}")
else:
    print("Nem szerepel az adattárolóban.")

def ado(adozas, negyzetmeter):
    befizetettado = 0

    if adozas.lower() == "c":
        befizetettado = negyzetmeter * 100
    elif adozas.lower() == "b":
        befizetettado = negyzetmeter * 600
    elif adozas.lower() == "a":
        befizetettado == negyzetmeter * 800

    if befizetettado > 10000:
        befizetettado=0

    return befizetettado

atelek = 0
btelek = 0
ctelek = 0

atelekado = 0
btelekado = 0
ctelekado = 0

for savok in tavolsag:
    if savok.lower() == "a":
        atelek += 1
        atelekado += ado(tavolsag,negyzetmeter)
    elif savok.lower() == "b":
        btelek += 1
        btelekado += ado(tavolsag, negyzetmeter)
    elif savok.lower() == "c":
        ctelek += 1
        ctelekado += ado(tavolsag, negyzetmeter)
print(f"A sávba {atelek} telek esik, az adó {atelekado}")
print(f"B sávba {btelek} telek esik, az adó {btelekado}")
print(f"C sávba {ctelek} telek esik, az adó {ctelekado}")
