"""
Számok száma
Írj egy függvényt, amely megszámolja az adott listában található számok számát, majd visszaadja azt.

Páros számok kiválogatása
Írj egy függvényt, amely egy adott listából kiválogatja az összes páros számot, majd visszaadja ezeket egy új listában.

Legnagyobb szám megtalálása
Írj egy függvényt, amely megtalálja az adott listában található legnagyobb számot, majd visszaadja azt.

Szöveg összefűzése
Írj egy függvényt, amely összefűzi az adott szövegeket egyetlen nagyobb szöveggé, majd visszaadja azt.

Fibonacci sorozat generálása
Írj egy függvényt, amely a megadott számnál kisebb Fibonacci-sorozatot generál, majd visszaadja azt.

Számok átlaga
Írj egy függvényt, amely meghatározza az adott listában található számok átlagát, majd visszaadja azt.
"""
lista = [15, 2, 8, 20, 25]
szovegek = ["Az ", "ágazati ", "vizsga ", "gatya ", "lesz."]
fib = [0, 1]  # előző két Fibonacci szám

def szamok_szama(lista):
    sz_szama = 0
    for szamok in lista:
        sz_szama += 1
    return sz_szama

def paros_szamok(lista):
    paros = []
    for szamok in lista:
        if szamok % 2 == 0:
            paros.append(szamok)
    return paros

def legnagyobb_szam(lista):
    legnagyobb_szam = lista[0]
    for szam in lista:
        if szam > legnagyobb_szam:
            legnagyobb_szam = szam
    return legnagyobb_szam

def szoveg_osszefuzese(szovegek):
    osszefuzott_szoveg = ""
    for szoveg in szovegek:
        osszefuzott_szoveg += szoveg
    return osszefuzott_szoveg

def fibonacci():
    n = int(input("Számot adj: "))
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fibonacci
fibonacci()

def szamok_atlaga(lista):
    ossz = 0
    szamok = 0
    for szam in lista:
        ossz += szam
        szamok += 1
    if szamok == 0:
        return 0
    else:
        return ossz / szamok



print(f"Feladatok gyors ellenőrzése \n\nSzámok száma: {szamok_szama(lista)}")
print(f"Páros számok kiválogatása: {paros_szamok(lista)}")
print(f"Legnagyobb szám megtalálása: {legnagyobb_szam(lista)}")
print(f"Szöveg összefűzése: {szoveg_osszefuzese(szovegek)}")
print(f"Fibonacci sorozat generálása: {(fib)}")
print(f"Számok átlaga: {szamok_atlaga(lista)}")
