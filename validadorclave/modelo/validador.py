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

    

class ReglaValidacionGanimedes(ReglaValidacion):
    def __init__(self, longitud_esperada):
        super().__init__(longitud_esperada)

    def contiene_caracter_especial(self, clave):
        caracteres_especiales = "@_#$%"
        if any(i in caracteres_especiales for i in clave):
            return True
        

    def es_valida(self, clave):
        return super().es_valida(clave)
    pass



class ReglaValidacionCalisto(ReglaValidacion):
    def __init__(self, longitud_esperada):
        super().__init__(longitud_esperada)
    


    def contiene_calisto(self, clave):
        if clave.lower().count("calisto") == 0 or clave.upper().count("CALISTO") < 2:
            return False
    

    def es_valida(self, clave):
        return super().es_valida(clave)

    pass

class Validador():
    def __init__(self, reglas):
        self.reglas = reglas
    pass





