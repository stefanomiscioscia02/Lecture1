# Nel package gestionale, scriviamo un modulo fatture.py che contenga:
# - una classe fattura che contiene un ordine, numero fattura e una data
# - un metodo genera fattura che restituisce una stringa formattata con tutte le info della fattura
from datetime import date

from gestionale.core.clienti import ClienteRecord
from gestionale.core.prodotti import ProdottoRecord
from gestionale.vendite.ordini import Ordine, RigaOrdine
from dataclasses import dataclass

@dataclass
class Fattura:
    ordine: Ordine
    numero_fattura: str
    data: date

    def genera_fattura(self):
        linee = [
            f"="*60,
            f"Fattura no.{self.numero_fattura} del {self.data}",
            f"=" * 60,
            f"Cliente: {self.ordine.cliente.name}\nCategoria: {self.ordine.cliente.livello}\nMail: {self.ordine.cliente.mail}",
            f"-" * 60,
            f"DETTAGLIO ORDINE"
        ]
        for i, riga in enumerate(self.ordine.righe, 1):
            linee.append(f"{i}"
                         f" {riga.prodotto.name} - "
                         f"Q.ta {riga.quantita} x {riga.prodotto.prezzo_unitario} - "
                         f"Tot. {riga.totale_riga()}")
        linee.extend([
            f"-" * 60,
            f"Totale netto: {self.ordine.totale_netto()}",
            f"IVA(22%): {self.ordine.totale_netto()*0.22}",
            f"Totale lordo: {self.ordine.totale_lordo(0.22)}",
            f"=" * 60]
        )

        return "\n".join(linee)

def _test_modulo():
    p1 = ProdottoRecord("Laptop", 1200.0)
    p2 = ProdottoRecord("Mouse", 20)
    p3 = ProdottoRecord("Tablet", 600.0)
    cliente = ClienteRecord("Mario Bianchi", "mail@gmail.com", "Gold")
    ordine = Ordine(righe = [RigaOrdine(p1,1), RigaOrdine(p2, 5), RigaOrdine(p3, 2)], cliente = cliente)
    fattura = Fattura(ordine, "2026/01", date.today())

    print(fattura.genera_fattura())

if __name__ == "__main__":
    _test_modulo()