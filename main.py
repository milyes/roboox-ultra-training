import time
import subprocess
import json
import asyncio

# ==================== ENERGY MANAGER ====================
class EnergyManager:
    def __init__(self):
        self.min_battery = 25

    def get_battery_info(self):
        try:
            cmd = ["/data/data/com.termux/files/usr/bin/termux-battery-status"]
            result = subprocess.check_output(cmd, stderr=subprocess.PIPE, timeout=5)
            data = json.loads(result.decode('utf-8'))
            return data.get('percentage', 50), data.get('status', 'UNKNOWN'), data.get('temperature', 30.0)
        except:
            return 50, "UNKNOWN", 30.0

    def sleep_smart(self, task_level=0):
        battery, status, temp = self.get_battery_info()
        is_charging = "CHARGING" in status or "FULL" in status

        if battery < self.min_battery and not is_charging:
            mode = "ULTRA_LOW"
            sleep_time = 2.5
            print(f"⚠️  [ENERGY] Batterie faible ({battery}%) → ULTRA_LOW")
        elif task_level == 0:
            mode = "LOW"
            sleep_time = 1.2
        elif task_level == 1:
            mode = "NORMAL"
            sleep_time = 0.4 if is_charging else 0.7
        else:
            mode = "HIGH"
            sleep_time = 0.1 if is_charging else 0.4

        if temp > 38.0:
            sleep_time = min(sleep_time * 1.8, 2.5)
            print(f"🔥 [ENERGY] Température élevée ({temp}°C) → Sleep augmenté")

        print(f"🔋 [ENERGY] Batterie: {battery}% | Charge: {status} | Mode: {mode} | Sleep: {sleep_time:.2f}s")
        time.sleep(sleep_time)
        return mode, battery

# ==================== BOOT SCREEN ====================
def show_boot_screen():
    print("\n" + "="*70)
    print("🤖 ROBOOX ULTRA - IA_ZPUCE_CORE v9.1")
    print("Fondateur : Mohammed Ilyes Zoubirou")
    print("Site officiel : https://netsecurepropro.ca")
    print("Mode : LOCAL AUTONOME | Souveraineté : LOCAL_ONLY")
    print("="*70)
    print("")
    
    print("NETSECUREPRO IA - IA_ZPUCE_CORE")
    print(f"Fondateur : Mohammed Ilyes Zoubirou")
    print(f"Email     : MILYES@NETSECUREPRO.CA")
    print(f"Version   : 9.1.0 | Souveraineté : LOCAL_ONLY")
    print("="*70)
    
    print("\n🚀 ROBOOX ULTRA - Mode LOCAL AUTONOME activé")
    print("Perception locale : ACCEPTED")
    print("Ledger scellé     : 20213f069ded...")
    print("✅ ROBOOX ULTRA est AUTONOME et LOCAL_ONLY")
    print("Prêt pour la Phase 2 (Module ZPUCE physique ESP32)")
    print("="*70 + "\n")

# ==================== MAIN ====================
async def main():
    show_boot_screen()
    
    energy = EnergyManager()
    print("✅ Energy Manager activé - Gestion intelligente de la batterie\n")
    
    task_level = 0
    
    while True:
        # Ici tu mets ton code de perception, décision, etc.
        print("🔄 Perception en cours...")
        
        # Exemple : augmenter le task_level si tu détectes quelque chose
        # task_level = 2 si tâche lourde, sinon 0 ou 1
        
        # Gestion intelligente de l'énergie
        mode, battery = energy.sleep_smart(task_level)
        
        if battery < 15 and "CHARGING" not in str(subprocess.check_output(["/data/data/com.termux/files/usr/bin/termux-battery-status"])):
            print("⚠️ Batterie très basse - Passage en mode économie maximale")

if __name__ == "__main__":
    asyncio.run(main())

	
