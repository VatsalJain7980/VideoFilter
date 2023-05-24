import os
import shutil

video_directory = '/home/vatsal/Music/orig_count_videos'
destination_directory = '/home/vatsal/Music/24-05-2023/'
video_list_file = '/home/vatsal/Music/time_stamp.txt'

# Read the video list from the text file
with open(video_list_file, 'r') as file:
    video_list = file.read().splitlines()


# Iterate over each video in the list
for video_name in video_list:
    # Search for the video in the directory
    for root, dirs, files in os.walk(video_directory):
        for file in files:
            if file == video_name:
                video_path = os.path.join(root, file)
                print("Video Found", video_list_file)
                destination_path = os.path.join(destination_directory, file)
                # Copy the video file to the destination directory
                shutil.copyfile(video_path, destination_path)
                print("Video copied:", destination_path)
