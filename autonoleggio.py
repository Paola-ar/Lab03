import csv

from automobili import Automobili


class Autonoleggio:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.nome = nome
        self.responsabile = responsabile
        self.listaAuto = []
        self.noleggi = {}

    def aggiornaResponsabile(self,nuovo_responsabile):
        self.responsabile = nuovo_responsabile

    def carica_file_automobili(self, file_path):
        """Carica le auto dal file"""
        # TODO
        try :
            file = open(file_path, "r", encoding = "utf-8")
            for i,riga in enumerate(file):
                riga = riga.strip()
                campo = riga.split(",")
                codice = campo[0]
                marca = campo[1]
                modello = campo[2]
                anno_imm = campo[3]
                num_posti = campo[4]
                auto = Automobili(codice, marca, modello, anno_imm, num_posti)
                self.listaAuto.append(auto)
        except FileNotFoundError:
            raise FileNotFoundError



    def aggiungi_automobile(self, marca, modello, anno, num_posti):
        """Aggiunge un'automobile nell'autonoleggio: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO
        if len(self.listaAuto) == 0:
            codice = "A1"
        else:
            ultimo_codice = self.listaAuto[-1].codice
            numero = int(ultimo_codice[1:]) +1
            codice = f"A{numero}"
        autom_nuova = Automobili(codice,marca, anno, modello, num_posti)
        self.listaAuto.append(autom_nuova)
        return autom_nuova



    def automobili_ordinate_per_marca(self):
        """Ordina le automobili per marca in ordine alfabetico"""
        # TODO
        self.listaAuto.sort(key=lambda x: x.marca.lower())
        return self.listaAuto

    def nuovo_noleggio(self, data, id_automobile, cognome_cliente):
        """Crea un nuovo noleggio"""
        # TODO
        auto = None
        for a in self.listaAuto:
            if a.codice == id_automobile:
                auto = a
                break

        if auto is None:
            raise Exception
        if auto.noleggiata:
            raise Exception

        numeri = []
        for k in self.noleggi.keys(): # k = "N1","N2"
            numero = int(k[1:]) # parte dopo "N"
            numeri.append(numero)
        if not numeri:
            nuovo_numero = 1
        else:
            nuovo_numero = max(numeri) + 1

        ID_noleggio = "N" + str(nuovo_numero)

        self.noleggi[ID_noleggio] = (id_automobile, cognome_cliente, data)
        auto.noleggiata = True

        return f"Noleggio {ID_noleggio} :{id_automobile},{cognome_cliente},{data}"



    def termina_noleggio(self, id_noleggio):
        """Termina un noleggio in atto"""
        # TODO

        if id_noleggio in self.noleggi:
            noleggio = self.noleggi[id_noleggio] # tupla contenente id_automobile, cognome_cliente e data
            id_auto = noleggio[0]
            cognome_cliente = noleggio[1]
            data_noleggio = noleggio[2]

            del self.noleggi[id_noleggio]

            auto = None
            for a in self.listaAuto:
                if a.codice == id_auto:
                    auto = a
                    break
            if auto is not None:
                auto.noleggiata = False
        else:
            raise Exception
