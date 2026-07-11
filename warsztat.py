class Auto:
    def __init__(self, marka, model, rok_produkcji):
        self.marka = marka
        self.model = model
        self.rok_produkcji = rok_produkcji
        self.status = "do naprawy"
    def napraw(self, koszt):
        self.status = "naprawione"
        print(f"Auto {self.marka} {self.model} zostało naprawione za {koszt} i jest gotowe do odbioru")
class Warsztat:
    def __init__(self, nazwa):
        self.kasa = 0
        self.nazwa = nazwa
        self.lista_aut = []
    def przyjmij_auto(self, auto):
        self.lista_aut.append(auto)
        print(f"Auto {auto.marka} {auto.model} zostało przyjęte do warsztatu {self.nazwa}")
    def pokaz_garaz(self):
        print(f"Warsztat {self.nazwa} ma w garażu następujące auta:")
        for auto in self.lista_aut:
            print(f"- {auto.marka} {auto.model} ({auto.rok_produkcji}) - {auto.status}")
        print(f"Na koncie warsztatu znajduje się {self.kasa} złotych")
    def napraw_w_warsztacie(self, auto, koszt):
        if auto.status == "naprawione":
            print(f"Nie naciągamy klientów!")
        else:
            auto.napraw(koszt)
            self.kasa += koszt
        
AutoFix = Warsztat("AutoFix")
AutoFix.pokaz_garaz()
Audi = Auto("Audi", "A4", 2020)
Punto = Auto("Fiat", "Punto", 2010)
AutoFix.przyjmij_auto(Audi)
AutoFix.przyjmij_auto(Punto)
AutoFix.napraw_w_warsztacie(Punto, 80)
AutoFix.pokaz_garaz()
AutoFix.napraw_w_warsztacie(Punto, 80)