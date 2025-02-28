""" - Excepción cuando no se seleccionan caracteres para la contraseña
     - Excepción para contraseñas inválidas"""

class ContraseñaInvalidaError(Exception):
    def __init__(self, mensaje="La contraseña no cumple con los requisitos mínimos"):
        super().__init__(mensaje)

class TipoCaracterNoSeleccionadoError(Exception):
    def __init__(self, mensaje="Debe seleccionar al menos un tipo de carácter para generar la contraseña"):
        super().__init__(mensaje)
