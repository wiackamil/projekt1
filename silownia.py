class Cwiczenie:
    def __init__(self,nazwa,serie,powtorzenia):
        self.nazwa = nazwa
        self.powtorzenia = powtorzenia
        self.serie = serie
    def pokaz_plan(self):
        print(f"🏋️‍♂️ Ćwiczenie: {self.nazwa} - {self.serie} serii po {self.powtorzenia} powtórzeń.")
class CwiczenieSila(Cwiczenie):
    def __init__(self, nazwa, serie, powtorzenia, ciezar):
        super().__init__(nazwa,serie,powtorzenia)
        self.ciezar = ciezar     
    def pokaz_cwicz(self):
        print(f"🏋️‍♂️ Ćwiczenie: {self.nazwa} - {self.serie}x{self.powtorzenia} z ciężarem {self.ciezar} kg.")
class Plan:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.lista = []
    def dodaj(self,cwiczonko):
        self.lista.append(cwiczonko)
    def odczytaj(self):
        for cwiczonko in self.lista:
            print(f"🏋️‍♂️ Ćwiczenie: {cwiczonko.nazwa} - {cwiczonko.serie}x{cwiczonko.powtorzenia} z ciężarem {cwiczonko.ciezar} kg.")

        


martwy_ciag = CwiczenieSila("Martwy Ciąg", 4, 5, 100)
bench_press = CwiczenieSila("Bench Press", 8, 5, 120)
Plecy = Plan("Plecy")
Plecy.dodaj(martwy_ciag)
Plecy.dodaj(bench_press)
Plecy.odczytaj()


