import json
import os
from datetime import datetime

class MemoryFabric:
    def __init__(self, storage_path="memory/local_storage.json"):
        self.storage_path = storage_path
        self.memory_map = self._load_memory()

    def _load_memory(self):
        if os.path.exists(self.storage_path):
            with open(self.storage_path, 'r') as f:
                return json.load(f)
        return {"episodic": [], "semantic": {}, "context_cache": []}

    def save_experience(self, action, result, confidence):
        """Enregistre une mémoire épisodique (Life Experience)"""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "result": result,
            "confidence": confidence
        }
        self.memory_map["episodic"].append(entry)
        self._persist()
        print(f"💾 Memory Fabric : Nouvelle expérience épisodique archivée.")

    def get_context_rag(self):
        """Simule l'injection de contexte (RAG) pour le cycle IA22"""
        if not self.memory_map["episodic"]:
            return "Première initialisation : aucun historique."
        last_exp = self.memory_map["episodic"][-1]
        return f"Dernière action réussie : {last_exp['action']} (Confiance: {last_exp['confidence']})"

    def _persist(self):
        with open(self.storage_path, 'w') as f:
            json.dump(self.memory_map, f, indent=4)
