# Python Studien-Dashboard (DLBDSOOFPP01_D)

Dieses Repository enthält den prototypischen Kommandozeilen-Prototyp (CLI) für ein Studien-Dashboard, entwickelt im Rahmen des Kurses **Objektorientierte und funktionale Programmierung mit Python** an der IU Internationalen Hochschule.

## Projektbeschreibung

Das Dashboard dient der Überwachung des individuellen Studienfortschritts. Es gleicht den aktuellen Notendurchschnitt sowie die ECTS-Pace mit vorab definierten Zielwerten ab (z.B. 180 ECTS in 4,5 Jahren, Notenschnitt besser als 2,0).

Die Besonderheit dieses Projekts liegt in der konsequenten Anwendung objektorientierter Programmierkonzepte und der Umsetzung einer sauberen Schichtenarchitektur (Clean Architecture).

## Features

* **Lokale Datenhaltung:** Persistente Speicherung der Modul- und Notendaten in einer lokalen `daten.json`. Das Programm erfordert zur Laufzeit keine Internetverbindung.
* **Kommandozeilen-UI:** Farbige und strukturierte Konsolenausgabe (Visualisierung von Fortschrittsbalken und Zielzuständen) mittels der Bibliothek `rich`.


* **Entkoppelte Architektur:** Strikte Trennung von Fachlogik (Domain/Service), Datenzugriff (Repository) und Präsentation (View/DTO).



## Architektur & Schichtenmodell

* **Domain:** Fachklassen (`Studiengang`, `Modulbelegung`, `Modul`, `Pruefungsleistung`, Enum `Pruefungsstatus`) inklusive Validierungslogik (z.B. 1..* Multiplizitäten via `__post_init__`).


* **Repository:** Dependency Inversion durch eine abstrakte Basisklasse (`StudiengangRepository`), umgesetzt durch das konkrete `JsonStudiengangRepository`.


* **Service:** Kapselung der Berechnungslogik (Notenschnitt, Pace) und Abgleich mit den Zielwerten (`StudienService`).


* **Controller & DTO:** Steuerung des Datenflusses. Zur sauberen Entkopplung werden ausschließlich vorbereitete Werte über ein `DashboardDatenDTO` an die View übergeben.


* **View:** Reine Präsentationsschicht ohne eigene fachliche Berechnungslogik (`DashboardView`).



## Installation und Start

1. **Repository klonen oder herunterladen:**
```bash
git clone https://github.com/ChefkochTony/DLBDSOOFPP01_Dashboard_Python.git
cd DLBDSOOFPP01_Dashboard_Python

```


2. **Abhängigkeiten installieren:**
Für die farbliche CLI-Darstellung wird das Standard-Paket `rich` benötigt.
```bash
pip install rich

```


3. **Dashboard ausführen:**
```bash
python main.py

```


*(Tipp für Windows-Nutzer: Bei Problemen mit dem `python`-Befehl das Programm im "Anaconda Prompt" starten).*

## Datenpflege

Die Pflege der Modul- und Notendaten erfolgt direkt über die Datei `daten.json`. Sobald neue Noten oder Module in die Struktur eingetragen werden, wertet das Dashboard diese beim nächsten Programmstart automatisch aus.

Legst du diese Datei nun als `README.md` direkt zu deinen anderen Python-Dateien in den Ordner und pusht sie zu GitHub, oder sollen wir direkt mit dem Abstract weitermachen?
