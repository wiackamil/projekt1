class Bohater:
    def __init__(self, imie, profesja):
        self.imie = imie
        self.profesja = profesja
        self.zloto = 100         
        self.ekwipunek = []      

    # 1. METODA DO UZUPEŁNIENIA
    def podnies_przedmiot(self, nazwa_przedmiotu):
        self.ekwipunek.append(nazwa_przedmiotu)
        print(f"{self.imie} podnosi {nazwa_przedmiotu}!")

    # 2. METODA DO UZUPEŁNIENIA
    def kup_przedmiot(self, nazwa_przedmiotu, koszt):
        if self.zloto >= koszt:
            self.zloto = self.zloto - koszt
            self.ekwipunek.append(nazwa_przedmiotu)
            print(f"{self.imie} kupuje {nazwa_przedmiotu}!")
        else:
            print(f"{self.imie} nie ma wystarczającej ilości złota!")

    def pokaz_status(self):
        print(f"\n--- STATUS POSTACI: {self.imie} ({self.profesja}) ---")
        print(f"Złoto: {self.zloto}")
        print(f"Ekwipunek: {self.ekwipunek}")
        print("----------------------------------------")


# === TESTOWANIE PROGRAMU (To się uruchomi) ===
gracz = Bohater("Kamil", "Wojownik")
gracz.pokaz_status()

# Test podnoszenia
gracz.podnies_przedmiot("Żelazny Miecz")

# Test zakupów (masz 100 złota, mikstura kosztuje 30 - powinno się udać)
gracz.kup_przedmiot("Mikstura Życia", 30)

# Test zakupów (tarcza kosztuje 500 - powinno wypisać błąd)
gracz.kup_przedmiot("Legendarna Tarcza", 500)

gracz.pokaz_status()