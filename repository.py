import json
from abc import ABC, abstractmethod
from datetime import datetime
from domain import Studiengang, Modul, Modulbelegung, Pruefungsleistung, Pruefungsstatus

class StudiengangRepository(ABC):
    """Abstrakte Basisklasse für die Datenhaltung."""
    @abstractmethod
    def lade_studiengang(self) -> Studiengang:
        pass
        
    @abstractmethod
    def speichere(self, studiengang: Studiengang) -> None:
        pass

class JsonStudiengangRepository(StudiengangRepository):
    """Konkrete Implementierung für dateibasierte JSON-Speicherung."""
    def __init__(self, dateipfad: str):
        self.dateipfad = dateipfad

    def lade_studiengang(self) -> Studiengang:
        with open(self.dateipfad, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # 1. Belegungen ZUERST erstellen
        belegungen_liste = []
        for b_data in data.get('belegungen', []):
            modul = Modul(titel=b_data['modul']['titel'], ects_punkte=b_data['modul']['ects_punkte'])
            status = Pruefungsstatus(b_data['status'])
            
            pl = None
            if 'pruefungsleistung' in b_data and b_data['pruefungsleistung'] is not None:
                note = b_data['pruefungsleistung'].get('note')
                pl = Pruefungsleistung(note=note)
                
            belegung = Modulbelegung(modul=modul, status=status, pruefungsleistung=pl)
            belegungen_liste.append(belegung)

        # 2. Studiengang-Objekt MIT der befüllten Liste instanziieren.
        # Python ruft hiernach vollautomatisch __post_init__ auf und validiert erfolgreich!
        sg = Studiengang(
            bezeichnung=data['bezeichnung'],
            start_datum=datetime.strptime(data['start_datum'], '%Y-%m-%d').date(),
            ziel_datum=datetime.strptime(data['ziel_datum'], '%Y-%m-%d').date(),
            ziel_ects=data['ziel_ects'],
            ziel_note=data.get('ziel_note', 2.0),
            belegungen=belegungen_liste
        )
        
        return sg

    def speichere(self, studiengang: Studiengang) -> None:
        pass # Für diesen Read-Only-Prototypen lassen wir das Speichern weg