import copy
from gestionale.core.prodotti import ProdottoRecord

# LISTE
p1 = ProdottoRecord("Laptop", 1200.0)
p2 = ProdottoRecord("Mouse", 20.0)
p3 = ProdottoRecord("Auricolari", 250.0)

carrello = [p1, p2, p3, ProdottoRecord("Tablet", 700.0)]
print("\nProdotti nel carrello")
for i, p in enumerate(carrello,1):
    print(f"{i} {p.name} - {p.prezzo_unitario}")

# Aggiugnere da una lista
carrello.append(ProdottoRecord("Monitor", 1500.0))

carrello.sort(key = lambda x: x.prezzo_unitario, reverse = True)

print("\nProdotti nel carrello: ")
for i, p in enumerate(carrello,1):
    print(f"{i} {p.name} - {p.prezzo_unitario}")

tot = sum([p.prezzo_unitario for p in carrello])
print(f"Totale del carrello: {tot}")

# Aggiungere
carrello.append(ProdottoRecord("Caricatore", 30.0))
carrello.extend([ProdottoRecord("Stampante", 550.0), ProdottoRecord("Telefono", 420.0)])
carrello.insert(2, ProdottoRecord("Powerbank", 50.0)) # -> Aggiugnere in posizione 2

print("\nProdotti nel carrello: ")
for i, p in enumerate(carrello,1):
    print(f"{i} {p.name} - {p.prezzo_unitario}")

# Rimuovere
#carrello.pop() #rimuove l'ultimo elemento
#carrello.pop(2) # rimuove l'elemento in posizione 2
#carrello.remove(p1) # Elimino la prima occorrenza di p1
#carrello.clear # svuota tutta la lista

# Sorting
#carrello.sort() # Ordina seguendo ordinamento naturale
#carrello.sort(reverse = True) # Ordina al contrario
#carrello.sort(key = function)
#carrello_ordinato = sorted(carrello)

# Copie ed altro
#carrello.reverse() # Inverte l'ordine
#carrello_copia = carrello.copy() # Crea una shallow copy
#carrello_copia2 = copy.deepcopy(carrello)

# TUPLE
sede_principale = (45, 8) # lat e long ella sede di torino
sede_milano = (45, 20) #lat e long della sede di milano
print(f"Sede principale lat: {sede_principale[0]}, long: {sede_principale[1]}")

AliquotaIVA = (
    ("Standard", 0.22),
    ("Ridotta", 0.10),
    ("Alimentari", 0.04),
    ("Esente", 0.0)
)
for descr, valor in AliquotaIVA:
    print(f"{descr}: {valor*100}%")

def calcola_statistiche_carrello(carrello):
    """Restituisce prezzo totale, prezzo medio, massimo e minimo"""
    prezzi = [p.prezzo_unitario for p in carrello]
    return (sum(prezzi), sum(prezzi)/len(prezzi), max(prezzi), min(prezzi))

tupla = calcola_statistiche_carrello(carrello)

tot, media, max, min = calcola_statistiche_carrello(carrello) #unpacking tupla

tot, *altri_campi = calcola_statistiche_carrello(carrello)

print(tot)

#SET
categorie = {"Gold", "Silver", "Bronze", "Gold"}
print(categorie)
print(len(categorie))
categorie2 = {"Gold", "Platinum", "Elite"}
# categorie_all = categorie.union(categorie2)
categorie_all = categorie | categorie2
print(categorie_all)

categorie_comuni = categorie & categorie2
print(categorie_comuni)

categorie_esclusive = categorie - categorie2
print(categorie_esclusive)

categorie_esclusive_symm = categorie ^ categorie2
print(categorie_esclusive_symm)

prodotti_ordine_A = {ProdottoRecord("Laptop", 1200.0),
                     ProdottoRecord("Mouse", 20.0),
                     ProdottoRecord("Auricolari", 250.0)}

prodotti_ordine_B = {ProdottoRecord("Laptop2", 1200.0), ProdottoRecord("Mouse2", 20.0),
                     ProdottoRecord("Auricolari2", 250.0)}

#metodi utili per i set
s = set()
s2 = set()
#aggiugere
prodotti_ordine_A. add(ProdottoRecord("Monitor", 1500.0)) # Aggiugnere un elemento
s.update([ProdottoRecord("Laptop", 1200.0), ProdottoRecord("Mouse", 20.0)]) # Aggiungere più elementi

#togliere
s.remove(elem) #rimuovere un elemento. Raise KeyError se non esiste.
s.discard(elem) #rimuovere un elemento, senza "arrabbiarsi" se questo non esiste
s.pop() #rimuove e restituisce un elemento
s.clear() #svuota il set

#operazioni insiemistiche
s.union(s2) # s | s2, ovvero gennereun set che unisce i due set di partenza
s.intersection() # s & s2, ovvero solo elementi comuni
s.differece() # s - s1, elementi di s che non sono contenuti in s1
s.symmetric_difference(s2) # s^ s2, ovvero elementi di s non contenuti in s2 ed elementi di s2 non contenuti in s

s2.issubset() #se gli elementi di s2 sono contenuti in s
s2.issuperset() #se gli elementi di s sono contenuti in s2
s2.isdisjoint() #se gli elementi di s e quelli di s2 sono diversi
