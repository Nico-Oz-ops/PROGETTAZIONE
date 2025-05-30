from Custom_Types import *
from datetime import *
from Insegnamento import *
from Universita import Citta

class Professore:
    _nome: str 
    _cognome: str
    _data_nascita: datetime.date #<<imm>>
    _codice_fiscale: CodiceFiscale #<<imm>>
    _prof_insegna_ins: Insegnamento
    _prof_citta_nasc: Citta

    def __init__(self, nome: str, cognome: str, data_nascita: datetime.date, codice_fiscale: CodiceFiscale, codice_matricola: IntGEZ, prof_citta_nasc: Citta):
        self.setNome(nome)
        self.setCognome(cognome)
        self._data_nascita = data_nascita
        self._codice_fiscale = codice_fiscale
        self._codice_matricola = codice_matricola
        self._prof_insegna_ins = set()
        self._prof_citta_nasc = prof_citta_nasc
    
    def setNome(self, nome: str) -> None:
        self._nome = nome    
    
    def setCognome(self, cognome: str) -> None:
        self._cognome = cognome
    
    def add_prof_insegna_ins(self, prof_insegna_ins: Insegnamento) -> None:
        self._prof_insegna_ins.add(prof_insegna_ins)
    
    def remove_prof_insegna_ins(self, prof_insegna_ins: Insegnamento) -> None:
        if len(self._prof_insegna_ins) >= 1:
            self._prof_insegna_ins.remove(prof_insegna_ins)
    
    def getProfCittaNasc(self) -> Citta:
        return self._prof_citta_nasc
    
    def getDataNascita(self) -> datetime.date:
        return self._data_nascita
    
    def getCodiceFiscale(self) -> CodiceFiscale:
        return self._codice_fiscale
    
    def getProfInsegnaIns(self) -> frozenset[Insegnamento]:
        return frozenset(self._prof_insegna_ins)
