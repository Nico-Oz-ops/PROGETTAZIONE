from Custom_types import *
from __future__ import annotations

class Impiegato:
    _nome: str # noto alla nascita
    _cognome: str # noto alla nascita
    _nascita: date # immutabile, noto alla nascita
    _stipendio: Importo # noto alla nascita
    _afferenza: afferenza # da assoc. 'afferenza' [1..1]

    def __init__(self, nome, cognome, nascita, stipendio, dipartimento_aff: Dipartimento | None = None, data_afferenza: date | None = None) -> None:

        self.set_nome(nome)
        self.set_cognome(cognome)
        self.nascita = nascita
        self.set_stipendio(stipendio)
        self.set_dipartimento(dipartimento_aff, data_afferenza)

        if (dipartimento_aff is None) != (data_afferenza is None):
            raise ValueError("Dipartimento e data di afferenza devono essere entrambi None o entrambi non None")
        self.set_dipartimento(dipartimento_aff)
        self._set_data_afferenza(data_afferenza)

    def nome(self) -> str:
        return self._nome
    
    def cognome(self) -> str:
        return self._cognome
    
    def set_nome(self, nome: str):
        self._nome = nome
    
    def set_cognome(self, cognome: str):
        self._cognome = cognome
    
    def nascita(self) -> date:
    
    def stipendio(self) -> Importo:
        return self._stipendio

    def set_stipendio(self, stipendio: Importo) -> None:
        self._stipendio = stipendio
    
    def __str__(self):
        afferenza: str = f"che afferisce al dip. {self.dipartimento().nome()}" if self._dipartimento_afferneza else ""
        return f"Impiegato: {self.nome()} {self.cognome()} {afferenza}"

class Dipartimento:
    _nome: str
    _telefono: Telefono
    _impiegati: set[_afferenza] # certamente non noti alla nascita

    def __init__(self, nome: str, telefono: Telefono):
        self.set_nome(nome)
        self.set_telefono(telefono)


class afferenza:
    _impiegato: Impiegato # ovviamente noto alla nascita
    _dipartimento: Dipartimento # ovviamente noto alla nascita
    _data_afferenza: datetime.date # noto alla nascita, immutabile

    def impiegato(self) -> Impiegato:
        return self.impiegato
    
    def dipartimento(self) -> Dipartimento:
        return self.dipartimento
    
    def data_afferenza(self) -> date:
        return self.data_afferenza
    
    def __init__(self, impiegato, dipartimento, data_afferenza):
    
    def __hash__(self):
        pass
    
    def __eq__(self, value):
        pass
