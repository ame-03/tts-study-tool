from splitter import split_text
from tts_engine import synthesize
from player import play_audio

import os
import subprocess

def play_files(file_list):
    command = ["mpg123", "-q"] + file_list
    subprocess.run(command)

def play_one(chunks, index):
    filename = f"output_{index}.mp3"
    synthesize(chunks[index], filename)
    play_files([filename])

def play_all(chunks):
    file_list = []

    for i, chunk in enumerate(chunks):
        filename = f"output_{i}.mp3"
        synthesize(chunk, filename)
        file_list.append(filename)

    play_files(file_list)

def main():
    text = "And this heat, this energy, it's always on, it's clean, and it actually holds our whole world together."

    chunks = split_text(text, max_words=15)

    for i, chunk in enumerate(chunks):
        print(f"[{i}] {chunk}")

    print("[a] play all")
    print("[q] quit")

    choice = input("Select: ")

    if choice == "a":
        play_all(chunks)
    elif choice == "q":
        return
    elif choice.isdigit():
        index = int(choice)
        if 0 <= index < len(chunks):
            play_one(chunks, index)

if __name__ == "__main__":
    main()