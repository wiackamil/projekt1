def podaj(tekst):
    while True:
        try:
            x = int(input(tekst))
            if(x<0): 
                raise ValueError()
            return x
        except ValueError:
            print("Podaj sama liczbe!")
def licz_kalorie(czas, tetno):
    return czas * tetno * 0.07
class trening:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.czas = podaj("Podaj czas w minutach: ")
        self.tetno = podaj("Podaj tętno: ")
    def dopisz(self):
        with open("dziennik.txt","a",encoding="utf-8") as plik:
            plik.write(f"Trening: {self.nazwa} | Czas: {self.czas} min | Tetno: {self.tetno} | Kalorie: {licz_kalorie(self.czas, self.tetno)} \n")
            print("trening zapisany w dzienniku!")
def pokaz_historie():
    print("Historia treningow: \n")
    with open("dziennik.txt","r",encoding="utf-8") as plik:
        print(plik.read())

wtorek = trening("bieganie")
wtorek.dopisz()
pokaz_historie()