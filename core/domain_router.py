class DomainRouter:
    def __init__(self):
        self.domains = {
            "MEDICAL": "Protocole HIPAA/Santé activé. Analyse des constantes.",
            "INDUSTRIAL": "Précision millimétrique. Sécurité machines lourdes.",
            "DOMESTIC": "Optimisation confort et assistance quotidienne.",
            "SECURITY": "NetSecurePro Shield en alerte maximale. Scan périmètre."
        }

    def route(self, perception_data):
        # Analyse simple pour choisir le domaine
        if "Utilisateur" in str(perception_data):
            return "DOMESTIC"
        if "Anomalie" in str(perception_data):
            return "SECURITY"
        return "INDUSTRIAL" # Par défaut
