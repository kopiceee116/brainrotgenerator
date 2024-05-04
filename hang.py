from TTS.api import TTS
import torch

# Init TTS with the target model name
device = "cuda" if torch.cuda.is_available() else "cpu"
tts = TTS(model_name="tts_models/de/thorsten/tacotron2-DDC", progress_bar=False).to(device)

szoveg = """Bida wenn ich auf meine Pause bestehe?
Hey, ich hab folgendes Thema und dazu die Frage Bida?

Ich arbeite seit einer Zeit in einem großen Unternehmen. Die Nachtschicht Pause wird durchbezahlt, deswegen beschwer ich mich nicht, wenn ich meine Pause unterbrechen muss oder sonst was. Während der Früh oder Spätschicht in normalerweise noch jemand in der Tag Schicht da, der die Pausen der beiden Schichten übernimmt.

Das funktioniert nur solange bis jemand krank ist oder im Urlaub ist. Dann muss ich jemanden suchen der meine Pause übernimmt. Dann hat mal die erste Person viel zutun und kann nicht, die zweite evtl auch und dann geht's hin und her bis jemand dann doch Zeit hat zum übernehmen.

Das geht dann jeden Tag so, das ich hin und her laufe und aktiv suchen muss wer mich solange vertritt. Wenn ich niemanden Frage, kann ich auch keine Pause machen, da die Maschinellen Abläufe hier auf mein handeln angewiesen sind. Mir kommt es vor als würde ich denjenigen auf den Sack gehen mit meiner Pause. Alle machen ihre Pause und müssen niemanden dafür einspringen lassen, bei mir geht es nicht anders. Bida wenn ich jeden Tag auf meine Pause bestehe?"""




# Run TTS
tts.tts_to_file(text=szoveg, file_path="output.wav")

# # Example voice cloning with YourTTS in English, French and Portuguese
# tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", progress_bar=False).to(device)
# tts.tts_to_file("This is voice cloning.", speaker_wav="my/cloning/audio.wav", language="en", file_path="output.wav")
# tts.tts_to_file("C'est le clonage de la voix.", speaker_wav="my/cloning/audio.wav", language="fr-fr", file_path="output.wav")
# tts.tts_to_file("Isso é clonagem de voz.", speaker_wav="my/cloning/audio.wav", language="pt-br", file_path="output.wav")