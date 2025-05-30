from Custom_Types import *
from datetime import *


class Direttore:

    _cf: CodiceFiscale # <<imm>>
    _nome: str
    _cognome: str
    _data_nascita: datetime.date # <imm>>
    _anni_servizio: IntGEZ

    def __init__(self, cf: CodiceFiscale, nome: str, cognome: str, data_nascita: datetime.date, anni_servizio: IntGEZ):
        self._cf = cf
        self.setNome(nome)
        self.setCognome(cognome)
        self._data_nascita = data_nascita
        self.setAnniServizio(anni_servizio)
    
    def setNome(self, nome: str) -> None:
        self._nome = nome
    
    def setCognome(self, cognome: str) -> None:
        self._cognome = cognome

    def setAnniServizio(self, anni_servizio: IntGEZ) -> None:
        self._anni_servizio = anni_servizio
    
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
        
