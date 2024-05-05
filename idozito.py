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

    return round(TotalTimeTalking,1)

def findStartingPoint(videoPath :str,audioFolderPath :str) -> int:
    return 100
    return random.randint(1,round(VideoLength(videoPath) - totalAuidoLength(audioFolderPath) - 10))

def startandEndLengths(videoPath,audioFolderPath):
    startingPoint = findStartingPoint(videoPath,audioFolderPath)
    StartandEndPoints = []
    print(startingPoint)    
    for file in os.listdir(audioFolderPath): 
        path = os.path.join(audioFolderPath,file)
        endpoint = round(startingPoint+AudioLength(path),1)
        StartandEndPoints.append((startingPoint,endpoint))
        startingPoint = round(endpoint+0.1, 1)
    print(StartandEndPoints)
        

print(startandEndLengths('BackgroundVid.mp4','hang'))    

# Make the text. Many more options are available.
# txt_clip = ( TextClip("My Holidays 2013",fontsize=70,color='white')
#              .set_position('center')
#              .set_duration(10) )

# result = CompositeVideoClip([video, txt_clip]) # Overlay text on video
# result.write_videofile("myHolidays_edited.mp4",fps=25) # Many options...