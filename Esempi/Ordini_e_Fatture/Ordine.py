from Custom_Types import *
from datetime import *


class Ordine:
    _data_stipula: datetime.date
    _descrizione: str
    _imponibile: FloatGEZ
    _aliquota_iva: FloatGEZ # [0..1] può ma non deve essere noto alla nascita
    _stato_ordine: StatoOrdine

    def __init__(self, data_stipulata: datetime.date, descrizione: str, imponibile: FloatGEZ, stato_ordine: StatoOrdine, aliquota_iva: FloatGEZ|None=None):
        self.setDataStipulata(data_stipulata)
        self.setDescrizione(descrizione)
        self.setImponibile(imponibile)
        self.setAliquotaIVA(aliquota_iva)
        self.setStatoOrdine(stato_ordine)
    
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


