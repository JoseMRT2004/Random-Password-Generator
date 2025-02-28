from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
import pyfiglet

class InterfazCLI:
    """Manejo de la interfaz de línea de comandos con arte ASCII y `rich`."""

    def __init__(self):
        self.console = Console()

    def mostrar_titulo(self):
        """Muestra el título en arte ASCII."""
        ascii_art = pyfiglet.figlet_format("Pass Manager")
        self.console.print(f"[bold cyan]{ascii_art}[/bold cyan]")

    def mostrar_panel_principal(self):
        """Muestra un panel de introducción."""
        panel_principal = Panel(
            "[bold white]Bienvenido al Generador de Contraseñas Seguras[/bold white]\n"
            "Seleccione sus preferencias y obtenga una contraseña segura.",
            title="Configuración",
            border_style="bold cyan",
            title_align="center",
            padding=(1, 2)
        )
        self.console.print(panel_principal)

    def mostrar_resultados(self, contrasena, seguridad):
        """Muestra la contraseña generada y su nivel de seguridad en una tabla."""
        table = Table(title="Contraseña Generada", show_header=True, pad_edge=False)
        table.add_column("Contraseña", justify="center", style="bold cyan")
        table.add_column("Seguridad", justify="center", style="bold magenta")
        table.add_row(contrasena, seguridad)
        self.console.print(table)

    def obtener_preferencias_usuario(self):
        """Permite al usuario elegir los tipos de caracteres y la longitud."""
        self.console.print("\nSeleccione los tipos de caracteres a incluir:\n")
        incluir_mayusculas = Prompt.ask("[bold yellow]¿Incluir mayúsculas?[/]", choices=["y", "n"])
        incluir_minusculas = Prompt.ask("[bold yellow]¿Incluir minúsculas?[/]", choices=["y", "n"])
        incluir_digitos = Prompt.ask("[bold yellow]¿Incluir dígitos?[/]", choices=["y", "n"])
        incluir_simbolos = Prompt.ask("[bold yellow]¿Incluir símbolos?[/]", choices=["y", "n"])
        longitud = int(Prompt.ask("[bold green]Ingrese la longitud de la contraseña (mínimo 8 caracteres)[/]"))

        return {
            "mayusculas": incluir_mayusculas == "y",
            "minusculas": incluir_minusculas == "y",
            "digitos": incluir_digitos == "y",
            "simbolos": incluir_simbolos == "y",
            "longitud": max(8, longitud)
        }
