from TTS.api import TTS
import torch
import os
import pathlib
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
            tts.tts_to_file(text=line, file_path=os.path.join(home_dir, "hang",f"sor{i}.wav"))
            i+=1

hangkeszites(szetszedes.szetszedes(karcolas.szeddkiaszoveget("https://www.reddit.com/r/BinIchDasArschloch/comments/1cj2xa4/bida_wenn_ich_auf_meine_pause_bestehe/")))
