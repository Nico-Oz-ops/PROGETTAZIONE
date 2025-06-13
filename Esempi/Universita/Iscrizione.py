from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Custom_Types import *
    from Studente import Studente
    from CorsoDiLaurea import CorsodiLaurea
    from datetime import datetime

class _iscrizione:

    class _link:
        _studente: 'Studente' 
        _corsodilaurea: 'CorsodiLaurea'
        _data_iscrizione: datetime.date

        def __init__(self, studente: 'Studente', corsodilaurea: 'CorsodiLaurea', data_iscrizione: datetime.date):
            self._studente = studente
            self._corsodilaurea = corsodilaurea
            self._data_iscrizione = data_iscrizione
        
        def getStudente(self) -> 'Studente':
            return self._studente
        
        def getCorsoDiLaurea(self) -> 'CorsodiLaurea':
            return self._corsodilaurea
        
        def getDataIscrizione(self) -> datetime.date:
            return self._data_iscrizione
        
        def __eq__(self, other: Any):
            if type(self) != type(other) or hash(self) != hash(other):
                return False
            return (self.getStudente(), self.getCorsoDiLaurea()) == (other.getStudente(), other.getCorsodiLaurea())
            
        def __hash__(self) -> datetime.date:
            return hash((self.getStudente(), self.getCorsoDiLaurea()))
        
        


            
