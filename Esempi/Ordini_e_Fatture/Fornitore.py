from Custom_Types import *
from Ordine import Ordine

class Fornitore:
    _ragione_sociale: str
    _partita_iva: PartitaIVA # <<imm>>
    _indirizzo: Indirizzo
    _telefono: Telefono
    _email: Email
    _forn_ord: Ordine

    def __init__(self, ragione_sociale: str, partita_iva: PartitaIVA, indirizzo: Indirizzo, telefono: Telefono, email: Email):
        self.setRagioneSociale(ragione_sociale)
        self._partita_iva = partita_iva
        self.setIndirizzo(indirizzo)
        self.setTelefono(telefono)
        self.setEmail(email)
        self._forn_ord = set()
    
    def setRagioneSociale(self, ragione_sociale: str) -> None:
        self._ragione_sociale = ragione_sociale
    
    def setIndirizzo(self, indirizzo: Indirizzo) -> None:
        self._indirizzo = indirizzo
    
    def setTelefono(self, telefono: Telefono) -> None:
        self._telefono = telefono
    
    def setEmail(self, email: Email) -> None:
        self._email = email
    
    def add_forn_ord(self, forn_ord: Ordine) -> None:
        self._forn_ord.add(forn_ord)
    
    def remove_forn_ord(self, forn_ord: Ordine) -> None:
        if len(self._forn_ord) >= 1:
            self._forn_ord.remove(forn_ord)
    
    def getRagioneSociale(self) -> str:
        return self._ragione_sociale
    
    def getPartitaIVA(self) -> PartitaIVA:
        return self._partita_iva
    
    def getIndirizzo(self) -> Indirizzo:
        return self._indirizzo
    
    def getTelefono(self) -> Telefono:
        return self._telefono
    
    def getEmail(self) -> Email:
        return self._email
    
    def getFornOrd(self) -> frozenset[Ordine]:
        return frozenset(self._forn_ord)
        