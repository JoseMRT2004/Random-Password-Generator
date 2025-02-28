import random
import string
from excepciones import TipoCaracterNoSeleccionadoError

class GeneradorContrasena:
    """Genera contraseñas robustas con opciones personalizadas."""

    def __init__(self):
        self.caracteres = ''

    def agregar_mayusculas(self):
        self.caracteres += string.ascii_uppercase

    def agregar_minusculas(self):
        self.caracteres += string.ascii_lowercase

    def agregar_digitos(self):
        self.caracteres += string.digits

    def agregar_simbolos(self):
        self.caracteres += string.punctuation

    def generar(self, longitud):
        """Genera una contraseña según los caracteres seleccionados."""
        if not self.caracteres:
            raise TipoCaracterNoSeleccionadoError()
        return ''.join(random.choices(self.caracteres, k=longitud))
