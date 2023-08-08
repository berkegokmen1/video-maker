from cv2 import FONT_HERSHEY_SIMPLEX as FONT

class VideoMakerOptions:
    IMAGE_FOLDER = "../named-images/"
    OUTPUT_VIDEO = "output_video.mp4"


class ImageGetterOptions:
    NUM_IMAGES = 10
    UNSPLASH_URL = "https://source.unsplash.com/random/1920x1080"
    DOWNLOAD_DIRECTORY = '../downloaded-images/'
    OLD_IMAGES_DIRECTORY = '../old-images/'


class NameWriterOptions:
    FONT = FONT
    FONT_SCALE = 4
    FONT_THICKNESS = 8
    BORDER_THICKNESS = 16
    TEXT_COLOR_WHITE = (255, 255, 255)
    BORDER_COLOR = (0, 0, 0) 
    INPUT_IMAGE_FOLDER = "../downloaded-images/"
    OUTPUT_IMAGE_FOLDER = "../named-images/"
