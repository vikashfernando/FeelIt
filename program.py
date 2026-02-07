import time
from playsound import playsound
import webbrowser
import os

start = input("Do you want to start the program? (y/n): ")

if start.lower() != "y":
    print("Good bye 👋")
    exit()

print("\nUse headphones 🎧")
time.sleep(1)
print("Set volume to 80% 🔊")
time.sleep(1)

ready = input("\nAre you ready? (y/n): ")

if ready.lower() != "y":
    print("Program stopped.")
    exit()

print("\nPlaying music...")
playsound("music.mp3")

print("\nClose your eyes...")
time.sleep(2)
print("Feel the sound...")
time.sleep(2)
print("Let your heart listen...")
time.sleep(2)

image_path = os.path.abspath("image.jpg")
webbrowser.open(image_path)
