import flet as ft

class Controller:
    def __init__(self, v):
        self._view = v

    def add_ordine(self):

        #Prodotto
        nomePstr = self._view._txtInNomeP.value()
        try:
            prezzoPstr = float(self._view._txtPrezzo.value())
            quantita = int(self._view.txtQuantita.value())
        except ValueError:
            self._view._lvOut.controls.append(
                ft.Text("Attenzione! Il prezzo deve essere un numero con virgola"),
                color="Red")
            self._view.update()
            return


    def gestisci_ordine(self):
        pass

    def gestisci_all_ordini(self):
        pass

    def stampa_sommario(self):
        pass

