import os
from moviepy.editor import VideoFileClip, clips_array

def convert_horizontal_to_vertical(input_file, output_file):
    # Load the video clip
    clip = VideoFileClip(input_file)

    # Define the region to keep
    width, height = clip.size
    x_center = width // 2
    y_center = height // 2
    new_width = height * 9 // 16  # 9:16 aspect ratio for vertical videos
    x1 = x_center - (new_width // 2)
    x2 = x_center + (new_width // 2)

    # Crop the clip to keep the central portion
    cropped_clip = clip.crop(x1=x1, y1=0, x2=x2, y2=height)

    # Add black bars on top and bottom to maintain aspect ratio
    black_bar = clips_array([[cropped_clip], [cropped_clip]])
    
    # Write the processed clip to a new file
    black_bar.write_videofile(output_file, codec="libx264", audio_codec="aac")

    
input_file = os.path.join('result','output.mp4')
output_file = "vertical_video.mp4"
convert_horizontal_to_vertical(input_file, output_file)
