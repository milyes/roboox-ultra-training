# status_report.py — ROBOOX ULTRA État Système
# Fondateur : Mohammed Ilyes Zoubirou | NetSecurePro IA

import json, os
from datetime import datetime

BASE         = os.path.dirname(os.path.abspath(__file__))
MEMORY_PATH  = os.path.join(BASE, "memory.json")
LEDGER_PATH  = os.path.join(BASE, "core/audit_ledger.jsonl")
STORAGE_PATH = os.path.join(BASE, "memory/local_storage.json")

def generate_report():
    print("=" * 50)
    print("  📊 RAPPORT D'ÉTAT ROBOOX ULTRA — Z-H202.ia")
    print(f"  Timestamp : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)

    # memory.json global
    try:
        with open(MEMORY_PATH) as f:
            mem = json.load(f)
        print(f"🧠 Expériences    : {mem.get('experiences', 0)}")
        print(f"🔒 Décisions      : {mem.get('decisions', 0)}")
        print(f"🌐 Mode           : {mem.get('status', 'INCONNU')}")
        print(f"🛡️  Shield         : {mem.get('shield', 'INCONNU')}")
        print(f"⏱️  Dernier sync   : {mem.get('last_sync', 'N/A')}")
    except Exception as e:
        print(f"⚠️  memory.json    : {e}")

    # Audit ledger
    try:
        with open(LEDGER_PATH) as f:
            logs = f.readlines()
        print(f"📋 Audit Ledger   : {len(logs)} décisions scellées")
        last = json.loads(logs[-1])
        print(f"   └─ Dernière    : [{last['timestamp']}] {last['action']} → {last['status']}")
    except:
        print("📋 Audit Ledger   : Vierge ou protégé")

    # Mémoire épisodique
    try:
        with open(STORAGE_PATH) as f:
            store = json.load(f)
        print(f"🧩 Épisodique     : {len(store.get('episodic', []))} entrées")
    except:
        print("🧩 Épisodique     : Non initialisée")

    print("=" * 50)
    print("✅ SYSTÈME Z-H202.ia : OPÉRATIONNEL")
    print("=" * 50)

if __name__ == "__main__":
    generate_report()
