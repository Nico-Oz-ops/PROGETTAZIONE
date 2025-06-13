from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Professore import Professore
    from Studente import Studente
    from Regione import Regione


class Citta:
    _nome: str
    _prof_citta_nasc: 'Professore'
    _stud_citta_nasc: 'Studente'
    _citta_reg: 'Regione'

    def __init__(self, nome: str, citta_reg: 'Regione'):

        self.setNome(nome)
        self._prof_citta_nasc = set()
        self._stud_citta_nasc = set()
        self.setCittaReg(citta_reg)

    def setNome(self, nome: str) -> None:
        self._nome = nome
    
    def add_prof_citta_nasc(self, prof_citta_nasc: 'Professore') -> None:
        self._prof_citta_nasc.add(prof_citta_nasc)
    
    def remove_prof_citta_nasc(self, prof_citta_nasc: 'Professore') -> None:
        if len(self._prof_citta_nasc) >= 1:
            self._prof_citta_nasc.remove(prof_citta_nasc)
    
    def add_stud_citta_nasc(self, stud_citta_nasc: 'Studente') -> None:
        self._stud_citta_nasc.add(stud_citta_nasc)
    
    def remove_stud_citta_nasc(self, stud_citta_nasc: 'Studente') -> None:
        if len(self._stud_citta_nasc) >= 1:
            self._stud_citta_nasc.remove(stud_citta_nasc)
    
    def setCittaReg(self, citta_reg: 'Regione') -> None:
        self._citta_reg = citta_reg
    
    def getNome(self) -> str:
        return self._nome
    
    def getProfCittaNasc(self) -> frozenset['Professore']:
        return frozenset(self._prof_citta_nasc)
    
    def getStudCittaNasc(self) -> frozenset['Studente']:
        return frozenset(self._stud_citta_nasc)
    
    def getCittaReg(self) -> 'Regione':
        return self._citta_reg

        