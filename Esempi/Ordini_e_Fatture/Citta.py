from Regione import Regione
from Direttore import Direttore


class Citta:

    _nome: str
    _cit_reg: Regione
    _cit_nasc: Direttore

    def __init__(self, nome: str, cit_reg: Regione):

        self.setNome(nome)
        self.setCitReg(cit_reg)
        self._cit_nasc = set()
    
    def setNome(self, nome: str) -> None:
        self._nome = nome
    
    def setCitReg(self, cit_reg: Regione) -> None:
        self._cit_reg = cit_reg
    
    def add_cit_nasc(self, cit_nasc: Direttore) -> None:
        self._cit_nasc = cit_nasc
    
    def remove_cit_nasc(self, cit_nasc: Direttore) -> None:
        if len(self._cit_nasc) >= 1:
            self._cit_nasc.remove(cit_nasc)
    
    def getNome(self) -> str:
        return self._nome

    def getCitReg(self) -> Regione:
        return self._cit_reg
    
    def getCitNasc(self) -> frozenset[Direttore]:
        return self._cit_nasc
        