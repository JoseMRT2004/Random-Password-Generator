from generador import GeneradorContrasena
from verificador import VerificadorSeguridad
from interfaz import InterfazCLI
from excepciones import TipoCaracterNoSeleccionadoError

def main():
    interfaz = InterfazCLI()
    interfaz.mostrar_titulo()
    interfaz.mostrar_panel_principal()

    preferencias = interfaz.obtener_preferencias_usuario()

    generador = GeneradorContrasena()
    if preferencias["mayusculas"]: generador.agregar_mayusculas()
    if preferencias["minusculas"]: generador.agregar_minusculas()
    if preferencias["digitos"]: generador.agregar_digitos()
    if preferencias["simbolos"]: generador.agregar_simbolos()

    try:
        contrasena = generador.generar(preferencias["longitud"])
        seguridad = VerificadorSeguridad.verificar(contrasena)
        interfaz.mostrar_resultados(contrasena, seguridad)
    except TipoCaracterNoSeleccionadoError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
