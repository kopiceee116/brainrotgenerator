from moviepy.editor import *
import wave
import contextlib
import os

def vido(videofilepath):
    bigVideo = VideoFileClip(videofilepath)
    BigVideoLength = bigVideo.duration
    return(BigVideoLength)

def AudioLength(filename):
    with contextlib.closing(wave.open(filename,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        return round(duration+0.02,2)

def totalAuidoLength(folder):
    TotalTimeTalking = 0
    for file in os.listdir(folder): 
        path = os.path.join(folder,file)
        TotalTimeTalking+=AudioLength(path)

    return TotalTimeTalking

print(totalAuidoLength("hang"))
# Make the text. Many more options are available.
# txt_clip = ( TextClip("My Holidays 2013",fontsize=70,color='white')
#              .set_position('center')
#              .set_duration(10) )

# result = CompositeVideoClip([video, txt_clip]) # Overlay text on video
# result.write_videofile("myHolidays_edited.mp4",fps=25) # Many options...