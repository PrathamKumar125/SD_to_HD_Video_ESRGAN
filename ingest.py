import cv2
import os

# Create the directory if it doesn't exist
output_dir = r'ESRGAN\LR'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

VIDEO_FILE="video.mp4"
# Open the video file
video_stream = cv2.VideoCapture(VIDEO_FILE)

# Get FPS of the video
fps = video_stream.get(cv2.CAP_PROP_FPS)

frame_idx = 0
while video_stream.isOpened():
        ret, frame = video_stream.read()
        if not ret:
            break

        # Save every frame that corresponds to 5 FPS
        if frame_idx % int(fps / 10) == 0:
            frame_filename = f"frame_{frame_idx}.jpg"
            full_frame_path = os.path.join(output_dir, frame_filename)
            cv2.imwrite(full_frame_path, frame)

        frame_idx += 1

# Release the video stream
video_stream.release()
