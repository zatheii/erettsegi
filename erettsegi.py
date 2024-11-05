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
        print(tovabbi_adatok[3])       
telek_szam = len(adatok)
print(f"{telek_szam} telek adatai találhatók az állományban.")

keresett_adoszam = input("Adja meg az adószámát: ")

if keresett_adoszam in adatok:
    print(f"További adatok: {adatok[keresett_adoszam]}")
else:
    print("Nem szerepel az adattárolóban.")

def ado(adozas, negyzetmeter):
    befizetettado = 0
    
            
    if adozas > 10000:
        ado=0
    return befizetettado
