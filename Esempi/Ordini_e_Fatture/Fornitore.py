from Custom_Types import *

class Fornitore:
    _ragione_sociale: str
    _partita_iva: PartitaIVA # <<imm>>
    _indirizzo: Indirizzo
    _telefono: Telefono
    _email: Email

    def __init__(self, ragione_sociale: str, partita_iva: PartitaIVA, indirizzo: Indirizzo, telefono: Telefono, email: Email):
        self.setRagioneSociale(ragione_sociale)
        self._partita_iva = partita_iva
        self.setIndirizzo(indirizzo)
        self.setTelefono(telefono)
        self.setEmail(email)
    
    def setRagioneSociale(self, ragione_sociale: str) -> None:
        self._ragione_sociale = ragione_sociale
    
    def setIndirizzo(self, indirizzo: Indirizzo) -> None:
        self._indirizzo = indirizzo
    
    def setTelefono(self, telefono: Telefono) -> None:
        self._telefono = telefono
    
    def setEmail(self, email: Email) -> None:
        self._email = email
    
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
        