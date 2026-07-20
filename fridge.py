import json
from datetime import datetime

class Produkt:
    def __init__(self,nazwa,ilosc,data,minIlosc):
        self.nazwa = nazwa
        self.ilosc = ilosc
        self.data = data
        self.minIlosc = minIlosc
    def __repr__(self):
        return(f"{self.nazwa}, {self.ilosc} sztuki, {self.data}, alarm przy {self.minIlosc} sztukach")

def pobierz(rodzaj,tekst):
    if rodzaj == 'nazwa':
        return input(tekst)
    if rodzaj == 'data':
        while True:
            try:
                x = input(tekst)
                data = datetime.strptime(x, "%d.%m.%Y").date()
                return data
            except ValueError:
                print(f"Wystapil blad przy podawaniu daty. Format to [DD.MM.RRRR]. Sprobuj ponownie: ")
    if rodzaj == 'liczba':
        while True:
            try:
                x = float(input(tekst))
                return x
            except ValueError:
                print(f"Wystapil blad przy podawaniu wartosci. Sprobuj ponownie: ")   


def dodaj_produkt():
    nazwa = pobierz('nazwa','Podaj nazwe swojego produktu')
    ilosc = pobierz('liczba','Podaj ilosc produktu')
    data = pobierz('data','Podaj date waznosci w formacie DD.MM.RRRR')
    minIlosc = pobierz('liczba', 'Podaj minimalna ilosc przy jakiej ma wyskoczyc alert')
    spizarka.add(Produkt(nazwa,ilosc,data,minIlosc))
def wypisz_menu():
    print(f"""
    ==============================
    Wybierz co chcesz zrobic:
    1. Zobaczyc stan spizarki
    2. Dodac produkt
    3. Usunac produkt 
    4. Opuscic program
    """)

spizarka = set()

def wczytaj():
    try:
        with open("fridge_content.json","r",encoding="utf-8") as plik:
            for product in plik:
                spizarka.add(json.load(product))
    except FileNotFoundError:
        print("Błąd: Nie znaleziono pliku. najpierw cos zapisz")

def zapisz():
    with open("fridge_content.json","w",encoding="utf-8") as plik:
        json.dump(spizarka)

def usun(produkt):
    pass


wypisz_menu()
print(spizarka)
dodaj_produkt()