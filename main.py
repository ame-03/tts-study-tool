from splitter import split_text
from tts_engine import synthesize

import os
import subprocess

CACHE_DIR = "data/audio_cache"

def ensure_cache_dir():
    if not os.path.exists(CACHE_DIR):
        os.makedirs(CACHE_DIR)

def generate_all(chunks):
    for i, chunk in enumerate(chunks):
        filename = os.path.join(CACHE_DIR, f"output_{i}.mp3")

        if not os.path.exists(filename):
            print(f"Generating: {filename}")
            synthesize(chunk, filename)


def play_files(file_list):
    #command = ["mpg123", "-q"] + file_list
    #subprocess.call(command)
    command = "mpg123 -q " + " ".join(file_list)
    os.system(command)

def play_one(index):
    filename = os.path.join(CACHE_DIR, f"output_{index}.mp3")
    play_files([filename])

def play_all(num_chunks):
    file_list = [
        os.path.join(CACHE_DIR, f"output_{i}.mp3")
        for i in range(num_chunks)
    ]
    play_files(file_list)

def main():
    text = "And this heat, this energy, it's always on, it's clean, and it actually holds our whole world together."

    chunks = split_text(text, max_words=15)

    ensure_cache_dir()
    generate_all(chunks)

    for i, chunk in enumerate(chunks):
        print(f"[{i}] {chunk}")

    print("[a] play all")
    print("[q] quit")

    choice = input("Select: ")

    if choice == "a":
        play_all(len(chunks))
    elif choice == "q":
        return
    elif choice.isdigit():
        index = int(choice)
        if 0 <= index < len(chunks):
            play_one(index)

if __name__ == "__main__":
    main()