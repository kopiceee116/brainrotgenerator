from TTS.api import TTS
import torch
def szovegkeszites(fajlnev):
    with open(fajlnev,"r",encoding="utf-8") as fajl:
        # Init TTS with the target model name
        i=1
        device = "cuda" if torch.cuda.is_available() else "cpu"
        tts = TTS(model_name="tts_models/de/thorsten/tacotron2-DDC", progress_bar=False).to(device)
        for line in fajl.split("\n"):
        # Run TTS
            tts.tts_to_file(text=line, file_path=f"sor{i}.wav")
            i+=1

        # # Example voice cloning with YourTTS in English, French and Portuguese
        # tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", progress_bar=False).to(device)
        # tts.tts_to_file("This is voice cloning.", speaker_wav="my/cloning/audio.wav", language="en", file_path="output.wav")
        # tts.tts_to_file("C'est le clonage de la voix.", speaker_wav="my/cloning/audio.wav", language="fr-fr", file_path="output.wav")
        # tts.tts_to_file("Isso é clonagem de voz.", speaker_wav="my/cloning/audio.wav", language="pt-br", file_path="output.wav")