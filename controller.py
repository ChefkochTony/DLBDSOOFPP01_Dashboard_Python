from dto import DashboardDatenDTO
from repository import StudiengangRepository
from service import StudienService

class DashboardController:
    """Koordiniert den Datenfluss zwischen Datenhaltung, Logik und Darstellung."""
    def __init__(self, repository: StudiengangRepository, service: StudienService):
        self.repository = repository
        self.service = service

    def lade_dashboard_daten(self) -> DashboardDatenDTO:
        # 1. Daten laden (kennt nur das abstrakte Repository)
        studiengang = self.repository.lade_studiengang()
        
        # 2. Logik & Berechnungen über Service ausführen
        notenschnitt = self.service.berechne_notenschnitt(studiengang)
        ects = self.service.berechne_ects_pace(studiengang)
        ziel_noten = self.service.pruefe_ziel_notenschnitt(studiengang)
        ziel_pace = self.service.pruefe_ziel_pace(studiengang)
        
        # 3. DTO für die View bauen (keine Domain-Objekte mehr enthalten!)
        return DashboardDatenDTO(
            aktueller_notenschnitt=notenschnitt,
            aktuelle_ects=ects,
            ziel_ects=studiengang.ziel_ects,
            ist_notenziel_erreicht=ziel_noten,
            ist_pace_ziel_erreicht=ziel_pace
        )