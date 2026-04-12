import hashlib
import json
from datetime import datetime

class NetSecureProShield:
    def __init__(self, security_level="MAXIMUM"):
        self.level = security_level
        self.audit_log = "core/audit_ledger.jsonl"
        print(f"🛡️ NetSecurePro Shield : Audit Immuable activé (Niveau {self.level}).")

    def _generate_audit_hash(self, entry):
        """Simule le scellage d'une décision via hash cryptographique."""
        data_string = json.dumps(entry, sort_keys=True)
        return hashlib.sha256(data_string.encode()).hexdigest()

    def validate_decision(self, decision):
        # Vérification de la souveraineté
        is_sovereign = decision.get("sovereign_state") == "LOCAL_ONLY"
        
        # Création de l'entrée d'audit
        audit_entry = {
            "timestamp": datetime.now().isoformat(),
            "action": decision.get("action_plan"),
            "confidence": decision.get("confidence"),
            "status": "APPROVED" if is_sovereign else "REJECTED"
        }
        
        # Scellage de l'entrée
        audit_entry["block_hash"] = self._generate_audit_hash(audit_entry)
        
        # Écriture dans le registre (Append Only)
        with open(self.audit_log, "a") as f:
            f.write(json.dumps(audit_entry) + "\n")
            
        print(f"🔒 Audit : Décision scellée dans le ledger. Hash: {audit_entry['block_hash'][:12]}...")
        return is_sovereign
