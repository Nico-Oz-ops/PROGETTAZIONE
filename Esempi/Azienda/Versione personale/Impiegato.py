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
        self.set_link_afferenza(dipartimento_aff, data_afferenza)

    def set_link_afferenza(self, dipartimento_aff: Dipartimento | None = None, data_afferenza: date | None=None) -> None:
        if (dipartimento_aff is None) != (data_afferenza is None):
            raise ValueError("Dipartimento e data di afferenza devono essere entrambi None o entrambi non None")


        # Se afferiva a un dipartimento, devo rimuoverlo da esso
        try:
            if self.get_link_afferenza():
                self.get_link_afferenza().dipartimento()._remove_impiegato(self.get_link_afferenza())
        except AttributeError:  # il campo _afferenza non era mai stato settato: questo metodo è stato quindi chiamato dal costruttore
            pass

        if dipartimento_aff: # sono entrambi not None
            self._afferenza = _afferenza(impiegato=self, dipartimento=dipartimento_aff, data_afferenza=data_afferenza)
            dipartimento_aff._add_impiegato(self._afferenza)
        else: # sono entrambi None
            self._afferenza = None

    def get_link_afferenza(self) -> _afferenza:
        return self._afferenza

    def nome(self) -> str:
        return self._nome
    
    def cognome(self) -> str:
        return self._cognome
    
    def set_nome(self, nome: str):
        self._nome = nome
    
    def set_cognome(self, cognome: str):
        self._cognome = cognome
    
    def nascita(self) -> date:
        return self._nascita
    
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
    _impiegati: [] # certamente non noti alla nascita

    def __init__(self, nome: str, telefono: Telefono):
        self.set_nome(nome)
        self.set_telefono(telefono)


class _afferenza:
    _impiegato: Impiegato # ovviamente noto alla nascita e immutabile
    _dipartimento: Dipartimento # ovviamente noto alla nascita e immutabile
    _data_afferenza: date # immutabile, noto alla nascita

    def __init__(self, impiegato:Impiegato, dipartimento:Dipartimento, data_afferenza: date) -> None:
        self._impiegato = impiegato
        self._dipartimento = dipartimento
        self._data_afferenza = data_afferenza

    def impiegato(self) -> Impiegato:
        return self._impiegato

    def dipartimento(self) -> Dipartimento:
        return self._dipartimento

    def data_afferenza(self) -> date:
        return self._data_afferenza

    def __hash__(self) -> int:
        return hash((self.impiegato(), self.dipartimento()))

    def __eq__(self, other: Any) -> bool:
        if type(self) != type(other) \
            or hash(self) != hash(other):
            return False
        return (self.impiegato(), self.dipartimento()) == \
            (other.impiegato(), other.dipartimento())