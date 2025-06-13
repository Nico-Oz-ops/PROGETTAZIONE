from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from CorsoDiLaurea import CorsodiLaurea



class TipoCorsoDiLaurea:
    _nome: str 
    _cdl_tipo: 'CorsodiLaurea'

    def __init__(self, nome: str):
        self.setNome(nome)
        self._cdl_tipo = set()

    def setNome(self, nome: str) -> None:
        self._nome = nome
    
    def add_cdl_tipo(self, cdl_tipo: 'CorsodiLaurea') -> None:
        self._cdl_tipo.add(cdl_tipo)
    
    def remove_cdl_tipo(self, cdl_tipo: 'CorsodiLaurea') -> None:
        if len(self._cdl_tipo) >= 1:
            self._cdl_tipo.remove(cdl_tipo)

    def getNome(self) -> str:
        return self._nome
    
    def getCdlTipo(self) -> frozenset['CorsodiLaurea']:
        return frozenset(self._cdl_tipo)
        