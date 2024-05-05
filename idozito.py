from moviepy.editor import *
import wave, contextlib, os
import random #to have random starting point in video :)

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
    timeStamps = StartandEndPoints(videoPath,audioFolderPath)
    BigVideo = VideoFileClip(videoPath)
    with open(subtitlesPath,"r",encoding="utf-8") as feliratFajl:
        feliratok = feliratFajl.read().split("\n")
    AudioPaths = []
    for file in os.listdir(audioFolderPath): 
        path = os.path.join(audioFolderPath,file)
        AudioPaths.append(path)
    for sor in range(len(feliratok)):    
        clip = BigVideo.subclip(round(timeStamps[sor][0],2),round(timeStamps[sor][1],2))
        audio = AudioFileClip(AudioPaths[sor])

        txt_clip = (TextClip(feliratok[sor],fontsize=16,color='white',font="Segoe-UI-Bold")
                    .set_position('center')
                    .set_duration(AudioLength(AudioPaths[sor])))
        result = clip.set_audio(AudioPaths[sor])
        result = CompositeVideoClip([clip, txt_clip]) # Overlay text on video
        result.write_videofile(f"video{sor+1}.mp4",fps=25,audio_codec="aac") # Many options...
    

makeVids('BackgroundVid.mp4','split.txt','hang')