import os

def play_audio(filename):
    os.system(f"mpg123 {filename}")