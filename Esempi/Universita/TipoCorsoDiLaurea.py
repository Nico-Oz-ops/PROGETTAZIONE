from CorsoDiLaurea import CorsoDiLaurea
from typing import FrozenSet


class TipoCorsoDiLaurea:
    _nome: str 
    _cdl_tipo: CorsoDiLaurea

    def __init__(self, nome: str):
        self.setNome(nome)
        self._cdl_tipo = set()

    def setNome(self, nome: str) -> None:
        self._nome = nome
    
    def add_cdl_tipo(self, cdl_tipo: CorsoDiLaurea) -> None:
        self._cdl_tipo.add(cdl_tipo)
    
    def remove_cdl_tipo(self, cdl_tipo: CorsoDiLaurea) -> None:
        if len(self._cdl_tipo) >= 1:
            self._cdl_tipo.remove(cdl_tipo)

    def getNome(self) -> str:
        return self._nome
    
    def getCdlTipo(self) -> FrozenSet[CorsoDiLaurea]: # type: ignore
        return frozenset(self._cdl_tipo)
        