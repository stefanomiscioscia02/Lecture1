# Scriviamo un codice python che modelli un semplice
# gestionale aziendale. Dovremo prevedere la possibilità di
# definire entità che modellano i prodotti, i clienti,
# offrire interfacce per calcolare i prezzi, eventualmente
# scontati, ...
from dataclasses import dataclass


# Si modifichi la classe cliente in maniera tale che la proprietà categoria sia "protetta"
# e accetti solo (Gold, Silver, Bronze)

class Prodotto:
    aliquota_iva = 0.22 #variabile di classe -> è lastessa per tutte le sitanze che verrano create

    def __init__(self, name:str, price:float, quantity:int, supplier = None):
        self.name = name
        self._price = None # Per rendere un pò più privata la variabile mettiamo _ davanti la variabile. Anche __
        self.price = price
        self.quantity = quantity
        self.supplier = supplier

    @property
    def price(self): # eq. GETTER
        return self._price

    @price.setter
    def price(self, valore):
        if valore < 0:
            raise ValueError("Valore negativo")
        self._price = valore

    def __str__(self):
        return f"{self.name} - disponibili: {self.quantity} pezzi al prezzo di : {self.price} $ "

    def __repr__(self):
        return f"Prodotto(name = {self.name}, price = {self.price}, quantity = {self.quantity}, supplier = {self.supplier})"

    def __eq__(self, other: object):
        if not isinstance(other, Prodotto):
            return NotImplemented
        return (self.name == other.name
                and self.price == other.price
                and self.quantity == other.quantity
                and self.supplier == other.supplier)

    def __lt__(self, other: "Prodotto") -> bool:
        return self.price < other.price

    @classmethod
    def costruttore_con_quantità_uno(cls, name: str, price: float, supplier: str):
        return cls(name, price, quantity = 1, supplier = supplier)

    @staticmethod
    def applica_sconto(prezzo, percentuale):
        return prezzo*(1-percentuale)

    def valore_netto(self):
        return self._price * self.quantity

    def valore_lordo(self):
        netto = self.valore_netto()
        lordo = netto*(1-self.aliquota_iva)
        return lordo

    def prezzo_finale(self):
        return self._price * (1+self.aliquota_iva)

MAX_QUANTITA = 1000
def crea_prodotto_standard(nome: str, prezzo: float):
    return Prodotto(nome, prezzo, quantity=1, supplier=None)

class ProdottoScontato(Prodotto): # sottoclasse di Prodotto
    def __init__(self, name:str, price:float, quantity:int, supplier: str, sconto_percentuale: float):
        #Prodotto.__init__
        super().__init__(name, price, quantity, supplier)
        self.sconto_percentuale = sconto_percentuale

    def prezzo_finale(self) -> float:
        return self.valore_lordo()*(1-self.sconto_percentuale/100)

class Servizio(Prodotto):
    def __init__(self, name:str, tariffa_oraria: float, ore: int):
        super().__init__(name, tariffa_oraria, quantity=1, supplier=None)
        self.ore = ore

    def prezzo_finale(self) -> float:
        return self.price * self.ore

# --- Esercizio lezione 02.03.2026 ---
# Definire una classe abbonamento che  abbia come attributi: "Nome, prezzo mensile, mesi".
# Abbonnamento dovrà avere un metodo per calcolare il prezzo finale ottenuto come prezzo_mensile*mesi
class Abbonamento:
    def __init__(self, name:str, prezzo_mensile: float, mesi: int):
        self.name = name
        self.prezzo_mensile = prezzo_mensile
        self.mesi = mesi

    def prezzo_finale(self) -> float:
        return self.prezzo_mensile*self.mesi

# Dataclass
@dataclass
class ProdottoRecord:
    name: str
    prezzo_unitario: float
#----------------------------------------------------------------------------------------------------------------
def _test_modulo():
    print("\n---------------------------------------------")
    print("------ Sto testando il modulo prodotti ------")
    print("---------------------------------------------\n")
    myproduct1 = Prodotto( name="Laptop", price=1200.0, quantity=12, supplier="ABC")
    print(f"Nome prodotto: {myproduct1.name} - prezzo: {myproduct1.price}")
    print(f"Prezzo scontato di myproduct1 {Prodotto.applica_sconto(myproduct1.price, 0.15)}") #modo per chiamare un metodo statico

    print(f"Il totale lordo del mio prodotto {myproduct1.valore_lordo()}") #uso in metodo di instanza
    Prodotto.aliquota_iva = 0.24
    print(f"Il totale lordo del mio prodotto {myproduct1.valore_lordo()}")

    myproduct3 = Prodotto.costruttore_con_quantità_uno(name="Auricolari", price=200.0, supplier="ABC") #modo per chiamare un metodo di classe
    print(myproduct3) #Stampa con il metodo __str__

    myproduct2 = Prodotto( name="Mouse", price=200, quantity=5, supplier="DEF")
    print(f"Nome prodotto: {myproduct2.name} - prezzo: {myproduct2.price}")

    p_a = Prodotto(name="Laptop", price=1200.0, quantity=12, supplier="ABC" )
    p_b = Prodotto(name="Mouse", price=10, quantity=14, supplier="CDE" )
    print("myproduct1 == p_a?", myproduct1 == p_a) # va a achiamare il metodo __eq__ appena implementato. Mi aspetto -> TRUE
    print("p_a == p_b", p_a == p_b) # Mi aspetto -> FALSE
    mylist = [p_a, p_b, myproduct1]
    mylist.sort()
    print(f"lista di prodotti ordinata: ")
    for p in mylist:
        print(f"- {p}")

    myProdScontato = ProdottoScontato(name="Auricolari", price=320.0, quantity=1, supplier="ABC", sconto_percentuale=10)
    myService = Servizio(name="Consulenza", tariffa_oraria=100, ore=3)
    mylist.sort(reverse=True)
    mylist.append(myProdScontato)
    mylist.append(myService)

    for a in mylist:
        print(a.name, "->", a.prezzo_finale())

    myPass = Abbonamento(name="Spotify", prezzo_mensile=20.99, mesi=12)
    mylist.append(myPass)


    for elem in mylist: # Ducktyping
        print(elem.name, "->", elem.prezzo_finale())

    def calcola_totale(elementi): # Ducktyping
        tot = 0
        for e in elementi:
            tot += e.prezzo_finale()
        return tot

    print(f"Il totale è: {calcola_totale(mylist)} ")

    from typing import Protocol

    class HaPrezzoFinale(Protocol): #rivedere lezione 3 minuto 1.12.00 circa
        def prezzo_finale(self) -> float:
            ... # equivalente a pass -> differenza con pass(con pass scrivo qualosa) mentre i ... qualcosa che implemento dopo

    def calcola_totale(elementi: list[HaPrezzoFinale]) -> float:
        return sum(e.prezzo_finale() for e in elementi)

    print(f"Il totale è: {calcola_totale(mylist)}")

if __name__ == "__main__": # IMPORTANTEEEEE!!!!!!
    _test_modulo()