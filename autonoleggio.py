from automobili import Automobili


class Autonoleggio:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.nome = nome
        self.responsabile = responsabile
        self.listaAuto = []

    def aggiornaResponsabile(self,nuovo_responsabile):
        self.responsabile = nuovo_responsabile

    def carica_file_automobili(self, file_path):
        """Carica le auto dal file"""
        # TODO
        file = open(file_path, "r", encoding = "utf-8")
        for line in file:
            auto = line.strip().split(",")
            autom = Automobili(auto[0], auto[1], auto[2], auto[3], auto[4])
            self.listaAuto = autom




    def aggiungi_automobile(self, marca, modello, anno, num_posti):
        """Aggiunge un'automobile nell'autonoleggio: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO
        autom_nuova = Automobili(marca, anno, modello, num_posti)



    def automobili_ordinate_per_marca(self):
        """Ordina le automobili per marca in ordine alfabetico"""
        # TODO

    def nuovo_noleggio(self, data, id_automobile, cognome_cliente):
        """Crea un nuovo noleggio"""
        # TODO


    def termina_noleggio(self, id_noleggio):
        """Termina un noleggio in atto"""
        # TODO
