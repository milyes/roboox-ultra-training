import asyncio
from core.ia22_logic_full import IA22LogicKernel
from core.netsecurepro_shield import NetSecureProShield
from core.perception_fusion import PerceptionFusion
from core.domain_router import DomainRouter
from core.voice_engine import VoiceEngine

async def run_roboox():
    print("--- ROBOOX ULTRA : MODE FULL DOMAIN ACTIVÉ ---")
    
    # Init
    brain = IA22LogicKernel()
    shield = NetSecureProShield()
    vision = PerceptionFusion()
    router = DomainRouter()
    voice = VoiceEngine()
    
    # 1. Perception
    perception = vision.get_environment_snapshot()
    
    # 2. Routage de Domaine
    current_domain = router.route(perception)
    print(f"🌐 Domaine Détecté : {current_domain}")
    
    # 3. Cycle IA22
    decision = await brain.process_cycle(perception)
    
    # 4. Action & Synthèse Vocale
    if shield.validate_decision(decision):
        action = decision['action_plan']
        print(f"✅ ACTION : {action}")
        voice.synthesize(f"J'exécute la {action} en mode {current_domain}.")
    
    print("\n--- SYSTÈME EN ATTENTE DE NOUVELLE PERCEPTION ---")

if __name__ == "__main__":
    asyncio.run(run_roboox())
