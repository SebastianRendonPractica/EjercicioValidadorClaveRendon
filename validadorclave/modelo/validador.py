from abc import ABC, abstractmethod

class ReglaValidacion(ABC):

    def __init__(self, longitud_esperada):
        self._longitud_esperada = longitud_esperada
    
    @abstractmethod
    def es_valida(self, clave):
        pass

    def _validar_longitud(self, clave):
        if len(clave) > self._longitud_esperada:
            return True
        
    def _contiene_mayuscula(self, clave):
        return any(c.isupper() for c in clave)

    def _contiene_minuscula(self, clave):
        return any(c.islower() for c in clave)

    def _contiene_numero(self, clave):
        return any(c.isdigit() for c in clave)

    

class ReglaValidacionGanimedes:

    def contiene_caracter_especial(self):
    pass

class ReglaValidacionCalisto:
    pass



