import cv2
import os

from options import VideoMakerOptions

def create_transitioned_video(image_folder, output_path, transition_duration=20, image_duration=100):
    image_files = sorted([f.lower() for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])
    image_paths = [os.path.join(image_folder, img) for img in image_files]

    frame_height, frame_width = cv2.imread(image_paths[0]).shape[:2]
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, 30, (frame_width, frame_height))

    for i in range(len(image_paths) - 1):
        img1 = cv2.imread(image_paths[i])
        img2 = cv2.imread(image_paths[i + 1])

        for t in range(transition_duration + 1):
            alpha = 1.0 - t / transition_duration
            blended = cv2.addWeighted(img1, alpha, img2, 1 - alpha, 0)
            out.write(blended)
        
        for _ in range(image_duration):
            out.write(img2)

        print(f"Processed to video: {image_files[i]}")

    out.release()

if __name__ == "__main__":
    create_transitioned_video(VideoMakerOptions.IMAGE_FOLDER, VideoMakerOptions.OUTPUT_VIDEO)
