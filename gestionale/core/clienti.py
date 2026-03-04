# --- Esercizio lezione 23.02.2026 ---
# Scrivere una classe Cliente che abbia i campi "nome", "email", "level" (Gold, Silver, Bronze),
# vorremmo che questa classe avesse un metodo che chiamiamo "descrizione"
# che deve restituisce una stringa formattata ad esempio
# "Cliente Fulvio Bianchi (Gold) - fulviobianchi@gmail.com"
from dataclasses import dataclass

categorie_valide = {"Gold", "Silver", "Bronze"} # soluzione molto più pythonic

class Cliente:
    def __init__(self, name:str, mail:str, level:str):
        self.name = name
        self.mail = mail
        self._level = None
        self.level = level

    def descrizione(self):
        return f"Cliente: {self.name} ({self.level}) - {self.mail}"

    @property
    def level(self):
        return self._level
    @level.setter
    def level(self, level):
        if level not in categorie_valide:
            raise ValueError("Livello non valido! Il livello cliente può essere solo Gold, Silver, Bronze")
        self._level = level

    # @level.setter
    # def level(self, categoria): # --> è ok! ma ricorda le parentesi altrimenti il not non funziona su tutta la condizione ma su ogni or
        # if not (categoria == "Gold" or categoria == "Silver" or categoria == "Bronze"):
            # raise ValueError("Il livello cliente può essere solo Gold, Silver, Bronze")
        # self._level = categoria

# ================== DATACLASS ==================
@dataclass
class ClienteRecord:
    name: str
    mail: str
    livello: str
#===========================================================================================================

def _test_modulo():
    print("\n---------------------------------------------")
    print("------ Sto testando il modulo clienti ------")
    print("---------------------------------------------\n")
    cliente1 = Cliente( name="Fulvio Bianchi", mail="fulviobianchi@gmail.com", level="Gold")
    #cliente2 = Cliente( name="Carlo Masone", mail="carlo.masone@gmail.com", level="Platinum")
    print(cliente1.descrizione())

if __name__ == "__main__": # IMPORTANTEEEEE!!!!!!
    _test_modulo()