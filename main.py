from repository import JsonStudiengangRepository
from service import StudienService
from controller import DashboardController
from view import DashboardView

class DashboardApp:
    def start(self):
        # 1. Instanziierung der konkreten Objekte
        repository = JsonStudiengangRepository('daten.json')
        service = StudienService()
        controller = DashboardController(repository, service)
        view = DashboardView()
        
        # 2. Programmablauf steuern
        daten_dto = controller.lade_dashboard_daten()
        view.zeige(daten_dto)

if __name__ == "__main__":
    app = DashboardApp()
    app.start()