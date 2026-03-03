import os

class AudioPlayer:
    def __init__(self, speed=1.0):
        self.speed = speed

    def set_speed(self, speed):
        self.speed = speed

    def play(self, file_list):
        for file in file_list:
            command = (
                f"ffplay -nodisp -autoexit "
                f"-af atempo={self.speed} "
                f"{file} > /dev/null 2>&1"
            )
            os.system(command)