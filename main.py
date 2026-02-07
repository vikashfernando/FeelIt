import time
import webbrowser
import os
import sys
import pygame

# -------- Helper to get correct folder for EXE --------
def resource_path(filename):
    if getattr(sys, 'frozen', False):  # running as EXE
        folder = sys._MEIPASS
    else:
        folder = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(folder, filename)

# -------- Ask to start --------
start = input("Do you want to start the program? (y/n): ")

if start.lower() != "y":
    print("Good bye 👋")
    exit()

# -------- Instructions --------
print("\nPlease use headphones 🎧")
time.sleep(1)
print("Set volume to 80% 🔊")
time.sleep(1)

ready = input("\nAre you ready? (y/n): ")

if ready.lower() != "y":
    print("Program stopped.")
    exit()

# -------- Initialize Pygame for music --------
pygame.mixer.init()
music_file = resource_path("music.mp3")
pygame.mixer.music.load(music_file)
pygame.mixer.music.play()  # play in background

# -------- Show lyrics while song plays --------
lyrics = [
    ("Close your eyes...", 2),
    ("Feel the music...", 3),
    ("Let your heart listen...", 4)
]

for line, delay in lyrics:
    print(line)
    time.sleep(delay)

# -------- Wait until music finishes --------
while pygame.mixer.music.get_busy():
    time.sleep(1)

# -------- Open image --------
image_file = resource_path("image.jpg")
webbrowser.open(image_file)

print("\nProgram finished! 🎵🖼️")
