import time
from playsound import playsound
import webbrowser
import os

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

# Play music
print("\nPlaying music...")
playsound("music.mp3")

# Show text with time
print("\nClose your eyes...")
time.sleep(2)

print("Feel the music...")
time.sleep(2)

print("Let your heart listen...")
time.sleep(2)

# Open image
print("\nOpening image...")
image_path = os.path.abspath("image.jpg")
webbrowser.open(image_path)
