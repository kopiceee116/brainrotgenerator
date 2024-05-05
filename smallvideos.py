from moviepy.editor import *
import wave, contextlib, os
import random #to have random starting point in video :)
def makeVideoFolder(whereToPutVideo):
    if not os.path.exists(whereToPutVideo):
        os.mkdir(whereToPutVideo)

def VideoLength(videofilepath):
    bigVideo = VideoFileClip(videofilepath)
    BigVideoLength = bigVideo.duration
    return(BigVideoLength)

def AudioLength(filename):
    with contextlib.closing(wave.open(filename,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        return round(duration+0.1,1)

def totalAuidoLength(folder :str) -> float:
    TotalTimeTalking = 0
    for file in os.listdir(folder): 
        path = os.path.join(folder,file)
        TotalTimeTalking+=AudioLength(path)
    print(TotalTimeTalking)
    return round(TotalTimeTalking,2)

def findStartingPoint(videoPath :str,audioFolderPath :str) -> int:
    return random.randint(1,round(VideoLength(videoPath) - totalAuidoLength(audioFolderPath) - 10))

def StartandEndPoints(videoPath,audioFolderPath):
    startingPoint = findStartingPoint(videoPath,audioFolderPath)
    StartandEndPoints = []
    print(startingPoint)    
    for file in os.listdir(audioFolderPath): 
        path = os.path.join(audioFolderPath,file)
        endpoint = round(startingPoint+AudioLength(path),1)
        StartandEndPoints.append((startingPoint,endpoint))
        startingPoint = round(endpoint+0.01, 2)
    return StartandEndPoints

def makeVids(videoPath,subtitlesPath,audioFolderPath):
    videoFolderPath="Videos"
    makeVideoFolder(videoFolderPath)
    timeStamps = StartandEndPoints(videoPath,audioFolderPath)
    BigVideo = VideoFileClip(videoPath)
    print("idopont es video megva")
    with open(subtitlesPath,"r",encoding="utf-8") as feliratFajl:
        feliratok = feliratFajl.read().split("\n")
    print("feliratok megvannak")
    AudioPaths = []
    AudioFiles = sorted(os.listdir(audioFolderPath))
    for file in AudioFiles: 
        path = os.path.join(audioFolderPath,file)
        AudioPaths.append(path)
    print("hangok megvannak")
    for sor in range(len(feliratok)):
        if sor == len(timeStamps): break
        clip = BigVideo.subclip(round(timeStamps[sor][0],2),round(timeStamps[sor][1],2))
        
        audio_clip = AudioFileClip(AudioPaths[sor])
        print(sor)
        print(AudioPaths[sor])

        txt_clip = (TextClip(feliratok[sor],fontsize=30,color='white',font="Segoe-UI-Bold",stroke_color="black",stroke_width=2)
                    .set_position('center')
                    .set_duration(AudioLength(AudioPaths[sor])))
        result = clip.set_audio(audio_clip)
        gecimar = CompositeVideoClip([result, txt_clip]) 
        displaynum = sor+1
        if displaynum < 10:
            displaynum = f"0{displaynum}"
        gecimar.write_videofile(os.path.join(videoFolderPath,f"{displaynum}.mp4"),fps=24,audio_codec="aac", logger=None)