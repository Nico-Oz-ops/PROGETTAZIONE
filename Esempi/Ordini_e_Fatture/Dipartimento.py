from Custom_Types import *
from Direttore import Direttore
from Ordine import Ordine

class Dipartimento:
    _nome: str
    _indirizzo: Indirizzo
    _dirige: Direttore
    _dip_ordine: Ordine

    def __init__(self, nome: str, indirizzo: Indirizzo, dirige: Direttore):
        self.setNome(nome)
        self.setIndirizzo(indirizzo)
        self.setDirige(dirige)
        self._dip_ordine = set()
    
    def setNome(self, nome: str) -> None:
        self._nome = nome
    
    def setIndirizzo(self, indirizzo: Indirizzo) -> None:
        self._indirizzo = indirizzo
    
    def setDirige(self, dirige: Direttore) -> None:
        self._dirige = dirige
    
    def add_dip_ordine(self, dip_ordine: Ordine) -> None:
        self._dip_ordine.add(dip_ordine)
    
    def remove_dip_ordine(self, dip_ordine: Ordine) -> None:
        if len(self._dip_ordine) >= 1:
            self._dip_ordine.remove(dip_ordine)

    def getNome(self) -> str:
        return self._nome
    
    def getIndirizzo(self) -> Indirizzo:
        return self._indirizzo
    
    def getDirige(self) -> Direttore:
        return self._dirige
    
    def getDipOrdine(self) -> frozenset[Ordine]:
        return frozenset(self._dip_ordine)
