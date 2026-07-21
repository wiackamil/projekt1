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
    def na_slownik(self):
        return {
            'nazwa':self.nazwa,
            'ilosc':self.ilosc,
            'data':self.data.strftime("%d.%m.%Y"),
            'minIlosc':self.minIlosc
        }
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
    nazwa = pobierz('nazwa','Podaj nazwe swojego produktu: ')
    ilosc = pobierz('liczba','Podaj ilosc produktu: ')
    data = pobierz('data','Podaj date waznosci w formacie DD.MM.RRRR: ')
    minIlosc = pobierz('liczba', 'Podaj minimalna ilosc przy jakiej ma wyskoczyc alert: ')
    spizarka.append(Produkt(nazwa,ilosc,data,minIlosc))
def wypisz_menu():
    print(f"""
    ==============================
    Wybierz co chcesz zrobic:
    1. Zobaczyc stan spizarki
    2. Dodac produkt
    3. Usunac produkt 
    4. Opuscic program
    """)

def wypisz_spizarka():
    print('Stan spizarki: \n')
    for i,przedmiot in enumerate(spizarka):
        print(f"{i+1}. {przedmiot}")

def wczytaj():
    try:
        with open("fridge_content.json","r",encoding="utf-8") as plik:
            dane = json.load(plik)
            x = list()
        for obiekt in dane:
            produkt = Produkt(obiekt['nazwa'],obiekt['ilosc'],datetime.strptime(obiekt['data'], "%d.%m.%Y").date(),obiekt['minIlosc'])
            x.append(produkt)
        return x
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def zapisz():
    with open("fridge_content.json","w",encoding="utf-8") as plik:
        z = list()
        for przedmiot in spizarka:
            z.append(przedmiot.na_slownik())
        json.dump(z,plik,indent=4)

def usun():
    wypisz_spizarka()
    try:
        numer = pobierz('liczba','Wybierz numer produktu ktory chcesz usunac')-1
        if numer>=len(spizarka) or numer<0:
            raise Exception("Zly indeks produktu")          
        ile = pobierz('liczba','Ile chcesz tego usunac?')
        temp = spizarka[numer]
        if temp.ilosc<ile:
            raise Exception("Nie masz tyle w spizarce")
        else:
            if temp.ilosc-ile<0.01:
                del spizarka[numer]
            else:
                spizarka[numer].ilosc-=ile
    except Exception as e:
        print(e)
        return

    
spizarka = wczytaj()
while True:
    wypisz_menu()
    wybor = input()
    if wybor == '1':
        wypisz_spizarka()
    elif wybor == '2':
        dodaj_produkt()
    elif wybor == '3':
        usun()
    elif wybor == '4':
        zapisz()
        break
    else:
        print("blad, podaj jeszcze raz")
exit()