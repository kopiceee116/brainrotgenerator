from TTS.api import TTS
import torch, os, pathlib
import szetszedes, karcolas

def hangkeszites(fajlnev):
    
    home_dir = os.getcwd()
    audioOutPath = os.path.join(home_dir, "hang")
    if not os.path.exists(audioOutPath):
        os.mkdir(audioOutPath)

    device = "cuda" if torch.cuda.is_available() else "cpu"
    tts = TTS(model_name="tts_models/de/thorsten/tacotron2-DDC", progress_bar=False).to(device)

    with open(fajlnev,"r",encoding="utf-8") as fajl:
        szoveg = fajl.read()
    i=1

    for line in szoveg.split("\n"):
        if len(line) <3:
            continue
        else:
            displayi = i
            if displayi < 10:
                displayi = f"0{i}"
            tts.tts_to_file(text=line, file_path=os.path.join(home_dir, "hang",f"{displayi}.wav"))
            i+=1
