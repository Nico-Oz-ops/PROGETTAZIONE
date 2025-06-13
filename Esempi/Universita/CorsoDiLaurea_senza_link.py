from Custom_Types import *
from Insegnamento import *
from Iscrizione import *
from TipoCorsoDiLaurea import *
from Studente import *


class CorsodiLaurea:
    _codice: str
    _nome: str
    _insegn_cdl: Insegnamento
    _stud_iscritti: dict[Studente, date]
    _cdl_tipo: TipoCorsoDiLaurea
    
    def __init__(self, codice: str, nome: str, cdl_tipo: TipoCorsoDiLaurea):
        self.setCodice(codice)
        self.setNome(nome)
        self._insegn_cdl = set()
        self._stud_iscritti = dict()
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

    def add_stud_iscritti(self, studente: Studente, data: date) -> None:
        if studente in self._stud_iscritti:
            raise ValueError(f"Errore, lo studente '{studente.nome()}' è stato iscritto il '{self._stud_iscritti[studente]}' al corso di laurea.")
        self._stud_iscritti[studente] = data
    
    def remove_stud_iscritti(self, studente: Studente) -> None:
        if not studente in self._stud_iscritti:
            raise ValueError(f"Errore, lo studente '{studente.nome()}' non fa parte di questo corso di laurea.")
        del self._stud_iscritti[studente]

    def __contains__(self, item: Any) -> bool:
        if type(item) != Studente:
            return False
        return item in self._stud_iscritti
    
    def setCdlTipo(self, cdl_tipo: TipoCorsoDiLaurea) -> None:
        self._cdl_tipo = cdl_tipo
    
    def getNome(self) -> str:
        return self._nome
    
    def getCodice(self) -> str:
        return self._codice
        
    def getStudentiIscritti(self) -> frozenset[tuple[Studente, date]]:
        return frozenset((stud, data) for stud, data in self._stud_iscritti.items())
    
    def getInsegnCdl(self) -> frozenset[Insegnamento]:
        return frozenset(self._insegn_cdl)
    
    def getIscrizione(self) -> frozenset[Studente]:
        return frozenset(self._iscrizione)
    
    def getCdlTipo(self) -> TipoCorsoDiLaurea:
        return self._cdl_tipo
