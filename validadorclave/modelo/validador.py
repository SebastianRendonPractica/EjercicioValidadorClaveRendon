from abc import ABC, abstractmethod

class ReglaValidacion(ABC):

    def __init__(self, longitud_esperada):
        self._longitud_esperada = longitud_esperada
    
    @abstractmethod
    def es_valida(self, clave):
        pass

    def _validar_longitud(self, clave):
        return len(clave) > self._longitud_esperada
    


    

class ReglaValidacionGanimedes:
    pass

class ReglaValidacionCalisto:
    pass



