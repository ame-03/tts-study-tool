import os

def play_audio(filename):
   os.system(f"mpg123 {filename}")
    #os.system(f"cmd.exe /c start {filename}")