class VoiceEngine:
    def __init__(self):
        self.engine_name = "Lyria 3 - Z-Voice"

    def synthesize(self, text):
        # Simulation de sortie vocale 30ms latence
        print(f"🔊 [VOICE]: {text}")
