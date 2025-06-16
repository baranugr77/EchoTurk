from TTS.api import TTS

# Coqui TTS modelini yükle
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)

def generate_tts(text, lang="en"):
    if not text.strip():
        return

    try:
        output_path = "static/output.wav"
        tts.tts_to_file(text=text, file_path=output_path)
        return output_path
    except Exception as e:
        print(f"TTS hatası: {e}")
        return None
