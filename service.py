from datetime import date
from domain import Studiengang

class StudienService:
    """Kapselt die fachliche Berechnungslogik (Notenschnitt, Pace, Zielprüfung)."""
    
    def berechne_notenschnitt(self, studiengang: Studiengang) -> float:
        noten_summe = 0.0
        gewichtung_ects = 0
        
        for bel in studiengang.belegungen:
            # Nur abgeschlossene Module mit echter numerischer Note zählen
            if bel.ist_abgeschlossen and bel.pruefungsleistung and bel.pruefungsleistung.note is not None:
                noten_summe += bel.pruefungsleistung.note * bel.modul.ects_punkte
                gewichtung_ects += bel.modul.ects_punkte
                
        if gewichtung_ects == 0:
            return 0.0
        return round(noten_summe / gewichtung_ects, 1)

    def berechne_ects_pace(self, studiengang: Studiengang) -> int:
        ects_summe = 0
        for bel in studiengang.belegungen:
            if bel.ist_abgeschlossen:
                ects_summe += bel.modul.ects_punkte
        return ects_summe

    def pruefe_ziel_notenschnitt(self, studiengang: Studiengang) -> bool:
        schnitt = self.berechne_notenschnitt(studiengang)
        if schnitt == 0.0:
            return True # Noch keine Noten eingetragen
        # Im deutschen System ist eine kleinere Note besser
        return schnitt <= studiengang.ziel_note

    def pruefe_ziel_pace(self, studiengang: Studiengang) -> bool:
        # Pace-Berechnung: Ziel = 180 ECTS in 54 Monaten (4,5 Jahre) = ~3.33 pro Monat
        heute = date.today()
        monate_vergangen = (heute.year - studiengang.start_datum.year) * 12 + (heute.month - studiengang.start_datum.month)
        
        # Vermeide negative Monate, falls Start in der Zukunft
        monate_vergangen = max(0, monate_vergangen) 
        
        soll_ects = int(monate_vergangen * 3.33)
        ist_ects = self.berechne_ects_pace(studiengang)
        
        return ist_ects >= soll_ects