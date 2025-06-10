import re
from typing import Self
from datetime import *

class Importo(float):

    def __new__(cls, v:int | float | str) -> Self:
        if v < 0:
            raise ValueError(f"Value v == {v} must be >= 0")
        return float.__new__(cls, v)
    
class Telefono(str):

    def __new__(cls, v: str) -> Self:
        
        if not re.fullmatch(r'^\+?[0-9]+', v):
            raise ValueError(f"Value v == {v} does not satisfy the standard")
        return super().__new__(cls, v)

class Dipartimento:
    _nome: str
    _telefono: Telefono

class Impiegato:
    _nome: str
    _cognome: str
    _nascita: datetime.date
    _stipendio: Importo
    _afferenza: Dipartimento

    def nome(self) -> str:
        return self._nome
    
    def cognome(self) -> str:
        return self._cognome
    
    def nascita(self) -> datetime.date:
        return self._nascita
    
    def stipendio(self) -> Importo:
        return self._stipendio
    
    def set_nome(self, nome: str) -> None:
        self._nome = nome
    
    def set_cognome(self, cognome: str) -> None:
        self._cognome = cognome
    
    def set_nascita(self, nascita: datetime.time) -> None:
        self._nascita = nascita
    
    def set_stipendio(self, stipendio: Importo) -> None:
        self._stipendio = stipendio
    
    def set_afferenza(self, dipartimento: Dipartimento, data: datetime.date):
        l = afferenza(self, dipartimento, data)
    

    def __init__(self, nome: str, cognome: str, nascita: datetime.date, stipendio: Importo, afferenza: afferenza):
        self.set_nome(nome)
        self.set_cognome(cognome)
        self.set_stipendio(stipendio)
        self._nascita = nascita
    

