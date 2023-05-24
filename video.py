import os
import re
import shutil

video_directory = '/home/vatsal/PycharmProjects/VideoFilter/orig_count_videos'
destination_directory = '/home/vatsal/PycharmProjects/VideoFilter/24-05-2023'
video_list_file = '/home/vatsal/PycharmProjects/VideoFilter/time_stamp.txt'
timestamp_pattern = r"\d{4}-\d{2}-\d{2}-\d{2}"
with open(video_list_file, 'r') as file:
    video_list = file.read().splitlines()
for video_name in video_list:
    for filename in os.listdir(video_directory):
        file_path = os.path.join(video_directory, filename)

        if os.path.isfile(file_path) and any(file_path.lower().endswith(ext) for ext in ['.mp4']):
            match = re.search(timestamp_pattern, filename)
            if match:
                timestamp = match.group(0)
                destination_path = os.path.join(destination_directory, filename)
                shutil.copyfile(file_path, destination_path)
                print("Video file copied:", filename)
                print("Timestamp:", timestamp)
            #         if file == video_name:
            #             video_path = os.path.join(root, file)
            #             destination_path = os.path.join(destination_directory, file)
            #             # Copy the video file to the destination directory
            #             shutil.copyfile(video_path, destination_path)
            #             print("Video copied:", destination_path)
