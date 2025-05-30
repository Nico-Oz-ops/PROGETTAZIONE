from Custom_Types import *
from Insegnamento import *
from Iscrizione import *
from Universita import TipoCorsoDiLaurea


class CorsodiLaurea:
    _codice: str
    _nome: str
    _insegn_cdl: Insegnamento
    _iscrizione: Studente
    _cdl_tipo: TipoCorsoDiLaurea
    
    def __init__(self, codice: str, nome: str, cdl_tipo: TipoCorsoDiLaurea):
        self.setCodice(codice)
        self.setNome(nome)
        self._insegn_cdl = set()
        self._iscrizione = set()
        self.setCdlTipo(cdl_tipo)
    
    def setNome(self, nome: str) -> None:
        self._nome = nome
    
    def setCodice(self, codice: str) -> None:
        self._codice = codice
    
    def add_insegn_cdl(self, insegn_cdl: Insegnamento) -> None:
        self._insegn_cdl.add(insegn_cdl)
    
    def remove_insegn_cdl(self, insegn_cdl: Insegnamento) -> None:
        if len(self._insegn_cdl) >= 1:
            self._insegn_cdl.remove(insegn_cdl)
    
    def add_iscrizione_studente(self, iscrizione: Studente) -> None:
        self._iscrizione.add(iscrizione)
    
    def remove_iscrizione_studente(self, iscrizione: Studente) -> None:
        if len(self._iscrizione) >= 1:
            self._iscrizione.remove(iscrizione)
    
    def setCdlTipo(self, cdl_tipo: TipoCorsoDiLaurea) -> None:
        self._cdl_tipo = cdl_tipo
    
    def getNome(self) -> str:
        return self._nome
    
    def getCodice(self) -> str:
        return self._codice
    
    def getInsegnCdl(self) -> frozenset[Insegnamento]:
        return frozenset(self._insegn_cdl)
    
    def getIscrizione(self) -> frozenset[Studente]:
        return frozenset(self._iscrizione)
    
    def getCdlTipo(self) -> TipoCorsoDiLaurea:
        return self._cdl_tipo

        
