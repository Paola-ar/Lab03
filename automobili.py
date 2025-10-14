class Automobili:
    def __init__(self, codice, marca, modello, anno_imm, num_posti):
        self.codice = codice
        self.marca = marca
        self.modello = modello
        self.anno_imm = anno_imm
        self.num_posti = num_posti
        self.noleggiata = False

    def __str__(self):
        if self.noleggiata:
            stato = "Noleggiata"
        else:
            stato = "Disponibile"
        return f"{self.codice},{self.marca},{self.modello},{self.anno_imm},{self.num_posti},{stato}"


