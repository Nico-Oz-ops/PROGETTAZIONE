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
    _aeroporto_citta: _aeroporto_citta # mutabile e noto alla nascita

    def __init__(self, codice: CodiceAeroporto, nome: str, aeroporto_citta: _aeroporto_citta):
        self._codice = codice
        self.setNome(nome)
        self._voli_arrivo = set()
        self._voli_partenza = set()
        self.setAeroportoCitta(aeroporto_citta)
    
    def setNome(self, nome: str) -> None:
        self._nome = nome
    
    def add_voli_arrivo(self, voli_arrivo: _arrivo) -> None:
        self._voli_arrivo.add(voli_arrivo)
    
    def remove_voli_arrivo(self, voli_arrivo: _arrivo) -> None:
        if len(self._voli_arrivo) >= 1 and voli_arrivo in self._voli_arrivo:
            self._voli_arrivo.remove(voli_arrivo)
        else:
            raise ValueError(f"Errore, il volo '{voli_arrivo}' non arriva all'aeroporto '{self._nome}'")

    def add_voli_partenza(self, voli_partenza: _partenza) -> None:
        self._voli_partenza.add(voli_partenza)
    
    def remove_voli_partenza(self, voli_partenza: _partenza) -> None:
        if len(self._voli_partenza) >= 1 and voli_partenza in self._voli_partenza:
            self._voli_partenza.remove(voli_partenza)
        else:
            raise ValueError(f"Errore, il volo '{voli_partenza}' non parte dall'aeroporto '{self._nome}'")

    def setAeroportoCitta(self, aeroporto_citta: _aeroporto_citta) -> None:
        self._aeroporto_citta = aeroporto_citta
    
    def getNome(self) -> str:
        return self._nome
    
    def getCodiceAeroporto(self) -> CodiceAeroporto:
        return self._codice
    
    def getVoliArrivo(self) -> frozenset[_arrivo]:
        return frozenset(self._voli_arrivo)
    
    def getVoliPartenza(self) -> frozenset[_partenza]:
        return frozenset(self._voli_partenza)
    
    def getAeroportoCitta(self) -> _aeroporto_citta:
        return self._aeroporto_citta

class Citta:
    _nome: str 
    _abitanti: Abitanti
    _aeroporto_citta: _aeroporto_citta # mutabile e non noti alla nascita
    _citta_nazione: _citta_nazione # mutabile e certamente noto alla nascita

    def __init__(self, nome: str, abitanti: Abitanti, citta_nazione: _citta_nazione):
        self.setNome(nome)
        self.setAbitanti(abitanti)
        self._aeroporto_citta = set()
        self.setCittaNazione(citta_nazione)
    
    def setNome(self, nome: str) -> None:
        if not isinstance(nome, str) or nome.strip() == "":
            raise ValueError("Errore. Nome non valido")
        self._nome = nome
    
    def setAbitanti(self, abitanti: Abitanti) -> None:
        self._abitanti = abitanti
    
    def add_aeroporto_citta(self, aeroporto_in_citta: _aeroporto_citta) -> None:
        self._aeroporto_citta.add(aeroporto_in_citta)
    
    def remove_aeroporto_citta(self, aeroporto_in_citta: _aeroporto_citta) -> None:
        if len(self._aeroporto_citta) >= 1 and aeroporto_in_citta in self._aeroporto_citta:
            self._aeroporto_citta.remove(aeroporto_in_citta)
        
        else:
            raise ValueError(f"Errore, l'aeroporto '{aeroporto_in_citta}' non si trova nella città di '{self._nome}'.")
    
    def setCittaNazione(self, citta_nazione: _citta_nazione) -> None:
        self._citta_nazione = citta_nazione
    
    def getNome(self) -> str:
        return self._nome
    
    def getAbitanti(self) -> Abitanti:
        return self._abitanti
    
    def getAeroportoCitta(self) -> frozenset[_aeroporto_citta]:
        return frozenset(self._aeroporto_citta)
    
    def getCittaNazione(self) -> _citta_nazione:
        return self._citta_nazione

class CompagniaAerea:
    _nome: str
    _anno_fondazione: Data1900 # <<immutabile>>
    _voli_della_compagnia: _volo_compagnia # mutabile, non noti alla nascita
    _sede_direzione: Citta # mutabile, nota alla nascita

    def __init__(self, nome: str, anno_fondazione: Data1900, sede_direzione: Citta):
        self._anno_fondazione = anno_fondazione
        self.setNome(nome)
        self._voli_della_compagnia = set()
        self.setSedeDirezione(sede_direzione)
    
    def setNome(self, nome: str) -> None:
        if not isinstance(nome, str) or nome.strip() == "":
            raise ValueError("Errore. Nome non valido")
        self._nome = nome
    
    def add_voli_della_compagnia(self, volo: _volo_compagnia) -> None:
        self._voli_della_compagnia.add(volo)
    
    def remove_voli_della_compagnia(self, volo: _volo_compagnia) -> None:
        if len(self._voli_della_compagnia) >= 1 and volo in self._voli_della_compagnia:
            self._voli_della_compagnia.remove(volo)
        
        else:
            raise ValueError(f"Errore, il volo '{volo}' non fa parte della compagnia aerea '{self._nome}'.")
    
    def setSedeDirezione(self, sede_direzione: Citta) -> None:
        self._sede_direzione = sede_direzione
    
    def getNome(self) -> str:
        return self._nome
    
    def getAnnoFondazione(self) -> Data1900:
        return self._anno_fondazione
    
    def getVoliDellaCompagnia(self) -> frozenset[_volo_compagnia]:
        return frozenset(self._voli_della_compagnia)
    
    def getSedeDirezione(self) -> Citta:
        return self._sede_direzione

class Nazione:
    _nome: str
    _citta_nazione: _citta_nazione # mutabile e non noti alla nascita

    def __init__(self, nome: str):
        self.setNome(nome)
        self._citta_nazione = set()

    def setNome(self, nome: str) -> None:
        if not isinstance(nome, str) or nome.strip() == "":
            raise ValueError("Errore. Nome non valido")
        self._nome = nome
    
    def add_citta_nazione(self, citta_in_nazione: _citta_nazione) -> None:
        self._citta_nazione.add(citta_in_nazione)
    
    def remove_citta_nazione(self, citta_in_nazione: _citta_nazione) -> None:
        if len(self._citta_nazione) >= 1 and citta_in_nazione in self._citta_nazione:
            self._citta_nazione.remove(citta_in_nazione)
        
        else:
            raise ValueError(f"Errore. '{citta_in_nazione}' non si trova nella nazione '{self._nome}'.")

    def getNome(self) -> str:
        return self._nome  

    def getCittaNazione(self) -> frozenset[_citta_nazione]:
        return frozenset(self._citta_nazione)     

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

class _aeroporto_citta:

    class _link:
        _aeroporto: Aeroporto # immutabile, sempre noto alla nascita
        _citta: Citta # immutabile, sempre noto alla nascita

        def getAeroporto(self) -> Aeroporto:
            return self._aeroporto
        
        def getCitta(self) -> Citta:
            return self._citta
        
        def __init__(self, aeroporto: Aeroporto, citta: Citta):
            self._citta = citta
            self._aeroporto = aeroporto

        def __hash__(self) -> int:
            return hash((self.getAeroporto(), self.getCitta()))
        
        def __eq__(self, other: Any):
            if type(self) != type(other) or hash(self) != hash(other):
                return False
            return (self.getAeroporto(), self.getCitta()) == (other.getAeroporto(), other.getCitta())

class _citta_nazione:
    class _link:
        _citta: Citta #immutabile, sempre noto alla nascita
        _nazione: Nazione #immutabile, sempre noto alla nascita

        def getCitta(self) -> Citta:
            return self._citta
        
        def getNazione(self) -> Nazione:
            return self._nazione
        
        def __init__(self, citta: Citta, nazione: Nazione):
            self._citta = citta
            self._nazione = nazione
        
        def __hash__(self) -> int:
            return hash((self.getCitta(), self.getNazione()))
        
        def __eq__(self, other) -> bool:
            if type(self) != type(other) or hash(self) != hash(other):
                return False
            return (self.getCitta(), self.getNazione()) == (other.getCitta(), self.getNazione())


            





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
    
        

        


        


        