from abc import ABC, abstractmethod
from datetime import datetime

current_datetime = datetime.now()
today = current_datetime.strftime('%Y.%m.%d.')

todayint = (today)

print(today)

class Szoba(ABC):
    def __init__(self,szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar
    
    @abstractmethod
    def típus(self):
        pass

class Egyagyas(Szoba):
    def típus(self):
        return "Egyágyas szoba"

class Kétágyas(Szoba):
    def típus(self):
        return "Kétágyas szoba"


class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = {}
    
    def szoba_hozzáadása(self, szoba):
        self.szobak.append(szoba)
    
    def foglalas(self, szobaszam, datum, nev):
        talalat = False
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                talalat = True
                if szobaszam not in self.foglalasok:
                    self.foglalasok[szobaszam] = {}
                if datum in self.foglalasok[szobaszam]:
                    print("Ez a szoba erre a napra már le lett foglalva. Sajnáljuk, próbáljon másik szobát erre az időpontra.")
                    return
                self.foglalasok[szobaszam][datum] = nev
                print(f"A foglalása sikeres volt, fizetendő {szoba.ar} Ft a helyszínen. Köszönjük hogy minket választott!")
                return
        if not talalat:
            print("Ilyen számú szoba jelenleg nem elérhető.")
            print("Jelenleg elérhető szobáink: ")
            for szoba in self.szobak:
                print(szoba.szobaszam)
    
    
    def lemondas(self, szobaszam, datum):
        if szobaszam in self.foglalasok and datum in self.foglalasok[szobaszam]:
            del self.foglalasok[szobaszam][datum]
            print("A lemondás sikeres volt.")
        else:
            print("Ilyen foglalás nem található a rendszerben.")

    def FoglalasokListazasa(self):
        print("Foglalások:")
        for szobaszam, foglalasok in self.foglalasok.items():
            for datum, nev in foglalasok.items():
                print(f"\tSzoba: {szobaszam}, Dátum: {datum}, Foglaló: {nev}")

    def SzobaInformaciok(self, szobaszam):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                return print(f"Szoba száma: {szoba.szobaszam}, Ár: {szoba.ar}")




def main():
    szalloda = Szalloda("Napsugár szálloda")
    
    for i in range(1, 15):
        szalloda.szoba_hozzáadása(Egyagyas(f"{i}", f"{15470} Ft"))
    for i in range(16, 50):
        szalloda.szoba_hozzáadása(Kétágyas(f"{i}", f"{25470} Ft"))
    
    

    szalloda.foglalas("24", "2024.04.02.", "Antóci Dorottya")
    szalloda.foglalas("32", "2024.04.26.", "Wunderlich József")
    szalloda.foglalas("9", "2024.04.15.", "Csapó Attila")
    szalloda.foglalas("23", "2024.05.17.", "Fesztbaum Béla")
    szalloda.foglalas("10", "2024.05.26.", "Igó éva")

    while True:
        print("\nNapsugár Szálloda")
        print("\nMit szeretne tenni?:")
        print("1. Szoba foglalása")
        print("2. Szoba lemondása")
        print("3. Jelenlegi foglalások listázása")
        print("4. Elérhető szobáink")
        print("5. Kilépés")
        
        valasztas = input("\nMűvelet száma: ")

        if valasztas == "1":
            szobaszam = input("Add meg a foglalni kívánt szoba számát: ")
            datum = input("Add meg a foglalás dátumát (Év.Hónap.Nap. (2024.04.28.) formátumban): ")
            nev = input("Milyen néven foglalnál?: ")
            szalloda.foglalas(szobaszam, datum, nev)
        elif valasztas == "2":
            szobaszam = input("Add meg a lemondani kívánt szoba számát: ")
            datum = input("Add meg a lemondani kívánt foglalás dátumát (Év.Hónap.Nap. (2024.04.28.) formátumban): ")
            szalloda.lemondas(szobaszam, datum)
        elif valasztas == "3":
            szalloda.FoglalasokListazasa()
        elif valasztas == "4":
            MelySzoba=input("Egy- vagy kétágyas szobákat szeretne látni? ")
            if MelySzoba == "1":
                print("Egyágyas szobák:")
                for i in range(1, 15):
                    szalloda.SzobaInformaciok(f"{i}")
            elif MelySzoba == "2":
                print("Kétágyas szobák:")
                for j in range(16, 50):
                    szalloda.SzobaInformaciok(f"{j}")
            else:
                print("Helytelen bevitel")
        elif valasztas == "5":
            print("\nKöszönjük foglalását!")
            break
        else:
            print("A felsorolt műveletek azonosítójából válasszon!")

if __name__ == "__main__":
    main()





