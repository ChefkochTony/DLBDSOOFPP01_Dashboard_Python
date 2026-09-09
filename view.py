from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, BarColumn, TextColumn
from rich.text import Text
from dto import DashboardDatenDTO

class DashboardView:
    """Kümmert sich rein um die grafische Aufbereitung im CLI (Kommandozeile)."""
    def __init__(self):
        self.console = Console()

    def zeige(self, daten: DashboardDatenDTO) -> None:
        self.console.print("\n[bold blue]=== Dashboard zum Cyber-Security-Studiengang ===[/bold blue]\n")
        
        # 1. ECTS Fortschritt anzeigen
        pace_farbe = "green" if daten.ist_pace_ziel_erreicht else "red"
        
        with Progress(
            TextColumn("[progress.description]{task.description}"),
            BarColumn(complete_style=pace_farbe),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        ) as progress:
            task = progress.add_task(f"[{pace_farbe}]Aktueller Fortschritt:", total=daten.ziel_ects)
            progress.update(task, completed=daten.aktuelle_ects)
            
        self.console.print(f"[{pace_farbe}]IST: {daten.aktuelle_ects} ECTS | SOLL: {daten.ziel_ects} ECTS[/]\n")

        # 2. Notenschnitt anzeigen
        noten_farbe = "green" if daten.ist_notenziel_erreicht else "red"
        
        noten_panel = Panel(
            f"[{noten_farbe}][bold]{daten.aktueller_notenschnitt}[/bold][/]",
            title="Aktueller Notendurchschnitt",
            subtitle="Ziel: < 2.0",
            expand=False
        )
        self.console.print(noten_panel)
        self.console.print("\n")