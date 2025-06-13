from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Citta import Citta

class Regione:
    _nome: str
    _citta_reg: Citta

    def __init__(self, nome: str):

        self.setNome(nome)
        self._citta_reg = set()
    
    def setNome(self, nome: str) -> None:
        self._nome = nome
    
    def add_citta_reg(self, citta_reg: Citta) -> None:
        self._citta_reg.add(citta_reg)
    
    def remove_citta_reg(self, citta_reg: Citta) -> None:
        if len(self._citta_reg) >= 1:
            self._citta_reg.remove(citta_reg)
    
    def getNome(self) -> str:
        return self._nome
    
    def getCitta_Reg(self) -> frozenset['Citta']:
        return frozenset(self._citta_reg)