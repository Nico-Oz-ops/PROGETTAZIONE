from typing import TYPE_CHECKING
from Custom_Types import *
if TYPE_CHECKING:
    from CorsoDiLaurea import CorsodiLaurea

class Insegnamento:
    _nome: str 
    _n_ore: IntGEZ
    _codice: str
    _insegn_cdl: set

    def __init__(self, nome: str, n_ore: IntGEZ, codice: str, insegn_cdl: 'CorsodiLaurea'):
        self.setNome(nome)
        self.setNumOre(n_ore)
        self.setCodice(codice)
        self._insegn_cdl = set()
        self.add_insegn_cdl(insegn_cdl)
    
    def setNome(self, nome: str) -> None:
        self._nome = nome
    
    def setNumOre(self, n_ore: IntGEZ) -> None:
        self._n_ore = n_ore
    
    def setCodice(self, codice: str) -> None:
        self._codice = codice
    
    def add_insegn_cdl(self, insegn_cdl: 'CorsodiLaurea') -> None:
        self._insegn_cdl.add(insegn_cdl)
    
    def remove_insegn_cdl(self, insegn_cdl: 'CorsodiLaurea') -> None:
        if len(self._insegn_cdl) < 1:
            raise RuntimeError("Errore, ci deve essere almeno un insegnamento per il Corso di Laurea")
        else:
            self._insegn_cdl.remove(insegn_cdl)

    def getNome(self) -> str:
        return self._nome
    
    def getNumOre(self) -> IntGEZ:
        return self._n_ore
    
    def getCodice(self) -> str:
        return self._codice
    
    def getInsegnCdl(self) -> frozenset['CorsodiLaurea']:
        return frozenset(self._insegn_cdl)
        
