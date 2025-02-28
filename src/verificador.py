import re

class VerificadorSeguridad:
    """Verifica la fortaleza de una contraseña según criterios de seguridad."""

    @staticmethod
    def verificar(contrasena):
        puntuacion = 0
        longitud = len(contrasena)

        if longitud >= 8: puntuacion += 1
        if longitud >= 12: puntuacion += 1
        if longitud >= 16: puntuacion += 1
        if re.search(r"[A-Z]", contrasena): puntuacion += 1
        if re.search(r"[a-z]", contrasena): puntuacion += 1
        if re.search(r"[0-9]", contrasena): puntuacion += 1
        if re.search(r"[!@#$%^&*()_+{}\[\]:;'<>,.?/\\|`~-]", contrasena): puntuacion += 1

        patrones_comunes = ["123", "abc", "qwerty", "password", "admin", "1111", "0000"]
        if any(pat in contrasena.lower() for pat in patrones_comunes):
            puntuacion -= 1

        if puntuacion < 3: return "Muy Débil"
        elif puntuacion < 5: return "Débil"
        elif puntuacion < 7: return "Moderada"
        elif puntuacion < 9: return "Fuerte"
        else: return "Muy Fuerte"
