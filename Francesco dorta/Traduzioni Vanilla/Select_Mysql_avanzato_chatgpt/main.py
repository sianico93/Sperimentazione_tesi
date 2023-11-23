from controller import ApparecchiatureElettronicheController
from view import ApparecchiatureElettronicheView
 
def main():
    try:
        controller = ApparecchiatureElettronicheController()
        results = controller.get_elettroniche_by_resolution()
 
        view = ApparecchiatureElettronicheView()
        view.display_results(results)
    except Exception as e:
        print("Errore generale:", str(e))
 
if __name__ == "__main__":
    main()