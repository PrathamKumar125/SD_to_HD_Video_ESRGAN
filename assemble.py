import cv2
import os

def assemble_video(frames_folder, output_path, fps=5):
    # Get all frames from the folder
    frames = [os.path.join(frames_folder, frame) for frame in os.listdir(frames_folder) if frame.endswith('.png')]
    frames.sort()  # Sort frames to ensure they are in the correct order

    # Determine the dimensions of the frames (assuming they are the same for all)
    sample_frame = cv2.imread(frames[0])
    height, width, layers = sample_frame.shape

    # Initialize video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # codec for MP4
    video_writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    # Add frames to the video
    for frame in frames:
        img = cv2.imread(frame)
        video_writer.write(img)

    # Release the video writer
    video_writer.release()
    print(f'Video assembled and saved at {output_path}')

# Define paths
frames_folder = 'ESRGAN/results/'
output_path = 'final_hd_video.mp4'

# Assemble the video
assemble_video(frames_folder, output_path)