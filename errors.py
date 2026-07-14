def podaj(tekst):
    while True:
        try:
            x = int(input(tekst))
            if(x<0): 
                raise ValueError()
            return x
        except ValueError:
            print("Podaj sama liczbe!")
czas = podaj("Podaj czas w minutach")
tetno = podaj("Podaj tętno")
print(czas*tetno*0.068)


    
