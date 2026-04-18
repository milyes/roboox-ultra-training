#!/bin/bash
# start_roboox.sh — Boot Global Z-H202.ia
# Fondateur : Mohammed Ilyes Zoubirou | NetSecurePro IA

BASE="$HOME/roboox-ultra-training"
cd "$BASE"

echo "=================================================="
echo "  🚀 Z-H202.ia — BOOT SOUVERAIN ROBOOX ULTRA"
echo "  Fondateur : Mohammed Ilyes Zoubirou"
echo "  Mode      : GHOST / FULL AUTONOME"
echo "=================================================="

# 1. Génère dashboard frais
echo "⬡ [1/3] Génération dashboard..."
python3 "$BASE/generate_dashboard.py"

# 2. Intégration Zpuce
echo "⬡ [2/3] Intégration Zpuce..."
python3 "$HOME/Zpuce_integration.py"

# 3. Rapport d'état
echo "⬡ [3/3] Rapport d'état..."
python3 "$BASE/status_report.py"

# 4. Lance sentinel en background
echo "⬡ [4/4] Sentinel Pulse en arrière-plan..."
nohup python3 "$BASE/sentinel_pulse.py" > "$BASE/logs/sentinel.log" 2>&1 &
echo "   PID Sentinel : $!"
echo "=================================================="
echo "✅ Z-H202.ia OPÉRATIONNEL"
echo "=================================================="
