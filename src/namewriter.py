import cv2
import os
import shutil

from options import NameWriterOptions

def add_filename_to_images(image_folder, output_folder):
    image_files = sorted([f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])

    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        img = cv2.imread(image_path)
        
        frame_height, frame_width = img.shape[:2]

        text = image_file.upper().split(".")[0]

        text_size = cv2.getTextSize(text, NameWriterOptions.FONT, 
                                    NameWriterOptions.FONT_SCALE, NameWriterOptions.FONT_THICKNESS)[0]
        text_x = (frame_width - text_size[0]) // 2
        text_y = frame_height - 60

        cv2.putText(img, text, (text_x, text_y),
                NameWriterOptions.FONT, NameWriterOptions.FONT_SCALE, NameWriterOptions.BORDER_COLOR, 
                NameWriterOptions.BORDER_THICKNESS, cv2.LINE_AA)
        
        cv2.putText(img, text, (text_x, text_y),
                NameWriterOptions.FONT, NameWriterOptions.FONT_SCALE, NameWriterOptions.TEXT_COLOR_WHITE, 
                NameWriterOptions.FONT_THICKNESS, cv2.LINE_AA)

        output_path = os.path.join(output_folder, image_file)
        cv2.imwrite(output_path, img)

        print(f"Added name: {image_file}")

if __name__ == "__main__":
    os.makedirs(NameWriterOptions.INPUT_IMAGE_FOLDER, exist_ok=True)
    os.makedirs(NameWriterOptions.OUTPUT_IMAGE_FOLDER, exist_ok=True)
    shutil.rmtree(NameWriterOptions.OUTPUT_IMAGE_FOLDER)  # reset the folder contents
    os.makedirs(NameWriterOptions.OUTPUT_IMAGE_FOLDER, exist_ok=True)
    add_filename_to_images(NameWriterOptions.INPUT_IMAGE_FOLDER, NameWriterOptions.OUTPUT_IMAGE_FOLDER)
