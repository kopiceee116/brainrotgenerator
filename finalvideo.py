import ffmpeg
import os
import subprocess

def getVideoFiles(videoFolderpath):
    video_files = []
    for x in os.listdir(videoFolderpath):
        video_files.append(os.path.join(videoFolderpath,x))
    return video_files

def concatenate_videos(video_files, output_file):
    output_file = os.path.join("result",output_file)
    if not os.path.exists('result'):
        os.mkdir('result')
    if os.path.exists(output_file):
        os.remove(output_file)
    # Create a temporary file to store the list of video files
    with open('filelist.txt', 'w') as f:
        for video_file in video_files:
            f.write("file '{}'\n".format(video_file))
    
    # Run ffmpeg command to concatenate the videos
    subprocess.run(['ffmpeg', '-f', 'concat', '-safe', '0', '-i', 'filelist.txt', '-c', 'copy', output_file], check=True)
    
    # Remove the temporary file
    os.remove('filelist.txt')