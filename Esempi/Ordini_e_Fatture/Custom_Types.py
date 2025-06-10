import re
from typing import *
from datetime import date
from enum import *

class CodiceFiscale(str):

    def __new__(cls, cf: str | Self) -> Self:

        cff: str = cf.upper().strip()
        
        if re.fullmatch(r"[A-Z]{6}[0-9]{2}[A-Z]{1}[0-9]{2}[A-Z]{1}[0-9]{3}[A-Z]{1}", cf):
            return super().__new__(cls, cff)
        raise ValueError(f"{cff} non è un codice fiscale italiano valido")

class DataGE1895(date):
    # Tipo di dato specializzato Data 

    def __new__(cls, year, month, day):
        if year < 1895:
            raise ValueError(f"La data {day}/{month}/{year} deve essere successiva all'1 gennaio 1895")
        
        return super().__new__(cls, year=year, month=month, day=day)

class Telefono(str):

    def __new__(cls, tel: str | Self) -> Self:
        
        if re.fullmatch(r"^\d{10}$", tel):
            return super().__new__(cls, tel)
        raise ValueError(f"{tel} non è un numero di telefono italiano valido")
    
class Email(str):

    def __new__(cls, email: str | Self) -> Self:
        
        if re.fullmatch(r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$", email):
            return super().__new__(cls, email)
        raise ValueError(f"{email} non è una email valida")

class Indirizzo:
	# campi dati:
	# _via:str
	# _civico:...
	def __init__(self, via:str, civico:str):
		if via is None:
			raise ValueError(f"via cannot be None")
		if civico is None:
			raise ValueError(f"civ cannot be None")
		
		self._via:str = via

		if not re.fullmatch(r"^[0-9]+[a-zA-Z]*$", civico):
			raise ValueError(f"value for civico '{civico}' not allowed")
		self._civico:str = civico
	
	def via(self)->str:
		return self._via
	def civico(self)->str:
		return self._civico

	def __repr__(self)->str:
		return f"Indirizzo(via={self.via()}, civico={self.civico()})"


	# class Indirizzo implementa un tipo di dato: Python deve riconoscere se oggetti diversi rappresentano lo stesso valore
	def __hash__(self)->int:
		return hash( (self.via(), self.civico()) )

	def __eq__(self, other:Any)->bool:
		if other is None or \
				not isinstance(other, type(self)) or \
				hash(self) != hash(other):
			return False
		return (self.via(), self.civico() ) == (other.via(), other.civico())

class PartitaIVA(int):

    def __new__(cls, iva: int | str | Self) -> Self:
        if re.fullmatch(r"^[0-9]{11}$"):
            return super().__new__(cls, iva)
        raise ValueError(f"La partita IVA '{iva}' non è valida")

class Genere(StrEnum):

    uomo = auto()
    donna = auto()

class StatoOrdine(StrEnum):

    in_preparazione = auto()
    inviato = auto()
    da_saldare = auto()
    saldato = auto()

class IntGEZ(int):
    # Tipo di dato specializzato Intero >= 0

    def __new__(cls, v: Self | int | float | str | bool):

        value: int = super().__new__(cls, v)

        if value < 0:
            raise ValueError(f"The value {v} must be greater than or equal to zero")
        return value
    
class FloatGEZ(float):
    # Tipo di dato specializzato Float >= 0

    def __new__(cls, v: Self | int | float | str | bool):

        value: float = super().__new__(cls, v)

        if value < 0:
            raise ValueError(f"The value {v} must be greater than zero")
        return value

class IntGZ(int):
    # Tipo di dato specializzato Intero > 0

    def __new__(cls, v: Self | int | float | str | bool):

        value: int = super().__new__(cls, v)

        if value <= 0:
            raise ValueError(f"The value {v} must be greater than zero")
        return value
    
    # Attenzione: in generale la differenza tra interi non dovrebbe essere toccata
    def __sub__(self, other: int | Self) -> Self:
        other_int : int = int(other)
        
        try:
            res: int = int(self) - other_int
            return IntGZ(res)
        except ValueError:
            raise ValueError(f"The difference between {self} and {other} is not an IntGZ")