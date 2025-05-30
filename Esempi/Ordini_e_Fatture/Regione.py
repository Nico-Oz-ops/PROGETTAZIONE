


class Regione:

    _nome: str

    def __init__(self, nome: str):

        self.setNome(nome)
    
    def setNome(self, nome: str) -> None:
        self._nome = nome
    
    def getNome(self) -> str:
        return self._nome
        