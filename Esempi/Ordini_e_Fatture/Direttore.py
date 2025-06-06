from Custom_Types import *
from datetime import *
from Citta import Citta
from Dipartimento import Dipartimento


class Direttore:

    _cf: CodiceFiscale # <<imm>>
    _nome: str
    _cognome: str
    _data_nascita: datetime.date # <imm>>
    _anni_servizio: IntGEZ
    _cit_nasc: Citta
    _dirige: Dipartimento

    def __init__(self, cf: CodiceFiscale, nome: str, cognome: str, data_nascita: datetime.date, anni_servizio: IntGEZ, cit_nasc: Citta):
        self._cf = cf
        self.setNome(nome)
        self.setCognome(cognome)
        self._data_nascita = data_nascita
        self.setAnniServizio(anni_servizio)
        self._cit_nasc = cit_nasc
        self._dirige = set()
    
    def setNome(self, nome: str) -> None:
        self._nome = nome
    
    def setCognome(self, cognome: str) -> None:
        self._cognome = cognome

    def setAnniServizio(self, anni_servizio: IntGEZ) -> None:
        self._anni_servizio = anni_servizio
    
    def add_dirige(self, dirige: Dipartimento) -> None:
        self._dirige.add(dirige)
    
    def remove_dirige(self, dirige: Dipartimento) -> None:
        if len(self._dirige) >= 1:
            self._dirige.remove(dirige)
    
    def getCodiceFiscale(self) -> CodiceFiscale:
        return self._cf
    
    def getDataNascita(self) -> datetime.date:
        return self._data_nascita
    
    def getNome(self) -> str:
        return self._nome
    
    def getCognome(self) -> str:
        return self._cognome
    
    def getAnniServizio(self) -> IntGEZ:
        return self._anni_servizio
    
    def getCitNasc(self) -> Citta:
        return self._cit_nasc
    
    def getDirige(self) -> frozenset[Dipartimento]:
        return frozenset(self._dirige)

        
