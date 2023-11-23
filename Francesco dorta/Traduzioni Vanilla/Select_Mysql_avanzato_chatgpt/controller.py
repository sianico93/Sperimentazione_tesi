from models import ApparecchiatureElettronicheModel
 
class ApparecchiatureElettronicheController:
    def get_elettroniche_by_resolution(self):
        model = ApparecchiatureElettronicheModel()
        results = model.get_elettroniche_by_resolution()
        return results