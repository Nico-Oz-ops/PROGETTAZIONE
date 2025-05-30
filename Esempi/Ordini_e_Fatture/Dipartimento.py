from Custom_Types import *

class Dipartimento:
    _nome: str
    _indirizzo: Indirizzo

    def __init__(self, nome: str, indirizzo: Indirizzo):
        self.setNome(nome)
        self.setIndirizzo(indirizzo)
    
    def setNome(self, nome: str) -> None:
        self._nome = nome
    
    def setIndirizzo(self, indirizzo: Indirizzo) -> None:
        self._indirizzo = indirizzo
    
    def getNome(self) -> str:
        return self._nome
    
    def getIndirizzo(self) -> Indirizzo:
        return self._indirizzo
        