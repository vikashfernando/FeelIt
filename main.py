import time
import webbrowser
import os
import pygame  # new

# Ask user to start
start = input("Do you want to start the program? (y/n): ")

if start.lower() != "y":
    print("Good bye 👋")
    exit()

# Instructions
print("\nPlease use headphones 🎧")
time.sleep(1)
print("Set volume to 80% 🔊")
time.sleep(1)

# Ask if ready
ready = input("\nAre you ready? (y/n): ")

if ready.lower() != "y":
    print("Program stopped.")
    exit()

# Initialize pygame mixer
pygame.mixer.init()
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play()  # plays in background

print("\nClose your eyes...")
time.sleep(5)

print("Feel the music...")
time.sleep(2)

print("Let your heart listen...")
time.sleep(2)

print("Let your heart listen...")
time.sleep(2)

print("Let your heart listen...")
time.sleep(2)

print("Let your heart listen...")
time.sleep(2)

# Wait until music finishes
while pygame.mixer.music.get_busy():
    time.sleep(1)

# Open image
print("\nOpening image...")
image_path = os.path.abspath("image.jpg")
webbrowser.open(image_path)
