# ============================================================
#   ROBOOX ULTRA — Domain Router v2.0
#   NetSecurePro IA — Code source privé
#   Tous droits réservés — Z-H202.IA
# ============================================================

class DomainRouter:

    DOMAINS = {
        "MEDICAL":    "Protocole H202.IA/HIPAA activé. Analyse constantes vitales.",
        "INDUSTRIAL": "Précision millimétrique. Sécurité machines lourdes activée.",
        "DOMESTIC":   "Optimisation confort et assistance quotidienne.",
        "SECURITY":   "NetSecurePro Shield alerte maximale. Scan périmètre actif.",
    }

    # Mots-clés par domaine — ordre de priorité : MEDICAL > SECURITY > DOMESTIC > INDUSTRIAL
    _KEYWORDS = {
        "MEDICAL": [
            "patient", "symptôme", "vital", "bpm", "tension",
            "température", "médical", "diagnostic", "h202", "tremblement",
            "fréquence cardiaque", "douleur", "pression"
        ],
        "SECURITY": [
            "anomalie", "intrusion", "menace", "alerte", "attaque",
            "scan", "breach", "unauthorized", "threat", "danger"
        ],
        "DOMESTIC": [
            "utilisateur", "maison", "chambre", "cuisine", "confort",
            "lumière", "température ambiante", "assistant"
        ],
    }

    def __init__(self):
        self._history = []

    def route(self, perception_data: dict) -> str:
        raw = str(perception_data).lower()

        # Détection par priorité
        for domain, keywords in self._KEYWORDS.items():
            if any(kw.lower() in raw for kw in keywords):
                self._log(domain, perception_data)
                return domain

        # Défaut
        self._log("INDUSTRIAL", perception_data)
        return "INDUSTRIAL"

    def describe(self, domain: str) -> str:
        return self.DOMAINS.get(domain, "Domaine inconnu.")

    def _log(self, domain: str, data: dict):
        entry = {
            "domain": domain,
            "keys": list(data.keys()) if isinstance(data, dict) else [],
        }
        self._history.append(entry)
        if len(self._history) > 100:
            self._history = self._history[-100:]

    def history(self) -> list:
        return self._history[-10:]

    def stats(self) -> dict:
        from collections import Counter
        counts = Counter(e["domain"] for e in self._history)
        return dict(counts)


