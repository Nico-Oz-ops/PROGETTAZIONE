from Regione import Regione

class Nazione:

    _nome: str
    _reg_naz: Regione

    def __init__(self, nome: str):

        self.setNome(nome)
        self._reg_naz = set()
    
    def setNome(self, nome: str) -> None:
        self._nome = nome
    
    def add_reg_naz(self, reg_naz: Regione) -> None:
        self._reg_naz.add(reg_naz)
    
    def remove_reg_naz(self, reg_naz: Regione) -> None:
        if len(self._reg_naz) >= 1:
            self._reg_naz.remove(reg_naz)
    
    def getNome(self) -> str:
        return self._nome
    
    def getRegNaz(self) -> frozenset[Regione]:
        return self._reg_naz

        