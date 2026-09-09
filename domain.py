from __future__ import annotations
from dataclasses import dataclass, field
from datetime import date
from enum import Enum
from typing import List, Optional

class Pruefungsstatus(Enum):
    OFFEN = "Offen"
    BESTANDEN = "Bestanden"
    ANGERECHNET = "Angerechnet"
    NICHT_BESTANDEN = "Nicht bestanden"

@dataclass
class Pruefungsleistung:
    """Repräsentiert eine erbrachte Prüfungsleistung. Note ist optional (z.B. bei Anerkennung)."""
    note: Optional[float] = None

@dataclass
class Modul:
    """Repräsentiert ein Modul aus dem Modulkatalog (wiederverwendbar)."""
    titel: str
    ects_punkte: int

@dataclass
class Modulbelegung:
    """Verknüpft ein Modul mit dem Studiengang und hält den individuellen Status."""
    modul: Modul
    status: Pruefungsstatus
    pruefungsleistung: Optional[Pruefungsleistung] = None

    @property
    def ist_abgeschlossen(self) -> bool:
        """Prüft, ob das Modul erfolgreich abgeschlossen wurde."""
        return self.status in (Pruefungsstatus.BESTANDEN, Pruefungsstatus.ANGERECHNET)

@dataclass
class Studiengang:
    """Wurzeleinheit, die den Studiengang und alle belegten Module bündelt."""
    bezeichnung: str
    start_datum: date
    ziel_datum: date
    ziel_ects: int
    ziel_note: float = 2.0  # Zielwert für den Controller/Service
    belegungen: List[Modulbelegung] = field(default_factory=list)

    def __post_init__(self):
        """Validierung der 1..* Multiplizität. Ein Studiengang muss mindestens ein Modul haben."""
        if not self.belegungen:
            raise ValueError(
                f"Der Studiengang '{self.bezeichnung}' muss mindestens eine Modulbelegung enthalten (1..* Beziehung)."
            )
            
    def fuege_belegung_hinzu(self, belegung: Modulbelegung) -> None:
        """Fügt dem Studiengang eine neue Modulbelegung hinzu."""
        self.belegungen.append(belegung)