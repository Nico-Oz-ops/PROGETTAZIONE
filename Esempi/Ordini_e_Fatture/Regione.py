from Nazione import Nazione
from Citta import Citta

class Regione:

    _nome: str
    _reg_naz: Nazione
    _cit_reg: Citta

    def __init__(self, nome: str, reg_naz: Nazione):

        self.setNome(nome)
        self.setRegNaz(reg_naz)
        self._cit_reg = set()
    
    def setNome(self, nome: str) -> None:
        self._nome = nome
    
    def setRegNaz(self, reg_naz: Nazione) -> None:
        self._reg_naz = reg_naz
    
    def add_cit_reg(self, cit_reg: Citta) -> None:
        self._cit_reg = cit_reg
    
    def remove_cit_reg(self, cit_reg: Citta) -> None:
        if len(self._cit_reg) >= 1:
            self._cit_reg.remove(cit_reg)
    
    def getNome(self) -> str:
        return self._nome
    
    def getRegNaz(self) -> Nazione:
        return self._reg_naz
    
    def getCitReg(self) -> frozenset[Citta]:
        return self._cit_reg
        