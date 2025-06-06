from Custom_Types import *
from datetime import *
from Dipartimento import Dipartimento
from Fornitore import Fornitore

class Ordine:
    _data_stipula: datetime.date
    _descrizione: str
    _imponibile: FloatGEZ
    _aliquota_iva: FloatGEZ # [0..1] può ma non deve essere noto alla nascita
    _stato_ordine: StatoOrdine
    _dip_ordine: Dipartimento
    _forn_ord: Fornitore

    def __init__(self, data_stipulata: datetime.date, descrizione: str, imponibile: FloatGEZ, stato_ordine: StatoOrdine, dip_ordine: Dipartimento, forn_ord: Fornitore, aliquota_iva: FloatGEZ|None=None):
        self.setDataStipulata(data_stipulata)
        self.setDescrizione(descrizione)
        self.setImponibile(imponibile)
        self.setAliquotaIVA(aliquota_iva)
        self.setDipOrdine(dip_ordine)
        self.setStatoOrdine(stato_ordine)
        self.setFornOrd(forn_ord)
    
    def setDataStipulata(self, data_stipulata: datetime.date) -> None:
        self._data_stipula = data_stipulata
    
    def setDescrizionme(self, descrizione: str) -> None:
        self._descrizione = descrizione
    
    def setImponibile(self, imponibile: FloatGEZ) -> None:
        self._imponibile = imponibile

    def setAliquotaIVA(self, aliquota_iva: FloatGEZ | None) -> None:
        if aliquota_iva is not None:
            self._aliquota_iva = aliquota_iva
    
    def setStatoOrdine(self, stato_ordine: StatoOrdine) -> None:
        self._stato_ordine = stato_ordine
    
    def setDipOrdine(self, dip_ordine: Dipartimento) -> None:
        self._dip_ordine = dip_ordine
    
    def setFornOrd(self, forn_ord: Fornitore) -> None:
        self._forn_ord = forn_ord
    
    def getDataStipulata(self) -> datetime.date:
        return self._data_stipula
    
    def getDescrizione(self) -> str:
        return self._descrizione
    
    def getImponibile(self) -> FloatGEZ:
        return self._imponibile
    
    def getAliquotaIVA(self) -> FloatGEZ:
        return self._aliquota_iva
    
    def getStatoOrdine(self) -> StatoOrdine:
        return self._stato_ordine
    
    def getDipOrdine(self) -> Dipartimento:
        return self._dip_ordine

    def getFornOrd(self) -> Fornitore:
        return self._forn_ord


