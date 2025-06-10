from Custom_types import *
from Tipi_Dati_Voli_Aerei import *
from typing import *
from __future__ import annotations

class Volo:
    _codice: CodiceVolo # <<immutabile>>
    _durata_minuti: Durata
    _partenza: _partenza # noto alla nascita e immutabile
    _arrivo: _arrivo
    _volo_compagnia: _volo_compagnia # immu e noto alla nascita

    def __init__(self, codice: CodiceVolo, durata_minuti: Durata, partenza: _partenza, arrivo: _arrivo, volo_compagnia: _volo_compagnia):
        self._codice = codice
        self.setDurataMinuti(durata_minuti)
        self._partenza = partenza
        self._arrivo = arrivo
        self._volo_compagnia = volo_compagnia
    
    def setDurataMinuti(self, durata_minuti: Durata) -> None:
        self._durata_minuti = durata_minuti
    
    def getDurataMinuti(self) -> Durata:
        return self._durata_minuti
    
    def getCodiceVolo(self) -> CodiceVolo:
        return self._codice
    
    def getPartenza(self) -> _partenza:
        return self._partenza
    
    def getArrivo(self) -> _arrivo:
        return self._arrivo
    
    def getVoloCompagnia(self) -> _volo_compagnia:
        return self._volo_compagnia
    
class Aeroporto:
    _codice: CodiceAeroporto # <<immutabile>>
    _nome: str # noto alla nascita
    _voli_arrivo: _arrivo
    _voli_partenza: _partenza

    def __init__(self, codice: CodiceAeroporto, nome: str):
        self._codice = codice
        self.setNome(nome)
        self.voli_arrivo = set()
        self.voli_partenza = set()
    
    def setNome(self, nome: str) -> None:
        self._nome = nome
    
    def add_voli_arrivo(self, voli_arrivo: _arrivo) -> None:
        self.voli_arrivo.add(voli_arrivo)
    
    def remove_voli_arrivo(self, voli_arrivo: _arrivo) -> None:
        if len(self.voli_arrivo) >= 1:
            self.voli_arrivo.remove(voli_arrivo)

    def add_voli_partenza(self, voli_partenza: _partenza) -> None:
        self.voli_partenza.add(voli_partenza)
    
    def remove_voli_partenza(self, voli_partenza: _partenza) -> None:
        if len(self.voli_partenza) >= 1:
            self.voli_partenza.remove(voli_partenza)
    
    def getNome(self) -> str:
        return self._nome
    
    def getCodiceAeroporto(self) -> CodiceAeroporto:
        return self._codice
    
    def getVoliArrivo(self) -> frozenset[_arrivo]:
        return frozenset(self._voli_arrivo)
    
    def getVoliPartenza(self) -> frozenset[_partenza]:
        return frozenset(self._voli_partenza)

class Citta:
    _nome: str 
    _abitanti: Abitanti

    def __init__(self, nome: str, abitanti: Abitanti):
        self.setNome(nome)
        self.setAbitanti(abitanti)
    
    def setNome(self, nome: str) -> None:
        if not isinstance(nome, str) or nome.strip() == "":
            raise ValueError("Errore. Nome non valido")
        self._nome = nome
    
    def setAbitanti(self, abitanti: Abitanti) -> None:
        self._abitanti = abitanti
    
    def getNome(self) -> str:
        return self._nome
    
    def getAbitanti(self) -> Abitanti:
        return self._abitanti

class CompagniaAerea:
    _nome: str
    _anno_fondazione: Data1900 # <<immutabile>>
    _voli_della_compagnia: _volo_compagnia # mutabile, non noti alla nascita

    def __init__(self, nome: str, anno_fondazione: Data1900):
        self._anno_fondazione = anno_fondazione
        self.setNome(nome)
        self._voli_della_compagnia = set()
    
    def setNome(self, nome: str) -> None:
        if not isinstance(nome, str) or nome.strip() == "":
            raise ValueError("Errore. Nome non valido")
        self._nome = nome
    
    def add_voli_della_compagnia(self, volo: _volo_compagnia) -> None:
        self._voli_della_compagnia.add(volo)
    
    def remove_voli_della_compagnia(self, volo: _volo_compagnia) -> None:
        if len(self._voli_della_compagnia) >= 1:
            self._voli_della_compagnia.remove(volo)
    
    def getNome(self) -> str:
        return self._nome
    
    def getAnnoFondazione(self) -> Data1900:
        return self._anno_fondazione
    
    def getVoliDellaCompagnia(self) -> frozenset[_volo_compagnia]:
        return frozenset(self._voli_della_compagnia)

class Nazione:
    _nome: str

    def __init__(self, nome: str):
        self.setNome(nome)

    def setNome(self, nome: str) -> None:
        if not isinstance(nome, str) or nome.strip() == "":
            raise ValueError("Errore. Nome non valido")
        self._nome = nome

    def getNome(self) -> str:
        return self._nome       

class _partenza:

    class _link:
        _volo: Volo
        _aeroporto: Aeroporto

        def getVolo(self) -> Volo:
            return self._volo
        
        def getAeroporto(self) -> Aeroporto:
            return self._aeroporto
        
        def __init__(self, volo: Volo, aeroporto: Aeroporto):
            self._volo = volo
            self._aeroporto = aeroporto
        
        def __hash__(self) -> int:
            return hash((self.getVolo(), self.getAeroporto()))
        
        def __eq__(self, other: Any) -> bool:
            if type(self) != type(other) or hash(self) != hash(other):
                return False
            return (self.getVolo(), self.getAeroporto()) == (other.getVolo(), other.getAeroporto())
            
class _arrivo:

    class _link:
        _volo: Volo
        _aeroporto: Aeroporto

        def getVolo(self) -> Volo:
            return self._volo
        
        def getAeroporto(self) -> Aeroporto:
            return self._aeroporto
        
        def __init__(self, volo: Volo, aeroporto: Aeroporto):
            self._volo = volo
            self._aeroporto = aeroporto
        
        def __hash__(self) -> int:
            return hash((self.getVolo(), self.getAeroporto()))
        
        def __eq__(self, other: Any) -> bool:
            if type(self) != type(other) or hash(self) != hash(other):
                return False
            return (self.getVolo(), self.getAeroporto()) == (other.getVolo(), other.getAeroporto())

class _volo_compagnia:

    class _link:
        _volo: Volo # immutabile, noto alla nascita
        _compagnia_area: CompagniaAerea # immutabile, noto alla nascita

        def getVolo(self) -> Volo:
            return self._volo
        
        def getCompagniaArea(self) -> CompagniaAerea:
            return self._compagnia_area
        
        def __init__(self, volo: Volo, compagnia_area: CompagniaAerea):
            self._volo = volo
            self._compagnia_area = compagnia_area
        
        def __hash__(self) -> int:
            return hash((self.getVolo(), self.getAeroporto()))
        
        def __eq__(self, other: Any):
            if type(self) != type(other) or hash(self) != hash(other):
                return False
            return (self.getVolo(), self.getCompagniaArea()) == (other.getVolo(), other.getCompagniaArea())
            
            

            
        






# class Nazione:
#     _nome: str
#     _citta_nazione: set[Citta]

#     def __init__(self, nome: str):
#         self.setNome(nome)
#         self._citta_nazione = set()

#     def setNome(self, nome: str) -> None:
#         self._nome = nome
    
#     def add_citta_nazione(self, citta: Citta) -> None:
#         self._citta_nazione.add(citta)
    
#     def remove_citta_nazione(self, citta: Citta) -> None:
#         if citta in self._citta_nazione:
#             self._citta_nazione.remove(citta)
#         else:
#             raise ValueError("Errore. La città non si trova nella lista")

#     def getCittaNazione(self) -> frozenset[Citta]:
#         return frozenset(self._citta_nazione)

#     def getNome(self) -> str:
#         return self._nome     
    
        

        


        


        