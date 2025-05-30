from Custom_Types import *
from datetime import *
from Universita import CorsodiLaurea
from Insegnamento import *
from Citta import Citta

class Studente:
    _nome: str 
    _cognome: str
    _data_nascita: datetime.date #<<imm>>
    _codice_fiscale: CodiceFiscale #<<imm>>
    _codice_matricola: IntGEZ #<<imm>>
    _insegn_superato: Insegnamento
    _iscrizione: CorsodiLaurea
    _stud_citta_nasc: Citta

    def __init__(self, nome: str, cognome: str, data_nascita: datetime.date, codice_fiscale: CodiceFiscale, codice_matricola: IntGEZ, iscrizione: CorsodiLaurea, stud_citta_nasc: Citta):
        self.setNome(nome)
        self.setCognome(cognome)
        self._data_nascita = data_nascita
        self._codice_fiscale = codice_fiscale
        self._codice_matricola = codice_matricola
        self._insegn_superato = set()
        self._iscrizione = iscrizione
        self._stud_citta_nasc = stud_citta_nasc
    
    def setNome(self, nome: str) -> None:
        self._nome = nome    
    
    def setCognome(self, cognome: str) -> None:
        self._cognome = cognome
    
    def getDataNascita(self) -> datetime.date:
        return self._data_nascita
    
    def getCodiceFiscale(self) -> CodiceFiscale:
        return self._codice_fiscale
    
    def getCodiceMatricola(self) -> IntGEZ:
        return self._codice_matricola
    
    def add_insegn_superato(self, corso_sup: Insegnamento) -> None:
        self._insegn_superato.add(corso_sup)
    
    def getInsegnSuperato(self) -> frozenset[Insegnamento]:
        return frozenset(self._insegn_superato)
    
    def getIscrizione(self) -> CorsodiLaurea:
        return self._iscrizione
    
    def getStudCittaNasc(self) -> Citta:
        return self._stud_citta_nasc




        
