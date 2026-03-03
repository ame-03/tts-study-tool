from splitter import split_text
from tts_engine import synthesize
from player import AudioPlayer

import os
import time

CACHE_DIR = "data/audio_cache"

class LearningSession:
    def __init__(self, player, file_list):
        self.player = player
        self.file_list = file_list

    def shadowing(self, pause=2.0):
        print("\n--- Shadowing Mode ---")
        print("Press Ctrl+C to stop\n")

        try:
            for file in self.file_list:
                self.player.play([file])
                time.sleep(pause)
                self.player.play([file])
        except KeyboardInterrupt:
            print("\nStopped.")

def ensure_cache_dir():
    if not os.path.exists(CACHE_DIR):
        os.makedirs(CACHE_DIR)

def generate_all(chunks):
    for i, chunk in enumerate(chunks):
        filename = os.path.join(CACHE_DIR, f"output_{i}.mp3")

        if not os.path.exists(filename):
            print(f"Generating: {filename}")
            synthesize(chunk, filename)

def play_one(player, index):
    filename = os.path.join(CACHE_DIR, f"output_{index}.mp3")
    player.play([filename])

def play_all(player, num_chunks):
    file_list = [
        os.path.join(CACHE_DIR, f"output_{i}.mp3")
        for i in range(num_chunks)
    ]
    player.play(file_list)

def main():
    text = "And this heat, this energy, it's always on, it's clean, and it actually holds our whole world together."

    chunks = split_text(text, max_words=15)
    player = AudioPlayer(speed=1.0)

    ensure_cache_dir()
    generate_all(chunks)

    while True:
        print("\n--- MENU ---")
        for i, chunk in enumerate(chunks):
            print(f"[{i}] {chunk}")
        print("[a] play all")
        print("[s] change speed")
        print("[h] shadowing mode")
        print("[q] quit")

        choice = input("Select: ")

        if choice == "a":
            play_all(player, len(chunks))

        elif choice == "s":
            try:
                new_speed = float(input("Enter speed (0.5 - 2.0): "))
                player.set_speed(new_speed)
                print(f"Speed set to {new_speed}")
            except ValueError:
                print("Invalid number.")

        elif choice == "h":
            file_list = [
                os.path.join(CACHE_DIR, f"output_{i}.mp3")
                for i in range(len(chunks))
            ]
            session = LearningSession(player, file_list)
            session.shadowing(pause=2.0)

        elif choice == "q":
            break

        elif choice.isdigit():
            index = int(choice)
            if 0 <= index < len(chunks):
                play_one(player, index)

if __name__ == "__main__":
    main()