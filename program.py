import sys
import os

def resource_path(file_name):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, file_name)
    return os.path.join(os.path.abspath("."), file_name)

music = resource_path("music.mp3")
image = resource_path("image.jpg")
