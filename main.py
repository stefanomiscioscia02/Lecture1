# Recap Lezioni con modifiche nel programma Lecture 1
# Lezione 1 -> Banale lezione su Classi, print ecc.
# Lezione 2 -> Attributi con _ e __ seguiti dai Getter e Setter
# Lezione 3 -> + Metodi dunder __str__, __repr__, ecc.
#              + Inheritance -> due sottoclassi di prodotto(ProdottoScontato, Servizio) -> 3 metodi prezzo_finale
#              + Polimorfismo
#              + Duck typing
#              + Dataclass
#              + Moduli
from gestionale.vendite.ordini import Ordine, RigaOrdine, OrdineConSconto
from gestionale.core.prodotti import Prodotto, crea_prodotto_standard, ProdottoRecord
from gestionale.core.clienti import Cliente, ClienteRecord
import networkx as nx

print("\n----------------------------------------------")
print("--------- Classe Prodotto con Moduli ---------")
print("----------------------------------------------\n")
p1 = Prodotto("Monitor", 600, quantity=1, supplier="AAA")
p2 = crea_prodotto_standard("Tablet", 750)
print(p1)
print(p2)

print("\n-----------------------------------------------")
print("---------- Classe Cliente con Moduli ----------")
print("-----------------------------------------------\n")

c1 = Cliente("Mario Rossi", "mail@mail.com", "Silver")
print(c1)

# Modi per importare
# 1) from prodotti import ProdottoScontato -> p2 = PrdottoScontato(name="Auricolari"...)
# 2) from prodotti import ProdottoScontato as ps (rinomino l'oggetto) -> p3 = ps(name="Auricolari"...)
# 3) import prodotti (importa tutto dentro il main) -> p4 = prodotti.ProdottoScontato(name="Auricolari"...)
# 4) import prodotti as p (come il 3 ma con prodotti rinominato) -> p5 = p.ProdottoScontato(name="Auricolari"...)


print("\n-----------------------------------------------")
print("----------------- DATACLASSES -----------------")
print("-----------------------------------------------\n")


cliente1 = ClienteRecord(name="Mario Rossi", mail="mariorossi@example.com", livello="Gold")

prodotto1 = ProdottoRecord("Laptop", 1200.0 )
prodotto2 = ProdottoRecord("Mouse", 20.0 )

ordine = Ordine([RigaOrdine(prodotto1, 2), RigaOrdine(prodotto2, 10)], cliente1)

for j in range(ordine.numero_ordini()):
    print(f"Ordine {j+1}: {ordine.righe[j]}")
print("Numero di righe:", {ordine.numero_ordini()})
print(f"Totale netto:", ordine.totale_netto())
print("Totale lordo (IVA 22%):", ordine.totale_lordo(0.22))

ordine_scontato = OrdineConSconto([RigaOrdine(prodotto1, 2), RigaOrdine(prodotto2, 10)], cliente1, 0.1)

print(ordine_scontato)
print(f"Totale netto:", ordine_scontato.totale_netto())
print("Totale lordo (IVA 22%):", ordine_scontato.totale_lordo(0.22))

# Nel package gestionale, scriviamo un modulo fatture.py che contenga:
# - una classe fattura che contiene un ordine, numero fattura e una data
# - un metodo genera fattura che restituisce una stringa formattata con tutte le info della fattura
