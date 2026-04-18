import time
import subprocess
import json
import os

class EnergyManager:
    def __init__(self):
        self.current_task_level = 0  # 0 = idle, 1 = normal, 2 = high
        self.min_battery_threshold = 25  # % en dessous duquel on passe en mode ultra bas

    def get_battery_info(self):
        """Récupère le niveau de batterie via Termux API depuis Ubuntu"""
        try:
            # Chemin vers termux-battery-status
            cmd = ["/data/data/com.termux/files/usr/bin/termux-battery-status"]
            result = subprocess.check_output(cmd, stderr=subprocess.PIPE, timeout=5)
            data = json.loads(result.decode('utf-8'))
            
            percentage = data.get('percentage', 50)
            status = data.get('status', 'UNKNOWN')  # CHARGING, DISCHARGING, FULL, etc.
            temperature = data.get('temperature', 30.0)
            
            return percentage, status, temperature
        except Exception as e:
            # En cas d'erreur (première fois ou problème d'accès), on retourne des valeurs par défaut
            return 50, "UNKNOWN", 30.0

    def get_recommended_mode(self, task_level=0):
        """Retourne le mode énergie et le temps de sleep recommandé"""
        battery, status, temp = self.get_battery_info()
        
        is_charging = "CHARGING" in status or "FULL" in status
        
        # Priorité batterie faible
        if battery < self.min_battery_threshold and not is_charging:
            mode = "ULTRA_LOW"
            sleep_time = 2.5
            print(f"⚠️  [ENERGY] Batterie faible ({battery}%) → Mode ULTRA_LOW")
        
        # Mode selon la charge de travail
        elif task_level == 0:   # Rien à faire (attente)
            mode = "LOW"
            sleep_time = 1.2
        elif task_level == 1:   # Perception / raisonnement normal
            mode = "NORMAL"
            sleep_time = 0.4 if is_charging else 0.6
        else:                   # Tâche lourde (vision, décision urgente, etc.)
            mode = "HIGH"
            sleep_time = 0.08 if is_charging else 0.35
        
        # Protection température
        if temp > 38.0:
            sleep_time = min(sleep_time * 1.8, 2.0)
            print(f"🔥 [ENERGY] Température élevée ({temp}°C) → Sleep augmenté")
        
        print(f"🔋 [ENERGY] Batterie: {battery}% | Status: {status} | Mode: {mode} | Sleep: {sleep_time:.2f}s | Task: {task_level}")
        
        return mode, sleep_time, battery, is_charging

    def sleep_smart(self, task_level=0):
        """Fonction principale à appeler dans la boucle"""
        mode, sleep_time, battery, charging = self.get_recommended_mode(task_level)
        time.sleep(sleep_time)
        return mode, battery
