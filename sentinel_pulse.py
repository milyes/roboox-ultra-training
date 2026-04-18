# sentinel_pulse.py — Z-H202 GHOST SOUVERAIN
# Fondateur : Mohammed Ilyes Zoubirou | NetSecurePro IA
# v2.0 — Energy Manager intégré

import json, time, os
from datetime import datetime
from energy_manager import EnergyManager

BASE = os.path.dirname(os.path.abspath(__file__))
LEDGER_PATH  = os.path.join(BASE, "core/audit_ledger.jsonl")
MEMORY_PATH  = os.path.join(BASE, "memory.json")

energy = EnergyManager()

def log_decision(action, status, extra=None):
    os.makedirs(os.path.dirname(LEDGER_PATH), exist_ok=True)
    try:
        decision_id = sum(1 for _ in open(LEDGER_PATH)) + 1
    except FileNotFoundError:
        decision_id = 1

    entry = {
        "id": decision_id,
        "action": action,
        "status": status,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    if extra:
        entry.update(extra)

    with open(LEDGER_PATH, "a") as f:
        f.write(json.dumps(entry) + "\n")

    # Sync memory.json
    if os.path.exists(MEMORY_PATH):
        with open(MEMORY_PATH, "r+") as f:
            data = json.load(f)
            data["decisions"] = data.get("decisions", 0) + 1
            data["last_sync"] = entry["timestamp"]
            f.seek(0); json.dump(data, f, indent=4); f.truncate()

    return decision_id

def run_sentinel():
    print("🚀 --- DÉMARRAGE SENTINEL PULSE (Z-H202) v2.0 ---")
    print("📡 Mode: GHOST / SOUVERAIN | Energy Manager: ACTIF")

    cycle = 0
    try:
        while True:
            cycle += 1

            # Lecture énergie réelle
            mode, sleep_time, battery, charging = energy.get_recommended_mode(task_level=0)

            # Détermination shield
            if battery < 20 and not charging:
                shield = "CRITIQUE"
            elif battery < energy.min_battery_threshold and not charging:
                shield = "RÉDUIT"
            else:
                shield = "MAXIMUM"

            ts = datetime.now().strftime('%H:%M:%S')
            charge_icon = "⚡" if charging else "🔋"
            print(f"[{ts}] Cycle#{cycle} | {charge_icon} {battery}% | Shield: {shield} | Mode: {mode} | Sleep: {sleep_time:.2f}s")

            # Log toutes les 5 minutes (cycle ~60s)
            if cycle % 5 == 0:
                log_decision("GHOST_HEARTBEAT", "STABLE", {
                    "battery": battery,
                    "energy_mode": mode,
                    "shield": shield,
                    "charging": charging
                })

            # Update memory shield
            if os.path.exists(MEMORY_PATH):
                with open(MEMORY_PATH, "r+") as f:
                    data = json.load(f)
                    data["shield"] = shield
                    data["battery"] = battery
                    f.seek(0); json.dump(data, f, indent=4); f.truncate()

            time.sleep(60)

    except KeyboardInterrupt:
        print("\n🛑 Sentinel interrompu.")
        log_decision("SENTINEL_STOP", "INTERRUPTED")

if __name__ == "__main__":
    run_sentinel()
