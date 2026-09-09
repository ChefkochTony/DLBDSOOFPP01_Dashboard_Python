from dataclasses import dataclass

@dataclass
class DashboardDatenDTO:
    """
    Data Transfer Object (DTO), das ausschließlich die bereinigten Werte 
    und Zielzustände für die Darstellungsschicht (View) transportiert.
    Es enthält absichtlich KEIN Domain-Objekt mehr!
    """
    aktueller_notenschnitt: float
    aktuelle_ects: int
    ziel_ects: int
    ist_notenziel_erreicht: bool
    ist_pace_ziel_erreicht: bool